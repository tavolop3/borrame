from os import getenv
from dotenv import load_dotenv


class Config(object):
    """
    Configuración base
    """

    SECRET_KEY = "secret"
    TESTING = False
    SESSION_TYPE = "filesystem"


class DevelopmentConfig(Config):
    """
    Configuracion de development.
    """

    load_dotenv()

    DB_USER = getenv("DB_USER")
    DB_PASS = getenv("DB_PASS")
    DB_HOST = getenv("DB_HOST")
    DB_NAME = getenv("DB_NAME")
    DB_PORT = getenv("DB_PORT")

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    MAIL_SERVER = getenv("MAIL_SERVER")
    MAIL_DEFAULT_SENDER = getenv("MAIL_DEFAULT_SENDER")
    MAIL_PORT = getenv("MAIL_PORT")
    MAIL_USERNAME = getenv("MAIL_USERNAME")
    MAIL_PASSWORD = getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = getenv("MAIL_USE_TLS")
    MAIL_USE_SSL = getenv("MAIL_USE_SSL")


config = {"development": DevelopmentConfig}
