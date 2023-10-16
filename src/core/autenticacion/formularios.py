from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, validators
from wtforms.validators import InputRequired, Length


class RegistroSimpleForm(FlaskForm):
    nombre = StringField("Nombre", [InputRequired(), validators.Length(min=3, max=25)])
    apellido = StringField(
        "Apellido", [InputRequired(), validators.Length(min=3, max=25)]
    )
    email = EmailField("Email", validators=[InputRequired(), Length(max=50)])


class ConfirmarRegistroForm(FlaskForm):
    username = StringField(
        "Usuario", validators=[InputRequired(), Length(min=3, max=50)]
    )

    password = PasswordField(
        "Contraseña",
        [
            InputRequired(),
            Length(min=3, max=255),
            validators.EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repetir contraseña")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Length(max=50)])

    password = PasswordField("Contraseña", [InputRequired(), Length(min=3, max=255)])





class CreateForm(FlaskForm):
    username = StringField("Nombre de usuario", [InputRequired(), validators.Length(min=3, max=25)])
    password = StringField(
        "Contraseña (no va jeje)", [InputRequired(), validators.Length(min=3, max=250)]
    )
    email = StringField(
        "Email", [InputRequired(), validators.Length(min=3, max=100)]
    )
    nombre = StringField(
        "Nombre", [InputRequired(), validators.Length(min=3, max=25)]
    )
    apellido = StringField("Apellido", [InputRequired(), validators.Length(min=3, max=25)])
    