from flask import Blueprint, jsonify, request, session
from src.web.helpers.autenticacion import necesita_login
from src.web.schemas.perfil import perfil_schema
from marshmallow import ValidationError
from src.core.autenticacion import buscar_usuario_por_email

api_perfil_bp = Blueprint("perfil_api", __name__, url_prefix="/api")


@api_perfil_bp.get("/me/profile")
@necesita_login()
def profile():
    """Devuelve los datos del usuario autenticado"""

    email = session["usuario"]
    usuario = buscar_usuario_por_email(email)

    datos = perfil_schema.dump(usuario)

    return jsonify(datos), 200
