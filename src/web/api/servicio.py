from flask import Blueprint, jsonify, request
from src.web.schemas.servicio import servicio_schema
from src.core.servicio import list_servicios_paginated, get_servicio_by_id, list_tipos

api_servicios_bp = Blueprint("servicio_api", __name__, url_prefix="/api/services")

@api_instituciones_bp.get("/search")
def get_instituciones():
    """Devuelve los servicios pasandole page (default 1), per_page
    , una query y un tipo"""
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)
    total = page * per_page

    if per_page is None:
        return 'per_page parameter is required', 400

    servicios = list_servicio_paginated(page, per_page)
    servicios.append(total)
    
    datos = servicio_schema.dump(servicios)

    return datos

@api_instituciones_bp.get("/<id>")
def get_instituciones():
    """Devuelve el detalle del servicio pasado como parametro"""

    servicio = get_servicio_by_id(id)
    if(!servicio):
        return 'No existe o no se encontró un servicio con ese id.', 400

    datos = servicio_schema.dump(servicio)

    return datos

@api_instituciones_bp.get("/<id>")
def get_instituciones():
    """Devuelve el detalle del servicio pasado como parametro"""

    servicio = get_servicio_by_id(id)
    if(!servicio):
        return 'No existe o no se encontró un servicio con ese id.', 400

    datos = servicio_schema.dump(servicio)

    return datos