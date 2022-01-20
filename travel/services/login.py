import bcrypt
from flask_login import LoginManager

from travel.server.user_form import UserForm

LOGIN_MANAGER = LoginManager()

@LOGIN_MANAGER.user_loader
def user_loader(email):
    """Given *email*, return the associated User object.
    :param email: user to retrieve

    """
    try:
        return get_user(email)
    except:
        return None

from travel.db import Users, DB


def get_user(email):
    return DB.session.query(Users).filter_by(email=email).first()

def get_user_id(email):
    return DB.session.query(Users.id).filter_by(email=email).first()[0]


def check_user(email, password):
    hashed_password = DB.session.query(Users.hashed_password).filter_by(email=email).first()[0]
    if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(hashed_password, 'utf-8')):
        return True


def check_if_user_email_present(email):
    if DB.session.query(Users.email).filter_by(email=email).first():
        return True


def register_user(form):
    salt_byte=bcrypt.gensalt()
    user = Users(nick_name=form.nick_name.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                hashed_password=bcrypt.hashpw(bytes(form.password.data, 'utf8'), salt_byte).decode('utf8'))
    DB.session.add(user)
    DB.session.commit()





