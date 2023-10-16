from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired, InputRequired, Length


class CreateForm(FlaskForm):
    nombre = StringField("Nombre", [InputRequired(), validators.Length(min=3, max=25)])
    info = StringField(
        "Información", [InputRequired(), validators.Length(min=3, max=250)]
    )
    direccion = StringField(
        "Dirección", [InputRequired(), validators.Length(min=3, max=100)]
    )
    localizacion = StringField(
        "Localizacion", [InputRequired(), validators.Length(min=3, max=25)]
    )
    web = StringField("Web", [InputRequired(), validators.Length(min=3, max=25)])
    palabra_clave = StringField(
        "Palabras clave", [InputRequired(), validators.Length(min=3, max=210)]
    )
    horario_atencion = StringField(
        "Horarios de atención ", [InputRequired(), validators.Length(min=3, max=250)]
    )
    contacto = StringField(
        "Contacto", [InputRequired(), validators.Length(min=3, max=150)]
    )
