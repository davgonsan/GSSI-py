# Extractor e Importador de Datos

Este conjunto de programas en Python te permite extraer y procesar datos desde un archivo Excel, además de importar y organizar esos datos en formato JSON.

## Requisitos

- Python 3.x
- Librería openpyxl

```bash
pip install openpyxl
```

## Uso

### Extractor (extractor.py)

Este programa extrae datos específicos de un archivo Excel y los guarda en un archivo de texto (.txt).

1. Ejecutar `extractor.py`.
2. Introducir el nombre del archivo Excel y el nombre de la hoja.
3. Seleccionar las columnas deseadas.
4. Los datos se exportarán a un archivo `cargos.txt`.

### Importador (importador.py)

Este programa importa los datos del archivo `cargos.txt` y los organiza en un archivo JSON agrupado por compañía y cargo.

1. Ejecutar `importador.py`.
2. Los datos se agruparán y se exportarán a `cargos.json`.

## Manejo de Errores

- El Extractor maneja errores durante la extracción y los exporta a `errores_extractor/error_extractor_fecha.txt`.
- El Importador maneja errores durante la importación y los exporta a `errores_importador/error_importador_fecha.txt`.

## Estructura del Proyecto

```plaintext
.
└── **cargos_empleados**/
	├── exportador.exe
    ├── **__internal**/
    │   ├── _bz2.pyd
    │   ├── _decimal.pyd
    │   ├── _elementtree.pyd
    │   ├── _hashlib.pyd
    │   ├── _lzma.pyd
    │   ├── _socket.pyd
    │   ├── _ssl.pyd
    │   ├── base_library.zip
    │   ├── libcrypto-3.dll
    │   ├── libssl-3.dll
    │   ├── pyexpat.pyd
    │   ├── python312.dll
    │   ├── select.pyd
    │   ├── unicodedata.pyd
    │   └── VCRUNTlME140.d11
    ├── **datos_excel**/
    │   ├── cargos.txt
    │   └── REPORTE-DE-PERSONAL.xlsx
    ├── **errores_extractor**/
    │   └──  (Contiene los errores en formato txt)
    ├── **exportador**/
    │   ├── **_internal**/
    │   │   ├── _bz2.pyd
    │   │   ├── _ctypes.pyd
    │   │   ├── _decimal.pyd
    │   │   ├── _hashlib.pyd
    │   │   ├── _lzma.pyd
    │   │   ├── _multiprocessing.pyd
    │   │   ├── _queue.pyd
    │   │   ├── _socket.pyd
    │   │   ├── _ssl.pyd
    │   │   ├── _uuid.pyd
    │   │   ├── _wmi.pyd
    │   │   ├── base_library.zip
    │   │   ├── libcrypto-3.dll
    │   │   ├── libcrypto-3-x64.dll
    │   │   ├── libffi-8.dll
    │   │   ├── libmysql.dll
    │   │   ├── libssl-3.dll
    │   │   ├── libssl-3-x64.dll
    │   │   ├── MSVCP140.dll
    │   │   ├── pyexpat.pyd
    │   │   ├── python312.dll
    │   │   ├── select.pyd
    │   │   ├── unicodedata.pyd
    │   │   ├── VCRUNTlME140.dll
    │   │   └── VCRUNTlME140_1.dll
    └── 
```

## Notas

- Asegúrate de tener los permisos necesarios para leer y escribir archivos en las carpetas correspondientes.

```

Este README proporciona una guía básica de cómo usar los programas, describe los requisitos y la estructura del proyecto, y menciona el manejo de errores. Puedes personalizarlo según tus necesidades y detalles específicos del proyecto.
