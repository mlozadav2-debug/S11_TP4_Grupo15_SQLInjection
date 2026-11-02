
import sqlite3
from pathlib import Path
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Base de datos del laboratorio
BASE_DATOS = Path(__file__).resolve().parent / "usuarios.db"

# Formulario web
HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login Seguro - Grupo 15 UNEMI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eaf0f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }

        .login {
            background: white;
            padding: 40px;
            width: 350px;
            border-radius: 15px;
            box-shadow: 0 5px 20px #0002;
            text-align: center;
        }

        h2 {
            color: #173b70;
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            box-sizing: border-box;
            border: 1px solid #bbb;
            border-radius: 6px;
        }

        button {
            background: #173b70;
            color: white;
            border: none;
            padding: 12px;
            width: 100%;
            border-radius: 6px;
            cursor: pointer;
        }

        button:hover {
            background: #24549a;
        }

        .mensaje {
            margin-top: 20px;
            font-weight: bold;
        }

        .seguridad {
            color: green;
            font-size: 13px;
            margin-top: 15px;
        }
    </style>
</head>

<body>
    <div class="login">

        <h2>UNEMI - Grupo 15</h2>
        <h3>Seguridad Informatica</h3>
        <p>Practica SQL Injection</p>

        <form method="POST">

            <input
                type="text"
                name="usuario"
                placeholder="Usuario"
                required
            >

            <input
                type="password"
                name="contrasena"
                placeholder="Contraseña"
                required
            >

            <button type="submit">
                Iniciar sesion
            </button>

        </form>

        {% if mensaje %}
        <p class="mensaje">{{ mensaje }}</p>
        {% endif %}

        <p class="seguridad">
            Version protegida contra SQL Injection
        </p>

    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def inicio():

    mensaje = ""

    if request.method == "POST":

        usuario = request.form.get("usuario", "")
        contrasena = request.form.get("contrasena", "")

        # CONSULTA SEGURA
        # Se utilizan parametros para evitar SQL Injection

        consulta = (
            "SELECT id, usuario FROM usuarios "
            "WHERE usuario = ? AND contrasena = ?"
        )

        try:

            with sqlite3.connect(BASE_DATOS) as conexion:

                resultado = conexion.execute(
                    consulta,
                    (usuario, contrasena)
                ).fetchone()

            if resultado:

                mensaje = (
                    f"Acceso concedido: {resultado[1]}"
                )

            else:

                mensaje = (
                    "Acceso denegado. Datos incorrectos."
                )

        except sqlite3.Error:

            mensaje = (
                "Error al ejecutar la consulta SQL."
            )

    return render_template_string(
        HTML,
        mensaje=mensaje
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False
    )
