from fastapi import FastAPI, UploadFile, File
from app.pdf_handler import extract_text_from_pdf, create_pdf_from_text
from app.nsfw_detector import is_text_nsfw
from app.nsfw_rewriter import rewrite_text
import uuid
import os

app = FastAPI()

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Welcome to the NSFW PDF Filter API"}

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_bytes = await file.read()

    input_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.pdf")
    with open(input_path, "wb") as f:
        f.write(file_bytes)

    text = extract_text_from_pdf(file_bytes)

    if is_text_nsfw(text):
        rewritten = rewrite_text(text)
        output_path = os.path.join(OUTPUT_FOLDER, f"{uuid.uuid4()}_rewritten.pdf")
        create_pdf_from_text(rewritten, output_path)
        return {
            "status": "NSFW Detected",
            "rewritten_pdf_path": output_path
        }
    else:
        output_path = os.path.join(OUTPUT_FOLDER, f"{uuid.uuid4()}_clean.pdf")
        create_pdf_from_text(text, output_path)
        return {
            "status": "Clean",
            "output_pdf_path": output_path
        }
