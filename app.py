# Importar bibliotecas necesarias
from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from werkzeug.utils import secure_filename
import utils
app = Flask(__name__)
from utils import getMiniaturas
# Obtener la ruta absoluta del directorio padre de app.py
base_dir = os.path.abspath(os.path.dirname(__file__))
getMiniaturas()
# Configurar la carpeta para cargar archivos
app.config['UPLOAD_FOLDER'] = os.path.join(base_dir, 'uploads')

# Verificar si la carpeta 'uploads' existe, y si no, crearla
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de carga de archivos
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Verificar si se envió un archivo
        if 'file' not in request.files:
            return 'No se seleccionó ningún archivo.'
        
        file = request.files['file']

        # Verificar si se seleccionó un archivo
        if file.filename == '':
            return 'No se seleccionó ningún archivo.'

        # Asegurarse de que el nombre del archivo sea seguro
        filename = secure_filename(file.filename)

        # Guardar el archivo en la carpeta "uploads"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return 'Archivo cargado exitosamente.'

    return render_template('upload.html')

# Ruta para la página de descarga de archivos
@app.route('/download')
def download():
    # Obtener la lista de archivos en la carpeta "uploads"
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('download.html', files=files)

# Ruta para descargar archivos específicos
@app.route('/download/<filename>')
def download_file(filename):
    # Verificar si el archivo existe en la carpeta "uploads"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(file_path)
    if os.path.exists(file_path):
        # Descargar el archivo desde la carpeta "uploads"
        return send_file(file_path, as_attachment=True)
    else:
        return 'El archivo no existe.'

if __name__ == '__main__':
    # Iniciar la aplicación
    app.run()
