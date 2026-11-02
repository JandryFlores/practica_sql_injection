import sqlite3
import os
from werkzeug.security import generate_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_DIR = os.path.join(BASE_DIR, "database")
DATABASE_PATH = os.path.join(DATABASE_DIR, "seguridad.db")


def conectar():
    os.makedirs(DATABASE_DIR, exist_ok=True)

    conexion = sqlite3.connect(DATABASE_PATH)
    conexion.row_factory = sqlite3.Row

    return conexion


def inicializar_bd():

    conexion = conectar()
    cursor = conexion.cursor()

    # Tabla de usuarios para el laboratorio vulnerable
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios_vulnerables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            password TEXT NOT NULL,
            rol TEXT NOT NULL
        )
    """)

    # Tabla de usuarios para el laboratorio protegido
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios_seguros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            rol TEXT NOT NULL
        )
    """)

    # Datos ficticios
    usuarios = [
        ("admin", "admin123", "Administrador"),
        ("estudiante", "estudiante123", "Estudiante"),
        ("invitado", "invitado123", "Invitado")
    ]

    for usuario, password, rol in usuarios:

        cursor.execute("""
            SELECT id FROM usuarios_vulnerables
            WHERE usuario = ?
        """, (usuario,))

        if cursor.fetchone() is None:

            cursor.execute("""
                INSERT INTO usuarios_vulnerables
                (usuario, password, rol)
                VALUES (?, ?, ?)
            """, (usuario, password, rol))

        cursor.execute("""
            SELECT id FROM usuarios_seguros
            WHERE usuario = ?
        """, (usuario,))

        if cursor.fetchone() is None:

            cursor.execute("""
                INSERT INTO usuarios_seguros
                (usuario, password_hash, rol)
                VALUES (?, ?, ?)
            """, (
                usuario,
                generate_password_hash(password),
                rol
            ))

    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    inicializar_bd()
    print("Base de datos creada correctamente.")