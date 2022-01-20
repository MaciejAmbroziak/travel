from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


DB = SQLAlchemy()


class TripTypes(DB.Model):
    """
    Class representing Trip Types
    """
    __tablename__ = "TripTypes"
    id = DB.Column("id", DB.Integer, primary_key=True)
    trip_type = DB.Column(DB.String(128), unique=True)
    trips = relationship("Trips")


class Users(DB.Model):
    """
    Class representing Users
    """
    __tablename__ = "Users"
    id = DB.Column("id", DB.Integer, primary_key=True)
    nick_name = DB.Column(DB.String(128))
    first_name = DB.Column(DB.String(128))
    last_name = DB.Column(DB.String(128))
    email = DB.Column(DB.String(128), unique=True)
    hashed_password = DB.Column(DB.String(128))
    trips = relationship("Trips")
    willing_to_go = relationship("WillingToGo")

    def is_active(self):
        """True, as all users are active."""
        return self.is_active()

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self, _id):
        """Return True if the user is authenticated."""
        if self.id == _id:
            return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Trips(DB.Model):
    """
    Class representing Trips
    """
    __tablename__ = "Trips"
    id = DB.Column("id", DB.Integer, primary_key=True)
    where_to = DB.Column(DB.String(128))
    start = DB.Column(DB.Date)
    end = DB.Column(DB.Date)
    description = DB.Column(DB.String(1200))
    main_photo_url = DB.Column(DB.String(128))
    trip_type_id = DB.Column(DB.Integer, ForeignKey('TripTypes.id'))
    organizing_user_id = DB.Column(DB.Integer, ForeignKey("Users.id"))
    willing_to_go = relationship("WillingToGo")



class WillingToGo(DB.Model):
    """
    Class representing Users Willing to go to Trip
    """
    __tablename__ = "WillingToGo"
    id = DB.Column("id", DB.Integer, primary_key=True)
    taking_part_user_id = DB.Column(DB.Integer,  ForeignKey("Users.id"), unique=True)
    trip_id = DB.Column(DB.Integer, ForeignKey("Trips.id"))
