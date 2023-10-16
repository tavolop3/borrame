from flask import Blueprint, jsonify, request
from src.core.autenticacion import chequear_usuario, buscar_usuario_por_email
from src.web.schemas.autenticacion import autenticacion_schema
from marshmallow import ValidationError

api_autenticacion_bp = Blueprint("autenticacion_api", __name__, url_prefix="/api")


@api_autenticacion_bp.get("/auth")
def auth():
    """Devuelve el id recibiendo email y password por json"""
    req_data = request.json

    try:
        data_validada = autenticacion_schema.load(req_data)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    user = chequear_usuario(data_validada["email"], data_validada["password"])
    if not user:
        return jsonify({"error": "Usuario y/o contraseña invalidos"}), 401

    id = {"id": buscar_usuario_por_email(data_validada["email"]).id}
    return jsonify(id), 200
