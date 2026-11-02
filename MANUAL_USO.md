
# MANUAL DE USO Y PRUEBAS
## Simulación y mitigación de SQL Injection

**Universidad:** Universidad Estatal de Milagro - UNEMI  
**Asignatura:** Seguridad Informática  
**Semana:** 11  
**Práctica:** N.º 4  
**Grupo:** 15  
**Año:** 2026  

---

## 1. Introducción

Este manual describe los procedimientos utilizados
para instalar, ejecutar y comprobar el funcionamiento
del laboratorio de SQL Injection desarrollado con
Python, Flask y SQLite.

El proyecto incluye una aplicación vulnerable y una
versión protegida, con el propósito de comparar sus
respuestas frente a intentos de autenticación legítimos
y entradas SQL manipuladas.

Todas las pruebas están limitadas al equipo local
y emplean datos ficticios.

## 2. Requisitos del sistema

Para desarrollar esta práctica se utilizaron:

- Computadora con macOS.
- Python 3.14.4.
- Flask 3.1.3.
- SQLite, mediante la biblioteca sqlite3 de Python.
- Visual Studio Code.
- Google Chrome.
- Terminal integrada de VS Code.

## 3. Preparación del entorno

Abrir Visual Studio Code y seleccionar la carpeta
SQLInjection_Grupo15.

Desde la terminal, comprobar Python:

    python3 --version

Crear el entorno virtual:

    python3 -m venv .venv

Activar el entorno virtual en macOS:

    source .venv/bin/activate

Instalar Flask:

    python -m pip install flask

Verificar la instalación:

    python -m flask --version

La instalación se considera satisfactoria cuando
Flask muestra su versión sin errores.

## 4. Creación de la base de datos

Ejecutar:

    python crear_bd.py

Este procedimiento crea el archivo usuarios.db
y la tabla usuarios.

Se registran dos usuarios ficticios:

- admin
- estudiante

La base de datos se utiliza exclusivamente para
realizar las pruebas académicas.

Las contraseñas de demostración se almacenan en
texto plano para facilitar la comparación del
laboratorio; esta práctica no debe utilizarse
en un sistema real.

## 5. Ejecución de la aplicación vulnerable

En una terminal con el entorno virtual activado:

    python app_vulnerable.py

Abrir en el navegador:

http://127.0.0.1:5000

El sistema muestra un formulario con los campos
de usuario y contraseña.

Esta versión construye una consulta SQL mediante
concatenación directa de entradas.

Por ese motivo, es vulnerable a SQL Injection.

## 6. Pruebas de autenticación

### 6.1. Credenciales correctas

Usuario: admin

Contraseña: ClaveDemo123

Resultado observado:

Acceso concedido: admin

### 6.2. Credenciales incorrectas

Usuario: admin

Contraseña: incorrecta

Resultado observado:

Acceso denegado. Datos incorrectos.

### 6.3. Simulación de SQL Injection

En la aplicación vulnerable se introdujo el
siguiente valor en el campo de usuario:

    admin' -- 

Contraseña:

    incorrecta

Resultado observado:

Acceso concedido: admin

La entrada manipulada modifica el significado
de la consulta SQL y permite omitir la
comprobación de la contraseña.

Esta prueba demuestra un bypass de autenticación
en la aplicación del laboratorio.

## 7. Ejecución del script de pruebas

Mantener funcionando la aplicación vulnerable.

Abrir otra terminal y ejecutar:

    python ataque_sql_i.py

Se realizan dos comprobaciones:

1. Autenticación con una contraseña incorrecta.
2. Autenticación mediante una entrada SQL manipulada.

Resultados observados:

- Contraseña incorrecta: ACCESO DENEGADO.
- SQL Injection: ACCESO CONCEDIDO.

## 8. Ejecución de la aplicación protegida

En otra terminal, ejecutar:

    python app_segura.py

Abrir:

http://127.0.0.1:5001

Esta versión utiliza consultas SQL parametrizadas.

Los datos de entrada se envían como parámetros
y no se interpretan como instrucciones SQL.

## 9. Verificación de la mitigación

Repetir el intento de SQL Injection utilizado
anteriormente.

Usuario:

    admin' -- 

Contraseña:

    incorrecta

Resultado observado:

Acceso denegado. Datos incorrectos.

Esto demuestra que las consultas parametrizadas
impiden el bypass utilizado en la prueba.

## 10. Comparación experimental

Mantener ambas aplicaciones ejecutándose:

- Aplicación vulnerable: puerto 5000.
- Aplicación protegida: puerto 5001.

En una tercera terminal, ejecutar:

    python pruebas_comparativas.py

Resultados:

| Prueba | Vulnerable | Protegida |
|---|---|---|
| Acceso correcto | Concedido | Concedido |
| Contraseña incorrecta | Denegado | Denegado |
| SQL Injection | Concedido | Denegado |

La comparación permite comprobar la efectividad
de las consultas parametrizadas frente al ataque
simulado.

El estado HTTP 200 indica que la petición fue
procesada; no significa necesariamente que
la autenticación haya sido concedida.

## 11. Escaneo básico de red

Ejecutar:

    python escaneo_red.py

Se analiza exclusivamente la dirección local:

    127.0.0.1

Puertos comprobados:

- 5000: aplicación vulnerable.
- 5001: aplicación protegida.

Resultados registrados:

- Puertos analizados: 2.
- Puertos abiertos: 2.
- Puertos no disponibles: 0.

La comprobación permite identificar puertos
TCP que aceptan conexiones.

## 12. Seguridad de la base de datos

Ejecutar:

    python seguridad_bd.py

El módulo realiza las siguientes verificaciones:

1. Restricción de permisos de usuarios.db.
2. Comprobación de integridad mediante SQLite.
3. Activación de claves foráneas en la conexión.
4. Conteo de usuarios sin mostrar contraseñas.
5. Presentación de recomendaciones de seguridad.

Resultados registrados:

- Permisos: 0o600.
- Integridad: ok.
- Claves foráneas: True.
- Usuarios registrados: 2.

Estas comprobaciones no sustituyen otras medidas
de seguridad necesarias en producción.

## 13. Recomendaciones de seguridad

- Aplicar consultas parametrizadas.
- Validar adecuadamente las entradas del usuario.
- Almacenar hashes seguros de contraseñas.
- Restringir los permisos de acceso.
- Mantener respaldos protegidos.
- Evitar publicar información sensible.
- Actualizar las dependencias del sistema.
- Realizar pruebas únicamente con autorización.

## 14. Evidencias experimentales

Las capturas de la práctica se incorporarán
al informe técnico final en formato PDF.

Incluyen:

- Instalación y configuración de Flask.
- Aplicación web funcionando.
- Creación de la base de datos.
- Autenticación correcta e incorrecta.
- Simulación del ataque SQL Injection.
- Ejecución del script de ataque.
- Aplicación protegida.
- Validación de la mitigación.
- Resultados comparativos.
- Escaneo básico de red.
- Auditoría de seguridad de SQLite.

## 15. Conclusión

La práctica permitió identificar una vulnerabilidad
SQL Injection en una aplicación web desarrollada
con Python y Flask.

Las pruebas demostraron que una consulta construida
mediante concatenación puede alterar el proceso
de autenticación.

Posteriormente, se implementaron consultas
parametrizadas y se comprobó que el mismo intento
de inyección fue rechazado.

El proyecto destaca la importancia de desarrollar
aplicaciones seguras, proteger las bases de datos
y ejecutar pruebas controladas de ciberseguridad.

---

**Nota:** Este proyecto se utiliza exclusivamente
con fines educativos en un entorno local autorizado.
