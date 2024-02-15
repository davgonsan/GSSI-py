import json
import mysql.connector
import os
import traceback
from datetime import datetime

try:
    # Datos de conexión a la base de datos
    host = "192.168.2.31"
    usuario = "prueba"
    contrasena = "sansimon"
    base_datos = "glpisansimon"

    # Obtener la ruta del script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Crear la conexión a la base de datos
    conexion = mysql.connector.connect(
        host=host,
        user=usuario,
        password=contrasena,
        database=base_datos
    )
    cursor = conexion.cursor()

    # Leer datos desde el archivo txt
    carpeta_datos = os.path.join(script_dir, "..", "datos_excel")  # Move one directory above
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
except Exception as e:
    # Capturar cualquier excepción y exportar el mensaje de error
    mensaje_error = f"Error: {str(e)}\n"
    mensaje_error += traceback.format_exc()

    carpeta_errores = "errores_query"
    os.makedirs(carpeta_errores, exist_ok=True)
    
    fecha_error = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archivo_error = f'errores_query_{fecha_error}.txt'

    with open(os.path.join(carpeta_errores, archivo_error), 'w') as archivo_err:
        archivo_err.write(mensaje_error)

    print(f"Se ha producido un error. Detalles en '{carpeta_errores}/{archivo_error}'.")
