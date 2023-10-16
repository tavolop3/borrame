from core import autenticacion
from flask import Blueprint, redirect, url_for, flash, session, render_template
from src.core.autenticacion.formularios import LoginForm
from src.web.helpers.autenticacion import necesita_login, no_necesita_login

acceso_bp = Blueprint("acceso", __name__, url_prefix="/autenticacion/acceso")


@acceso_bp.route("/login", methods=["GET", "POST"])
@no_necesita_login()
def login():
    """
    Realiza el login, muestra el formulario si es un get, sino valida al usuario
    e inicia la sesión.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = autenticacion.chequear_usuario(form.email.data, form.password.data)

        if not user:
            flash("Usuario y/o contraseña invalidos", "error")
            return redirect(url_for("acceso.login"))

        session["usuario"] = user.email

        flash("La sesión se inició correctamente", "success")
        return redirect(url_for("home"))

    return render_template("autenticacion/login.html", form=form)


@acceso_bp.get("/logout")
def logout():
    if session["usuario"]:
        del session["usuario"]
        session.clear()
        flash("La sesión se cerró correctamente", "info")
    else:
        flash("No estás logueado", "info")

    return redirect(url_for("acceso.login"))


@acceso_bp.get("/quiensoy")
@necesita_login(permisos_requeridos=["admin"])
def quiensoy():
    return "soy " + session["usuario"]
