from flask import Blueprint, render_template, request, redirect, url_for, flash
from core.autenticacion.mail import enviar_mail
from src.web.helpers.autenticacion import no_necesita_login
from src.core.autenticacion import (
    buscar_usuario_por_email,
    crear_usuario_simple,
    completar_usuario,
    buscar_usuario_por_username,
)
from src.core.autenticacion.formularios import RegistroSimpleForm, ConfirmarRegistroForm

registro_bp = Blueprint("registro", __name__, url_prefix="/autenticacion/registro")


@registro_bp.route("/", methods=["GET", "POST"])
@no_necesita_login()
def registro_simple():
    """
    Muestra la vista de la primera etapa del registro, además valida los
    parametros, envia el mail de confirmación y guarda al usuario si
    se recibió el formulario.
    """
    form = RegistroSimpleForm()
    if form.validate_on_submit():
        if buscar_usuario_por_email(form.email.data):
            flash("El mail ingresado ya se encuentra registrado", "error")

        crear_usuario_simple(form.nombre.data, form.apellido.data, form.email.data)
        # TODO : cambiar el link de confirmacion por una env
        html = """<p>Gracias por registrarte 🤝</p>  
                  <p>Para continuar con tu registro hacé click en el siguiente enlace: <a href="http://127.0.0.1:5000/autenticacion/registro/confirmar?email={0}">confirmar</a></p>
               """.format(
            form.email.data
        )
        enviar_mail("Confirmación de cuenta", form.email.data, html=html)

        flash('Se envió un mail de confirmación a su email para finalizar el registro.')
        return redirect(url_for("acceso.login"))

    return render_template("autenticacion/registro.html", form=form)


@registro_bp.route("/confirmar", methods=["GET", "POST"])
def confirmar_registro():
    """
    Termina el registro del usuario, pidiendo en un formulario username y pass
    Se valida que no sea un mail invalido y que el username no esté tomado,
    además de las validaciones de los campos del formulario.
    """
    form = ConfirmarRegistroForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        if not buscar_usuario_por_email(email):
            flash("Ese email no existe o no se encontró.", "error")
            return redirect(url_for("acceso.login"))

        if buscar_usuario_por_username(form.username.data):
            flash("Ese nombre de usuario ya está en uso", "error")
            return redirect(url_for("acceso.login"))

        completar_usuario(email, form.username.data, form.password.data)

        flash("Ha finalizado su registro, puede usar su cuenta.", "success")
        return redirect(url_for("acceso.login"))

    return render_template(
        "autenticacion/confirmar-registro.html", form=form, email=request.args["email"]
    )
