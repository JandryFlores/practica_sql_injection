import requests

URL_VULNERABLE = "http://127.0.0.1:5000/login-vulnerable"
URL_SEGURA = "http://127.0.0.1:5000/login-seguro"


def probar_sql_injection():

    print("=" * 55)
    print(" SIMULACIÓN CONTROLADA DE SQL INJECTION")
    print("=" * 55)

    # Entrada de prueba para el laboratorio local
    datos = {
        "usuario": "' OR '1'='1' -- ",
        "password": "prueba_incorrecta"
    }

    print("\n[1] Probando el login vulnerable...")

    try:

        respuesta = requests.post(
            URL_VULNERABLE,
            data=datos,
            allow_redirects=True,
            timeout=5
        )

        if "/dashboard" in respuesta.url:

            print("[!] VULNERABILIDAD CONFIRMADA")
            print("El login vulnerable aceptó la entrada de prueba.")

        else:

            print("[+] No se consiguió acceder al panel.")

        print("\n[2] Probando el login protegido...")

        respuesta_segura = requests.post(
            URL_SEGURA,
            data=datos,
            allow_redirects=True,
            timeout=5
        )

        if "/dashboard" in respuesta_segura.url:

            print("[!] Revisar: el login protegido permitió el acceso.")

        else:

            print("[+] MITIGACIÓN CORRECTA")
            print("El login seguro rechazó la entrada manipulada.")

    except requests.exceptions.ConnectionError:

        print("[ERROR] No se encuentra el servidor Flask.")
        print("Primero ejecuta: python app.py")

    except requests.exceptions.Timeout:

        print("[ERROR] Tiempo de espera agotado.")

    print("\nPrueba finalizada.")


if __name__ == "__main__":

    probar_sql_injection()