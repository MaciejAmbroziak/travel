from wtforms import Form, StringField, PasswordField, validators


class UserForm(Form):
    nick_name = StringField("Nick name", [validators.Length(min=4, max=25)])
    email = StringField("Email Address", [validators.Length(min=6, max=35)])
    first_name = StringField("First name", [validators.Length(min=2, max=100)])
    last_name = StringField("Last name", [validators.Length(min=2, max=100)])
    password = PasswordField(
        "New Password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repeat Password")
