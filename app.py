from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
import io
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Rembg server is running!'

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render uses PORT environment variable
    app.run(host="0.0.0.0", port=port)    return 'Rembg server is running!'
