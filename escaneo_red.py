
import socket
from datetime import datetime

# Escaneo autorizado del equipo local
HOST = "127.0.0.1"

# Puertos de las aplicaciones del laboratorio
PUERTOS = {
    5000: "Flask - Aplicacion vulnerable",
    5001: "Flask - Aplicacion protegida"
}

print("=" * 55)
print("ESCANEO BASICO DE RED - GRUPO 15")
print("UNEMI - SEGURIDAD INFORMATICA")
print("=" * 55)

print(f"\nEquipo analizado: {HOST}")
print(f"Fecha y hora: {datetime.now()}")
print("\nIniciando escaneo de puertos...\n")

puertos_abiertos = 0

for puerto, servicio in PUERTOS.items():

    with socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    ) as cliente:

        cliente.settimeout(2)

        resultado = cliente.connect_ex(
            (HOST, puerto)
        )

        if resultado == 0:
            estado = "ABIERTO"
            puertos_abiertos += 1
        else:
            estado = "NO DISPONIBLE"

        print(f"Puerto: {puerto}")
        print(f"Servicio esperado: {servicio}")
        print(f"Estado: {estado}")
        print("-" * 40)

print("\nRESUMEN DEL ESCANEO")
print(f"Puertos analizados: {len(PUERTOS)}")
print(f"Puertos abiertos: {puertos_abiertos}")
print(
    f"Puertos no disponibles: "
    f"{len(PUERTOS) - puertos_abiertos}"
)

print("\nEscaneo finalizado correctamente.")
