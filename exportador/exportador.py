import json
import mysql.connector
import os
from datetime import datetime

# Datos de conexión a la base de datos
host = "192.168.2.31"
usuario = "prueba"
contrasena = "sansimon"
base_datos = "glpisansimon"

# Crear la conexión a la base de datos
conexion = mysql.connector.connect(
    host=host,
    user=usuario,
    password=contrasena,
    database=base_datos
)
cursor = conexion.cursor()

# Leer datos desde el archivo txt
carpeta_datos = "datos_excel"
archivo_txt = os.path.join(carpeta_datos, 'cargos.txt')

with open(archivo_txt, 'r') as archivo:
    lineas = archivo.readlines()

# Procesar cada línea en el archivo txt
for linea in lineas:
    valores = linea.strip().split('\t')
    compania, cedula, apellidos, nombres, cargo = valores

    # Sentencia SQL de inserción
    sql_insert = "INSERT INTO tabla_temp_cargos_empleados (COMPANIA, CEDULA, APELLIDOS, NOMBRES, CARGO) VALUES (%s, %s, %s, %s, %s)"

    # Datos para la inserción
    datos_insert = (compania, cedula, apellidos, nombres, cargo)

    # Ejecutar la sentencia SQL
    cursor.execute(sql_insert, datos_insert)

# Confirmar la inserción y cerrar la conexión
conexion.commit()
conexion.close()

print(f"Datos insertados correctamente en la base de datos.")
