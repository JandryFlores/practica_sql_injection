import socket

# Se revisan únicamente puertos de la computadora local.
HOST = "127.0.0.1"

PUERTOS = {
    80: "HTTP",
    443: "HTTPS",
    5000: "Flask",
    3306: "MySQL",
    5432: "PostgreSQL",
    8000: "Servidor de desarrollo",
    8080: "Servidor web alternativo"
}


def escanear_puertos():

    resultados = []

    for puerto, servicio in PUERTOS.items():

        conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexion.settimeout(1)

        estado = conexion.connect_ex((HOST, puerto))

        if estado == 0:
            estado_texto = "Abierto"
        else:
            estado_texto = "Cerrado"

        resultados.append({
            "puerto": puerto,
            "servicio": servicio,
            "estado": estado_texto
        })

        conexion.close()

    return resultados