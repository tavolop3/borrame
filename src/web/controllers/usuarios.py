from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask_paginate import Pagination, get_page_parameter
from src.core.autenticacion.formularios import CreateForm
from src.core import autenticacion #dentro de autenticacion esta definido usuario
from src.core import institucion


usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")

@usuarios_bp.get("/")
def index():
    usuarios = autenticacion.listar_usuarios()

    return render_template(
        "usuarios/index.html",
        usuarios=usuarios
    )

@usuarios_bp.get("/<id>")
def show(id):
    usuario = autenticacion.buscar_usuario_por_id(id)

    return render_template("usuarios/show.html", usuario=usuario)

@usuarios_bp.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    usuario = autenticacion.buscar_usuario_por_id(id)
    form = CreateForm()
    if form.validate_on_submit():
        # Verifico si el username ya esta registrado
        existing_user = autenticacion.buscar_usuario_por_username(request.form["username"])
        if existing_user and existing_user.id != int(id):
            flash("Error: El nombre de usuario ya está registrado.", "error")
            return render_template("usuarios/update.html", usuario=usuario, form=form)
        
        # Verifico si el correo ya esta registrado
        existing_user = autenticacion.buscar_usuario_por_email(request.form["email"])
        if existing_user and existing_user.id != int(id):
            flash("Error: El correo electrónico ya está registrado.", "error")
            return render_template("usuarios/update.html", usuario=usuario, form=form)
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        #activo = request.form["activo"]
        autenticacion.update_usuario(
            id=id,
            username=username,
            password=password,
            email=email,
            nombre=nombre,
            apellido=apellido,
            #activo=activo,
        )
        flash("Usuario actualizado exitosamente.", "success")
        return redirect(url_for("usuarios.index"))
    elif not form.validate_on_submit() and request.method == "POST":
        flash("Ocurrió un error.", "error")
    return render_template("usuarios/update.html", usuario=usuario, form=form)

@usuarios_bp.route("/create", methods=["GET", "POST"])
def create():
    form = CreateForm()
    if form.validate_on_submit():
                # Verifico si el username ya esta registrado
        existing_user = autenticacion.buscar_usuario_por_username(request.form["username"])
        if existing_user:
            flash("Error: El nombre de usuario ya está registrado.", "error")
            return render_template("usuarios/create.html", form=form)
        
        # Verifico si el correo ya esta registrado
        existing_user = autenticacion.buscar_usuario_por_email(request.form["email"])
        if existing_user:
            flash("Error: El correo electrónico ya está registrado.", "error")
            return render_template("usuarios/create.html", form=form)
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        # TODO poner el desplegable!!!
        #activo = request.form["activo"]
        autenticacion.crear_usuario(
            username=username,
            password=password,
            email=email,
            nombre=nombre,
            apellido=apellido,
            #activo=activo,
        )
        flash("Usuario creado exitosamente.", "success")
        return redirect(url_for("usuarios.index"))
    elif not form.validate_on_submit() and request.method == "POST":
        flash("Ocurrió un error.", "error")
    return render_template("usuarios/create.html", form=form)

@usuarios_bp.post("/delete/<id>")
def destroy(id=None):
    if id:
        autenticacion.delete_usuario(id)
        flash("Usuario eliminado exitosamente.", "success")
        return redirect(url_for("usuarios.index"))
    
@usuarios_bp.get("/activate/<id>")
def activate_usuario(id):
    autenticacion.activate_usuario(id)
    flash("Usuario habilitado exitosamente.", "success")
    return redirect(url_for("usuarios.show", id=id))

@usuarios_bp.get("/deactivate/<id>")
def deactivate_usuario(id):
    autenticacion.deactivate_usuario(id)
    flash("Usuario deshabilitado exitosamente.", "success")
    return redirect(url_for("usuarios.show", id=id))


@usuarios_bp.route("/testeo-instituciones/<id>")
def mostrar_instituciones(id):
    user = autenticacion.buscar_usuario_por_id(id)
    if user is not None:
        return render_template("usuarios/instituciones-del-usuario.html", usuario=user)
    else:
        flash("Usuario no encontrado", "error")
        return redirect(url_for("usuarios.index"))

@usuarios_bp.route("/activar-institucion/<int:user_id>/<int:institution_id>")
def activar_institucion(user_id, institution_id):
    user = autenticacion.buscar_usuario_por_id(user_id)
    if user is not None:
        autenticacion.asignar_institucion_activa(user_id, institution_id)
        flash("Institución activa asignada con éxito", "success")
        return redirect(url_for("usuarios.mostrar_instituciones",id=user.id))
    else:
        flash("Fallo la activación", "error")
        return redirect(url_for("usuarios.mostrar_instituciones",id=user.id))
