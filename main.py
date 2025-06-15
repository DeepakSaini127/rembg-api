from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, HTMLResponse
from rembg import remove
import io

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <h2>Welcome to Background Remover API</h2>
    <p>Use POST /remove-bg/ to upload an image and remove the background.</p>
    """

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)
    return StreamingResponse(io.BytesIO(output_image), media_type="image/png")
