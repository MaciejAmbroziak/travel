import sqlalchemy.exc
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import (
    login_user,
    logout_user,
    login_required,
    LoginManager,
    current_user,
)

from travel.db import TripTypes
from travel.server.trip_form import TripForm
from travel.server.trip_type_form import TripTypeForm
from travel.server.user_form import UserForm
from travel.services.index import (
    get_trip_form,
    get_list_of_trips_id,
    post_trip_form,
    get_trip_types,
    register_trip_type,
    register_user_for_trip,
    get_willing_to_go,
)
from travel.services.login import (
    check_user,
    register_user,
    user_loader,
    check_if_user_email_present,
    get_user,
    get_user_id,
)

index_blueprint = Blueprint("index", __name__)


@index_blueprint.route("/")
def index():
    return render_template("welcome.html")


@index_blueprint.route("/trips/<int:_id>", methods=["GET", "POST"])
@login_required
def trip(_id):
    users = get_willing_to_go(_id)
    form = get_trip_form(_id)
    return render_template("trip.html", form=form, users=users)


@index_blueprint.route("/trips")
@login_required
def trips():
    trips_form = []
    for _id in get_list_of_trips_id():
        trips_form.append(get_trip_form(_id))
    if request.method == "POST":
        return redirect(url_for("index.trip"))
    return render_template("trips.html", my_trips=trips_form)


@index_blueprint.route("/trip", methods=["get", "post"])
@login_required
def add_trip():
    form = TripForm(request.form)
    form.trip_type.choices = get_trip_types()
    if request.method == "POST":
        post_trip_form(form)
        return redirect(url_for("index.trips"))
    return render_template("trip.html", form=form)


@index_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        if not check_if_user_email_present(form.email.data):
            register_user(form)
            return redirect(url_for("index.login"))
        else:
            return render_template(
                "registered.html", message="you are already registered"
            )
    return render_template("register.html", form=form)


@index_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = UserForm(request.form)
    if request.method == "POST":
        if check_user(form.email.data, form.password.data):
            login_user(user_loader(form.email.data))
        return redirect(url_for("index.index"))
    return render_template("login.html", form=form)


@index_blueprint.route("/registered", methods=["get", "post"])
def registered():
    if request.method == "POST":
        return redirect(url_for("index.login"))
    return render_template("registered.html")


@index_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))


@index_blueprint.route("/trip_type", methods=["get", "post"])
@login_required
def trip_type():
    form = TripTypeForm(request.form)
    if request.method == "POST":
        register_trip_type(form)
        return redirect(url_for("index.add_trip"))
    return render_template("trip_type.html", form=form)


@index_blueprint.route("/trip/<int:trip_id>", methods=["POST", "GET"])
def I_will_go(trip_id):
    users = get_willing_to_go(trip_id)
    if request.method == "POST":
        try:
            register_user_for_trip(trip_id, get_user_id(current_user.get_id()))
        except sqlalchemy.exc.IntegrityError:
            return render_template("registered.html", message="You are registered")
        return redirect(url_for("index.trip", _id=trip_id, users=users))
    return redirect(url_for("index.trip", _id=trip_id))
