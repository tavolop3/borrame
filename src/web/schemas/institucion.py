from marshmallow import fields, Schema

class InstitucionSchema(Schema):
    # data = { esto es con muchos 
    nombre = fields.Str(required=True)
    info = fields.Str(required=True)
    direccion = fields.Str(required=True)
    localizacion = fields.Str(required=True)
    web = fields.Str(required=True)
    horario_atencion = fields.Str(required=True)
    contacto = fields.Str(required=True)
    habilitado = fields.Bool(required=True)

    page = fields.Int(required=true)
    per_page = fields.Int(required=true)
    total = fields.Int(required=true)

institucion_schema = InstitucionSchema(many=True)