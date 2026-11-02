
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError

# Pruebas exclusivas del laboratorio local
URL = "http://127.0.0.1:5000/"

pruebas = [
    ("Credenciales incorrectas", "admin", "incorrecta"),
    ("SQL Injection", "admin' -- ", "incorrecta")
]

print("=== PRUEBAS SQL INJECTION - GRUPO 15 ===")

for nombre, usuario, contrasena in pruebas:
    datos = urlencode({
        "usuario": usuario,
        "contrasena": contrasena
    }).encode("utf-8")

    peticion = Request(URL, data=datos, method="POST")

    try:
        with urlopen(peticion, timeout=5) as respuesta:
            pagina = respuesta.read().decode("utf-8")
            estado = respuesta.status

        acceso = "Acceso concedido:" in pagina

        print(f"\nPrueba: {nombre}")
        print(f"Estado HTTP: {estado}")
        print("Resultado:", "ACCESO CONCEDIDO" if acceso
              else "ACCESO DENEGADO")

    except URLError as error:
        print(f"\nError de conexion: {error}")

print("\n=== FIN DE LAS PRUEBAS ===")
