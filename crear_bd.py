
import sqlite3

# Crear o abrir la base de datos local
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Crear tabla de usuarios de prueba
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL
)
""")

# Agregar usuarios ficticios del laboratorio
usuarios = [
    ("admin", "ClaveDemo123"),
    ("estudiante", "Practica2026")
]

cursor.executemany("""
INSERT OR IGNORE INTO usuarios (usuario, contrasena)
VALUES (?, ?)
""", usuarios)

conexion.commit()

# Comprobar los registros creados
cursor.execute("SELECT id, usuario FROM usuarios")
registros = cursor.fetchall()

print("Base de datos creada correctamente.")
print("Usuarios registrados:")

for registro in registros:
    print(registro)

conexion.close()
