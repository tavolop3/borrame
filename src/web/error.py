from flask import render_template


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }

    return render_template("error.html", **kwargs), 404


def unauthorized(e):
    kwargs = {
        "error_name": "401 Unauthorized",
        "error_description": "Tenés que iniciar sesión para acceder a esta página",
    }

    return render_template("error.html", **kwargs), 401


def forbidden(e):
    kwargs = {
        "error_name": "403 Forbidden",
        "error_description": "No tenés permisos para acceder a esta página",
    }

    return render_template("error.html", **kwargs), 403
