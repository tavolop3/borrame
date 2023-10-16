from functools import wraps
from flask import session, abort, redirect
from src.core.autenticacion import listar_permisos_por_email_usuario


def esta_autenticado(session):
    return session.get("usuario") is not None


def necesita_login(permisos_requeridos=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not esta_autenticado(session):
                return abort(401)

            if permisos_requeridos:
                permisos_usuario = listar_permisos_por_email_usuario(session["usuario"])
                if not permisos_usuario:
                    return abort(403)

                for permiso in permisos_requeridos:
                    if permiso not in permisos_usuario:
                        return abort(403)

            return f(*args, **kwargs)

        return decorated_function

    return decorator

def no_necesita_login():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if esta_autenticado(session):
                return redirect("/")
        
            return f(*args, **kwargs)
    
        return decorated_function
    
    return decorator

def tiene_permiso(permisos_requeridos=None):
    permisos_usuario = listar_permisos_por_email_usuario(session["usuario"])
    
    for permiso in permisos_requeridos:
        if permiso not in permisos_usuario:
            return False
    
    return True