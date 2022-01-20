# PSL
from typing import List

# Own
from travel.db import Trips, TripTypes, DB, Users, WillingToGo
from travel.server.trip_form import TripForm
from travel.services.login import user_loader


def get_trips_id():
    return DB.session.query(Trips.id).all()


def get_trip_types() -> List[str]:
    """
    Caller: server.trips view
    :return: List of trips type.
    """
    return [word[0] for word in DB.session.query(TripTypes.trip_type).all()]


def get_trip_type_by_id(trip_type_id):
    """
    Caller: get_trip_form
    :return: trip_type of given trip_type_id
    :type: str
    """
    return DB.session.query(TripTypes.trip_type).join(Trips).filter(trip_type_id == TripTypes.id).first()[0]


def get_trip_type_id_by_name(name):
    return DB.session.query(TripTypes.id).filter(TripTypes.trip_type == name).first()[0]


def get_organizing_user_by_id(organizing_user_id):
    return DB.session.query(Users.nick_name).join(Trips).filter(organizing_user_id == Users.id).first()[0]


def get_organizing_user_id_by_nick_name(nick_name):
    return DB.session.query(Users.id).filter(Users.nick_name == nick_name).first()[0]


def get_trip_form(_id):
    """
    Function that retrieves trip form of given id from database
    :param _id: id of given trip
    :type: int
    :return: trip form
    :type: trip form
    """
    my_trip = DB.session.query(Trips).filter(Trips.id == _id).first()
    form = TripForm(
        id=_id,
        trip_type=get_trip_type_by_id(my_trip.trip_type_id),
        where_to=my_trip.where_to,
        organizing_user=get_organizing_user_by_id(my_trip.organizing_user_id),
        start=my_trip.start,
        end=my_trip.end,
        description=my_trip.description,
        main_photo_url=my_trip.main_photo_url
    )
    form.trip_type.choices = get_trip_types()
    form.trip_type.default = get_trip_type_by_id(my_trip.trip_type_id)
    return form


def post_trip_form(form):
    #    trip = Trips(form)
    trip = Trips(
        trip_type_id=get_trip_type_id_by_name(form.trip_type.data),
        where_to=form.where_to.data,
        organizing_user_id=get_organizing_user_id_by_nick_name(form.organizing_user.data),
        start=form.start.data,
        end=form.end.data,
        description=form.description.data,
        main_photo_url=form.main_photo_url.data
    )
    DB.session.add(trip)
    DB.session.commit()

def register_trip_type(form):
    trip_type = TripTypes(trip_type=form.trip_type.data)
    if DB.session.query(TripTypes.trip_type).filter(TripTypes.trip_type == trip_type.trip_type):
        DB.session.add(trip_type)
        DB.session.commit()
    else:
        return 'This trip"type is already registered'


def register_user_for_trip(trip_id, user_id):
    user = WillingToGo(taking_part_user_id=user_id, trip_id=trip_id)
    DB.session.add(user)
    DB.session.commit()


def get_willing_to_go(trip_id):
    return [user[0] for user in DB.session.query(Users.nick_name).join(WillingToGo).where(WillingToGo.trip_id == trip_id).all()]

def get_list_of_trips_id():
    trips = get_trips_id()
    forms = []
    for i, trip in enumerate(trips):
        forms.append(trip.id)
    return forms
