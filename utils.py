# Aquí puedes agregar funciones y utilidades para el manejo de archivos.
# Por ejemplo, funciones para subir y descargar archivos, verificar el espacio disponible, etc.
# Importar bibliotecas necesarias
import os

# Función para verificar si un archivo ya existe en el servidor
def archivo_existe(nombre_archivo):
    return os.path.exists(nombre_archivo)

# Función para obtener el tamaño del archivo en bytes
def obtener_tamano_archivo(nombre_archivo):
    try:
        return os.path.getsize(nombre_archivo)
    except OSError:
        return -1

# Función para calcular el espacio disponible en el servidor
def espacio_disponible():
    total_bytes = os.statvfs("/")[0] * os.statvfs("/")[2]
    usado_bytes = os.statvfs("/")[0] * (os.statvfs("/")[2] - os.statvfs("/")[3])
    disponible_bytes = total_bytes - usado_bytes
    return disponible_bytes

def getMiniaturas():
    from PIL import Image

    # Ruta de la imagen original
    ruta_original = "Proyecto_de_Servicios_de_Archivos/static/imgIcon.png"

    # Verificar si el directorio "min_img" existe, y si no, crearlo
    ruta_min_img = "Proyecto_de_Servicios_de_Archivos/static/min_img"
    if not os.path.exists(ruta_min_img):
        os.makedirs(ruta_min_img)

    # Abrir la imagen
    imagen_original = Image.open(ruta_original)

    # Generar una miniatura de 100x100 píxeles
    miniatura = imagen_original.resize((100, 100))

    # Guardar la miniatura en el directorio "min_img"
    ruta_miniatura = "Proyecto_de_Servicios_de_Archivos/static/min_img/imgIcon.png"
    miniatura.save(ruta_miniatura)


