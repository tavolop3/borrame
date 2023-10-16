from flask import Flask
from flask import render_template
from flask_session import Session
from core import autenticacion
from src.web import error
from src.core import database
from src.core import seeds
from src.web.config import config
from core.autenticacion.mail import mail
from src.web.config import config
from src.core import seeds
from src.web.controllers.configuracion import configuracion_bp

from src.web.rutas import registrar_bps
from src.web.helpers import autenticacion

session = Session()


def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    session.init_app(app)
    database.init_app(app)
    mail.init_app(app)

    registrar_bps(app)

    @app.get("/")
    def home():
        return render_template("index.html")

    app.register_error_handler(404, error.not_found_error)
    app.register_error_handler(401, error.unauthorized)
    app.register_error_handler(403, error.forbidden)

    app.jinja_env.globals.update(esta_autenticado=autenticacion.esta_autenticado, tiene_permiso=autenticacion.tiene_permiso)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run()

    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run()

    return app
