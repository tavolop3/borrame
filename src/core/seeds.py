from src.core.database import db
from src.core.configuracion import create_configuracion, create_info_contacto
from src.core.database import db
from src.core.institucion.models.institucion import Institucion
from src.core.institucion import create_institucion, delete_institucion

from src.core.autenticacion.roles_y_permisos import Rol, Permiso
from src.core.autenticacion import (
    completar_usuario,
    crear_usuario_simple,
    agregar_rol_a_usuario,
    agregar_permiso_a_rol,
    agregar_institucion_a_usuario,
)


def run():
    config = create_configuracion(
        cant_elementos_pag=10,
        mantenimiento=True,
        mantenimiento_msg="Estamos en mantenimiento",
    )

    info1 = create_info_contacto(nombre="Teléfono", activo=False)

    info2 = create_info_contacto(nombre="Email", activo=True)

    info3 = create_info_contacto(nombre="Dirección", activo=True)

    info4 = create_info_contacto(nombre="Sitio Web", activo=False)

    inst1 = (
        create_institucion(
            nombre="a",
            info="a",
            direccion="a",
            localizacion="a",
            web="a",
            palabra_clave=["a", "b"],
            horario_atencion=["10-19"],
            contacto="no hay",
        ),
    )
    inst2 = create_institucion(
        nombre="b",
        info="b",
        direccion="b",
        localizacion="d",
        web="d",
        palabra_clave=["d", "b"],
        horario_atencion=["11-12"],
        contacto="no",
    )
    crear_usuario_simple(
        email="admin@gmail.com",
        nombre="admin",
        apellido="admin",
    )

    completar_usuario("admin@gmail.com", "admin", "admin")
    rol = Rol(nombre="superadmin")
    db.session.add(rol)
    db.session.commit()
    permiso1 = Permiso(nombre="institucion_index")
    permiso2 = Permiso(nombre="institucion_show")
    permiso3 = Permiso(nombre="institucion_update")
    permiso4 = Permiso(nombre="institucion_create")
    permiso5 = Permiso(nombre="institucion_destroy")
    permiso6 = Permiso(nombre="institucion_activate")
    permiso7 = Permiso(nombre="institucion_deactivate")
    permiso_show = Permiso(nombre="configuracion_show")
    permiso_update = Permiso(nombre="configuracion_update")

    agregar_permiso_a_rol(permiso1, rol)
    agregar_permiso_a_rol(permiso2, rol)
    agregar_permiso_a_rol(permiso3, rol)
    agregar_permiso_a_rol(permiso4, rol)
    agregar_permiso_a_rol(permiso5, rol)
    agregar_permiso_a_rol(permiso6, rol)
    agregar_permiso_a_rol(permiso7, rol)
    agregar_permiso_a_rol(permiso_show, rol)
    agregar_permiso_a_rol(permiso_update, rol)
    agregar_rol_a_usuario(rol="superadmin", institucion="", user="admin@gmail.com")

    # crear_usuario_simple(email="superadmin@gmail.com", nombre="super", apellido="admin")
    # completar_usuario("superadmin@gmail.com", "superadmin", "admin")
    # rol_sadmin = Rol(nombre="superadmin")
    # permiso_show = Permiso(nombre="configuracion_show")
    # permiso_update = Permiso(nombre="configuracion_update")
    # agregar_permiso_a_rol(permiso_show, rol_sadmin)
    # agregar_permiso_a_rol(permiso_update, rol_sadmin)
    # agregar_rol_a_usuario(rol_sadmin, "superadmin@gmail.com")

    crear_usuario_simple(
        email="dueño@gmail.com",
        nombre="dueño",
        apellido="dueño",
    )
    completar_usuario("dueño@gmail.com", "dueño", "dueño")
    permiso1 = Permiso(nombre="userinst_index")
    permiso2 = Permiso(nombre="userinst_create")
    permiso3 = Permiso(nombre="userinst_update")
    permiso4 = Permiso(nombre="userinst_destroy")
    rol = Rol(nombre="dueño")
    db.session.add(rol)
    db.session.commit()
    agregar_permiso_a_rol(permiso1, rol)
    agregar_permiso_a_rol(permiso2, rol)
    agregar_permiso_a_rol(permiso3, rol)
    agregar_permiso_a_rol(permiso4, rol)
    agregar_rol_a_usuario(rol="dueño", institucion="a", user="dueño@gmail.com")

    crear_usuario_simple(
        email="user@gmail.com",
        nombre="user",
        apellido="user",
    )
    completar_usuario("user@gmail.com", "user", "user")

    crear_usuario_simple(
        email="user2@gmail.com",
        nombre="user2",
        apellido="user2",
    )
    completar_usuario("user2@gmail.com", "user2", "user2")

    rol = Rol(nombre="operador")
    db.session.add(rol)
    db.session.commit()
    rol = Rol(nombre="administrador")
    db.session.add(rol)
    db.session.commit()

    # TODO Hardcodeado para testeos,borrar
    agregar_institucion_a_usuario(2, 1)
    agregar_institucion_a_usuario(2, 2)
    db.session.commit()
