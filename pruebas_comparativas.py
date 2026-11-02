
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError

print("=== COMPARACION DE SEGURIDAD - GRUPO 15 ===")

aplicaciones = [
    ("Aplicacion vulnerable", 5000),
    ("Aplicacion protegida", 5001)
]

pruebas = [
    ("Acceso correcto", "admin", "ClaveDemo123"),
    ("Contrasena incorrecta", "admin", "incorrecta"),
    ("SQL Injection", "admin' -- ", "incorrecta")
]

for nombre_app, puerto in aplicaciones:

    print(f"\n--- {nombre_app} ---")

    for nombre, usuario, contrasena in pruebas:

        datos = urlencode({
            "usuario": usuario,
            "contrasena": contrasena
        }).encode("utf-8")

        url = f"http://127.0.0.1:{puerto}/"
        peticion = Request(url, data=datos, method="POST")

        try:
            with urlopen(peticion, timeout=5) as respuesta:
                pagina = respuesta.read().decode("utf-8")
                estado = respuesta.status

            acceso = "Acceso concedido:" in pagina

            print(f"\nPrueba: {nombre}")
            print(f"Estado HTTP: {estado}")
            print(
                "Resultado:",
                "ACCESO CONCEDIDO" if acceso
                else "ACCESO DENEGADO"
            )

        except URLError as error:
            print(f"\nError de conexion: {error}")

print("\n=== FIN DE LA COMPARACION ===")
