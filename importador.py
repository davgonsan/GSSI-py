import json
import os
from datetime import datetime

try:
    # Leer datos desde el archivo txt
    carpeta_datos = "datos_excel"
    archivo_txt = os.path.join(carpeta_datos, 'cargos.txt')
    with open(archivo_txt, 'r') as archivo:
        lineas = archivo.readlines()

    # Crear un diccionario para almacenar los datos agrupados
    datos_agrupados = {}

    # Procesar cada línea en el archivo txt
    for linea in lineas:
        valores = linea.strip().split('\t')
        compania, cedula, apellidos, nombres, cargo = valores

        # Si la compañía no existe en el diccionario, crear una entrada
        if compania not in datos_agrupados:
            datos_agrupados[compania] = {}

        # Si el cargo no existe para la compañía, crear una entrada
        if cargo not in datos_agrupados[compania]:
            datos_agrupados[compania][cargo] = []

        # Agregar los datos del empleado
        datos_agrupados[compania][cargo].append(
            {"CEDULA": cedula, "APELLIDOS": apellidos, "NOMBRES": nombres})

    # Exportar a formato JSON
    archivo_json_agrupado = os.path.join(carpeta_datos, 'cargos.json')
    with open(archivo_json_agrupado, 'w', encoding='utf-8') as archivo_json:
        json.dump(datos_agrupados, archivo_json, indent=2, ensure_ascii=False)

    print(f"Datos agrupados exportados correctamente a '{archivo_json_agrupado}'.")

except Exception as e:
    # Manejar errores
    carpeta_errores = "errores_importador"
    os.makedirs(carpeta_errores, exist_ok=True)

    # Crear nombre de archivo basado en la fecha y hora
    fecha_error = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_error = os.path.join(carpeta_errores, f'error_importador_{fecha_error}.txt')

    # Exportar información del error al archivo
    with open(archivo_error, 'w') as archivo_err:
        archivo_err.write(f"Error en el importador:\n{str(e)}")

    print(f"Se ha producido un error. Detalles del error exportados a '{archivo_error}'.")
