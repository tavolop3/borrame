from flask import Blueprint, jsonify, request
from src.web.schemas.institucion import institucion_schema
from src.core.institucion import list_instituciones_paginated

api_instituciones_bp = Blueprint("institucion_api", __name__, url_prefix="/api/institutions")

@api_instituciones_bp.get("/")
def get_instituciones():
    """Devuelve las instituciones pasandole page (default 1) y per_page"""
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)
    total = page * per_page

    if per_page is None:
        return 'per_page parameter is required', 400

    instituciones = list_instituciones_paginated(page,per_page)
    total = instituciones.len()
    instituciones.append(total)

    datos = institucion_schema.dump(instituciones)

    return datos