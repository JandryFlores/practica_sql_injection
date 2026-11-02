import requests

URL = "http://127.0.0.1:5000/login-seguro"


def probar_credenciales():

    print("=" * 50)
    print(" PRUEBAS DEL SISTEMA DE MITIGACIÓN")
    print("=" * 50)

    pruebas = [

        {
            "nombre": "Credenciales correctas",
            "datos": {
                "usuario": "admin",
                "password": "admin123"
            },
            "esperado": True
        },

        {
            "nombre": "Contraseña incorrecta",
            "datos": {
                "usuario": "admin",
                "password": "incorrecta"
            },
            "esperado": False
        },

        {
            "nombre": "Usuario inexistente",
            "datos": {
                "usuario": "desconocido",
                "password": "123456"
            },
            "esperado": False
        },

        {
            "nombre": "Entrada SQL manipulada",
            "datos": {
                "usuario": "' OR '1'='1' -- ",
                "password": "incorrecta"
            },
            "esperado": False
        }

    ]

    try:

        for prueba in pruebas:

            respuesta = requests.post(
                URL,
                data=prueba["datos"],
                allow_redirects=True,
                timeout=5
            )

            acceso = "/dashboard" in respuesta.url

            if acceso == prueba["esperado"]:

                print(
                    "[CORRECTO] " +
                    prueba["nombre"]
                )

            else:

                print(
                    "[ERROR] " +
                    prueba["nombre"]
                )

    except requests.exceptions.ConnectionError:

        print("Primero debes iniciar el servidor Flask.")

    print("\nPruebas finalizadas.")


if __name__ == "__main__":

    probar_credenciales()