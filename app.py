from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    input_file = request.files['file']
    input_bytes = input_file.read()
    output = remove(input_bytes)

    return send_file(
        io.BytesIO(output),
        mimetype='image/png',
        as_attachment=False,
        download_name='no-bg.png'
    )

@app.route('/')
def home():
    return 'Rembg server is running!'
