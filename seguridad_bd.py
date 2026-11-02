
import os
import sqlite3
import stat
from pathlib import Path

# Base de datos del laboratorio
BASE_DATOS = Path(__file__).resolve().parent / "usuarios.db"

print("=" * 55)
print("SEGURIDAD DE BASES DE DATOS - GRUPO 15")
print("UNEMI - SEGURIDAD INFORMATICA")
print("=" * 55)

if not BASE_DATOS.exists():
    print("ERROR: No se encontro usuarios.db")
    raise SystemExit(1)

# 1. Restringir permisos del archivo en macOS
os.chmod(BASE_DATOS, stat.S_IRUSR | stat.S_IWUSR)

permisos = stat.S_IMODE(BASE_DATOS.stat().st_mode)

print("\n1. CONTROL DE ACCESO")
print(f"Permisos del archivo: {oct(permisos)}")
print("Acceso permitido al propietario del archivo.")

# 2. Verificar integridad y configuracion
conexion = sqlite3.connect(BASE_DATOS)

try:
    conexion.execute("PRAGMA foreign_keys = ON")

    integridad = conexion.execute(
        "PRAGMA integrity_check"
    ).fetchone()[0]

    claves_foraneas = conexion.execute(
        "PRAGMA foreign_keys"
    ).fetchone()[0]

    total_usuarios = conexion.execute(
        "SELECT COUNT(*) FROM usuarios"
    ).fetchone()[0]

    print("\n2. VERIFICACION DE INTEGRIDAD")
    print(f"Integridad de SQLite: {integridad}")

    print("\n3. CLAVES FORANEAS")
    print(f"Verificacion activada: {bool(claves_foraneas)}")

    print("\n4. PROTECCION DE DATOS")
    print(f"Usuarios registrados: {total_usuarios}")
    print("No se muestran contrasenas.")

    print("\n5. RECOMENDACIONES")
    print("- Utilizar consultas parametrizadas.")
    print("- Almacenar hashes seguros de contrasenas.")
    print("- Mantener copias de seguridad protegidas.")
    print("- Restringir el acceso a la base de datos.")
    print("- Evitar publicar datos reales en GitHub.")

    print("\nAUDITORIA FINALIZADA CORRECTAMENTE")

finally:
    conexion.close()
