from flask import Flask, request, send_file, jsonify, render_template_string
from rembg import remove
from io import BytesIO
from PIL import Image
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return render_template_string("""
        <h2>Welcome to the Background Remover API</h2>
        <p>Use <code>POST /api/remove-bg</code> with form-data to remove image backgrounds.</p>
    """)

@app.route("/api/remove-bg", methods=["POST"])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided."}), 400

    input_file = request.files['image']
    try:
        img = Image.open(input_file.stream).convert("RGBA")
        output = remove(img)

        buf = BytesIO()
        output.save(buf, format="PNG")
        buf.seek(0)

        return send_file(buf, mimetype="image/png")

    except Exception as e:
        app.logger.error(f"Error processing image: {e}")
        return jsonify({"error": "Failed to process image."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
