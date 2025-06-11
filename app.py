# backend/app.py
from flask import Flask, request, send_file, jsonify
from rembg import remove
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route("/api/remove-bg", methods=["POST"])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided."}), 400
    
    input_file = request.files['image']
    img = Image.open(input_file.stream).convert("RGBA")
    output = remove(img)
    
    buf = BytesIO()
    output.save(buf, format="PNG")
    buf.seek(0)
    
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
    
