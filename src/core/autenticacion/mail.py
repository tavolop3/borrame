from flask import Flask
from flask_mail import Mail
from flask_mail import Message
import os

mail = Mail()


def init_app(app):
    mail.init_app(app)


def enviar_mail(asunto, destinatario, html="", mensaje=""):
    """
    Envía un mail real si la variable de entorno MAIL_HABILITADO es True,
    sino se imprime en consola.
    """
    env = os.getenv("MAIL_HABILITADO")
    if env == "True":
        msg = Message(asunto, recipients=[destinatario], html=html, body=mensaje)
        mail.send(msg)
    else:
        print(
            "Correo enviado a: "
            + destinatario
            + " asunto: "
            + asunto
            + " mensaje: "
            + mensaje
            + " html: "
            + html
        )
