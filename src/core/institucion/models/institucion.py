from src.core.database import db
from src.core.autenticacion.roles_y_permisos import Usuario_Tiene_Rol


class Institucion(db.Model):
    __tablename__ = "institucion"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String, nullable=False, unique=True)
    info = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=False)
    localizacion = db.Column(db.String, nullable=False)
    web = db.Column(db.String, nullable=False)
    palabra_clave = db.Column(db.ARRAY(db.String), nullable=False)
    horario_atencion = db.Column(db.String, nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    contacto = db.Column(db.String, nullable=False)
    #TODO ver si esto va o no, lo saque para testear
    #usuarios = db.relationship('Usuario', back_populates='institucion')
    # rol_institucion = db.Column(db.Integer(), db.ForeignKey("usuario_tiene_rol.id"))

    def __init__(
        self,
        nombre=None,
        info=None,
        direccion=None,
        localizacion=None,
        web=None,
        palabra_clave=None,
        horario_atencion=None,
        contacto=None,
    ):
        self.nombre = nombre
        self.info = info
        self.direccion = direccion
        self.localizacion = localizacion
        self.web = web
        self.palabra_clave = palabra_clave
        self.horario_atencion = horario_atencion
        self.habilitado = False
        self.contacto = contacto
