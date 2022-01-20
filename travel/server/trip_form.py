from wtforms import Form, StringField, SelectField, SubmitField, IntegerField
from wtforms.fields import DateField


class TripForm(Form):
    id = IntegerField("Id")
    trip_type = SelectField("Trip type", choices=[], default=0)
    where_to = StringField("Where to")
    organizing_user = StringField("Organizer")
    start = DateField("Start")
    end = DateField("End")
    description = StringField("Description")
    main_photo_url = StringField("photo url")
    submit = SubmitField("I will go")
