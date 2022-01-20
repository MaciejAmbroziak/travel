from wtforms import Form, StringField, validators, SubmitField


class TripTypeForm(Form):
    trip_type = StringField("Trip Type", [validators.Length(min=4, max=25)])
    submit = SubmitField("Insert")
