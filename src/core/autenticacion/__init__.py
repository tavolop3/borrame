from src.core.database import db
from src.core.autenticacion.usuario import Usuario
from src.core.institucion.models.institucion import Institucion
from src.core.institucion import get_institucion_by_id
from core.autenticacion.bcrypt import bcrypt
from src.core.autenticacion.roles_y_permisos import Usuario_Tiene_Rol, Rol


def listar_usuarios():
    return Usuario.query.all()


def crear_usuario_simple(nombre, apellido, email):
    usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        email=email,
        #activo=False,
    )
    db.session.add(usuario)
    db.session.commit()


# agregar_rol(nombre):
#     rol = Rol(nombre=nombre)
#     db.session.add(rol)
#     db.session.commit()


def completar_usuario(email, username, password):
    hash = bcrypt.generate_password_hash(password.encode("utf-8"))
    password = hash.decode("utf-8")

    usuario = buscar_usuario_por_email(email)

    usuario.username = username
    usuario.password = password
    usuario.activo = True

    db.session.commit()

def crear_usuario(**kwargs):
    crear_usuario_simple(kwargs["nombre"],kwargs["apellido"],kwargs["email"])
    completar_usuario(kwargs["email"],kwargs["username"],kwargs["password"])
    #usuario = Usuario(**kwargs)
    #db.session.add(usuario)
    #db.session.commit()

    #return usuario

def agregar_rol_a_usuario(rol, user, institucion):
    rol = Rol.query.filter_by(nombre=rol).first()
    user = buscar_usuario_por_email(user)
    institucion = Institucion.query.filter_by(nombre=institucion).first()
    if rol.nombre == "superadmin":
        rol_inst = Usuario_Tiene_Rol(rol_id=rol.id, usuario_id=user.id)
    else:
        rol_inst = Usuario_Tiene_Rol(rol.id, institucion.id, user.id)
    db.session.add(rol_inst)
    db.session.commit()


def agregar_permiso_a_rol(permiso, rol):
    rol.permisos.append(permiso)
    db.session.commit()


def buscar_usuario_por_email(email):
    return Usuario.query.filter_by(email=email).first()


def buscar_usuario_por_username(username):
    return Usuario.query.filter_by(username=username).first()

def buscar_usuario_por_id(id):
    return Usuario.query.filter_by(id=id).first()

def chequear_usuario(email, password):
    usuario = buscar_usuario_por_email(email)

    if usuario and bcrypt.check_password_hash(
        usuario.password, password.encode("utf-8")
    ):
        return usuario
    else:
        return None

def listar_permisos_por_email_usuario(email):
    usuario = buscar_usuario_por_email(email)
    usuario_tiene_rol = Usuario_Tiene_Rol.query.filter_by(usuario_id=usuario.id)
    permisos_usuario = []

    for user_rol in usuario_tiene_rol:
        permisos = Rol.query.filter_by(id=user_rol.rol_id).first().permisos
        for permiso in permisos:
            permisos_usuario.append(permiso.nombre)

    return permisos_usuario
#TODO ver el cambio de contraseña
def update_usuario(**kwargs):
    usuario = buscar_usuario_por_id(kwargs["id"])
    usuario.username = kwargs["username"]
    usuario.password = kwargs["password"]
    usuario.email = kwargs["email"]
    usuario.nombre = kwargs["nombre"]
    usuario.apellido = kwargs["apellido"]
    #usuario.activo = kwargs["activo"]
    #usuario.created_at = kwargs["created_at"]
    #usuario.updated_at = kwargs["updated_at"]

    db.session.commit()

#TODO establecer esto, ver como seleccionarlo del listado de instituciones activas
#def establecer_institucion_activa(id):

def delete_usuario(id):
    Usuario.query.filter_by(id=id).delete()
    db.session.commit()

def activate_usuario(id):
    usuario = buscar_usuario_por_id(id)
    usuario.activo = True
    db.session.commit()

def deactivate_usuario(id):
    usuario = buscar_usuario_por_id(id)
    usuario.activo = False
    db.session.commit()
# TODO

def get_usuario_institucion_activa(id):
    # Primero, busca al usuario por su id
    usuario = Usuario.query.filter_by(id=id).first()

    if usuario:
        # Luego, obtén la institución activa asociada a ese usuario
        institucion_activa = Institucion.query.get(usuario.institucion_activa_id)
        return institucion_activa
    else:
        # Maneja el caso en el que no se encuentre el usuario
        return None  # Puedes devolver None u otro valor que consideres apropiado

def get_instituciones_by_id(id):
    #busca al usuario por su id
    usuario = Usuario.query.filter_by(id=id).first()

    if usuario:
        # instituciones del usuario
        instituciones = usuario.instituciones
        return instituciones
    else:
        # Maneja el caso en el que no se encuentre el usuario
        return []
def agregar_institucion_a_usuario(usuario_id,institucion_id):
    # Busca al usuario por su nombre de usuario
    usuario = Usuario.query.filter_by(id=usuario_id).first()

    if usuario:
        # Obtiene la institución por su ID
        institucion = Institucion.query.get(institucion_id)

        if institucion:
            # Agrega la institución al usuario si no está relacionada previamente
            if institucion not in usuario.instituciones:
                usuario.instituciones.append(institucion)
                db.session.commit()
                print(usuario.instituciones)
                print(institucion)
                return True
            else:
                return "La institución ya está relacionada con el usuario."

        else:
            return "La institución con el ID especificado no existe."

    else:
        return "El usuario con el nombre de usuario especificado no existe."    
    
def asignar_institucion_activa(usuario_id, institucion_id):
    # Busca al usuario por su ID
    usuario = Usuario.query.get(usuario_id)

    # Obtiene la nueva institución por su ID
    institucion = Institucion.query.get(institucion_id)

    if usuario and institucion:
        # Actualiza el campo 'institucion_activa_id' del usuario con el ID de la nueva institución
        usuario.institucion_activa = institucion

        # Realiza un commit en la base de datos para guardar el cambio
        db.session.commit()

        return True
    else:
        return "El usuario o la institución con el ID especificado no existen."


