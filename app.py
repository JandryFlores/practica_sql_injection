#Librerías utilizadas
from scripts.escaneo_red import escanear_puertos

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import sqlite3
import os
from database import conectar, inicializar_bd
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.secret_key = "clave-laboratorio-local-cambiar"

# Inicializar la base de datos
inicializar_bd()

# PÁGINA PRINCIPAL
@app.route("/")
def index():
    return render_template("index.html")

# LOGIN VULNERABLE: con consulta insegura
@app.route("/login-vulnerable", methods=["GET", "POST"])
def login_vulnerable():

    if request.method == "POST":

        usuario = request.form["usuario"]
        password = request.form["password"]

        conexion = conectar()
        cursor = conexion.cursor()

        consulta = (
            "SELECT * FROM usuarios_vulnerables "
            "WHERE usuario = '" + usuario +
            "' AND password = '" + password + "'"
        )

        try:

            cursor.execute(consulta)
            resultado = cursor.fetchone()

            if resultado:

                session["usuario"] = resultado["usuario"]
                session["rol"] = resultado["rol"]
                session["modo"] = "Vulnerable"

                conexion.close()

                return redirect(url_for("dashboard"))

            flash("Credenciales incorrectas.", "danger")

        except sqlite3.Error:

            flash("Error en la consulta SQL.", "danger")

        conexion.close()

    return render_template(
        "login.html",
        modo="vulnerable"
    )

# LOGIN SEGURO: con consulta parametrizada
@app.route("/login-seguro", methods=["GET", "POST"])
def login_seguro():

    if request.method == "POST":

        usuario = request.form["usuario"]
        password = request.form["password"]

        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                SELECT * FROM usuarios_seguros
                WHERE usuario = ?
            """, (usuario,))

            resultado = cursor.fetchone()

            if (
                resultado and
                check_password_hash(
                    resultado["password_hash"],
                    password
                )
            ):

                session["usuario"] = resultado["usuario"]
                session["rol"] = resultado["rol"]
                session["modo"] = "Seguro"

                conexion.close()

                return redirect(url_for("dashboard"))

            flash("Credenciales incorrectas.", "danger")

        except sqlite3.Error:

            flash("Error al consultar la base de datos.", "danger")

        finally:
            conexion.close()

    return render_template(
        "login.html",
        modo="seguro"
    )


# PANEL PRINCIPAL
@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect(url_for("index"))

    return render_template(
        "dashboard.html",
        usuario=session["usuario"],
        rol=session["rol"],
        modo=session["modo"]
    )

# MÓDULO DE SEGURIDAD
@app.route("/seguridad")
def seguridad():

    return render_template("seguridad.html")

# MÓDULO DE ESCANEO
@app.route("/escaneo", methods=["GET", "POST"])
def escaneo():

    resultados = []

    if request.method == "POST":
        resultados = escanear_puertos()

    return render_template(
        "escaneo.html",
        resultados=resultados
    )

# EJECUCIÓN
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )