
# SQL Injection - Grupo 15

## Universidad Estatal de Milagro - UNEMI

**Asignatura:** Seguridad Informática  
**Unidad:** 4 - Seguridad en redes y bases de datos  
**Semana:** 11  
**Práctica:** N.º 4  
**Año:** 2026

## 1. Descripción

Este proyecto desarrolla un laboratorio controlado para
identificar, demostrar y mitigar una vulnerabilidad de
inyección SQL (SQL Injection) en una aplicación web.

Se utiliza Python, Flask y SQLite para comparar el
comportamiento de una aplicación vulnerable y una
versión protegida mediante consultas parametrizadas.

Todas las pruebas se realizan localmente con usuarios
ficticios y fines exclusivamente académicos.

## 2. Objetivo

Demostrar los riesgos de construir consultas SQL
mediante concatenación de entradas del usuario y
evaluar la eficacia de las consultas parametrizadas
como mecanismo de prevención.

## 3. Herramientas utilizadas

- Python 3.14.4
- Flask 3.1.3
- SQLite
- Visual Studio Code
- Git y GitHub
- macOS
- Google Chrome

## 4. Archivos del proyecto

- app_vulnerable.py: aplicación vulnerable.
- app_segura.py: aplicación con consultas parametrizadas.
- crear_bd.py: creación de la base SQLite.
- ataque_sql_i.py: simulación automatizada de SQL Injection.
- pruebas_comparativas.py: comparación de ambas aplicaciones.
- escaneo_red.py: análisis básico de puertos locales.
- seguridad_bd.py: comprobaciones de seguridad de SQLite.
- README.md: descripción general del proyecto.
- MANUAL_USO.md: instrucciones de instalación y pruebas.

## 5. Instalación

Crear y activar el entorno virtual:

    python3 -m venv .venv
    source .venv/bin/activate

Instalar Flask:

    python -m pip install flask

Crear la base de datos:

    python crear_bd.py

## 6. Ejecución

Aplicación vulnerable:

    python app_vulnerable.py

Dirección: http://127.0.0.1:5000

Aplicación protegida:

    python app_segura.py

Dirección: http://127.0.0.1:5001

## 7. Pruebas experimentales

Ejecutar:

    python ataque_sql_i.py
    python pruebas_comparativas.py

Resultados observados:

| Prueba | Vulnerable | Protegida |
|---|---|---|
| Credenciales válidas | Concedido | Concedido |
| Contraseña incorrecta | Denegado | Denegado |
| SQL Injection | Concedido | Denegado |

La versión vulnerable permitió evadir la autenticación.
La versión protegida rechazó el mismo intento.

## 8. Escaneo de red

Ejecutar:

    python escaneo_red.py

Se comprobaron los puertos 5000 y 5001 en 127.0.0.1.
Ambos respondieron como puertos TCP abiertos durante
la práctica.

## 9. Seguridad de bases de datos

Ejecutar:

    python seguridad_bd.py

Se verificaron los permisos del archivo, la integridad
de SQLite y la configuración de claves foráneas en la
conexión de auditoría.

## 10. Consideraciones éticas

El proyecto está diseñado únicamente para un
laboratorio local y autorizado.

La aplicación vulnerable no debe publicarse como
servicio accesible desde Internet.

Los usuarios y contraseñas son ficticios.
No se deben utilizar datos personales reales.

## 11. Conclusión

Las pruebas permitieron demostrar cómo una consulta
SQL insegura puede comprometer la autenticación de
una aplicación web.

Las consultas parametrizadas impidieron el bypass
demostrado en el laboratorio.

El desarrollo evidencia la importancia de aplicar
prácticas de programación segura y realizar pruebas
controladas antes de implementar sistemas reales.
