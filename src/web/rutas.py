from src.web.controllers.autenticacion.registro import registro_bp
from src.web.controllers.autenticacion.acceso import acceso_bp
from src.web.controllers.configuracion import configuracion_bp
from src.web.api.autenticacion import api_autenticacion_bp
from src.web.api.perfil import api_perfil_bp
from src.web.api.institucion import api_insitucion_bp

from src.web.controllers.usuarios_institucion import usuarios_institucion_bp
from src.web.controllers.instituciones import instituciones_bp
from src.web.controllers.usuarios import usuarios_bp


def registrar_bps(app):
    """
    Registra los blueprints que se levantan al incio
    """
    app.register_blueprint(registro_bp)
    app.register_blueprint(acceso_bp)
    app.register_blueprint(usuarios_institucion_bp)
    app.register_blueprint(instituciones_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(configuracion_bp)
    app.register_blueprint(api_autenticacion_bp)
    app.register_blueprint(api_perfil_bp)
    app.register_blueprint(api_insitucion_bp)