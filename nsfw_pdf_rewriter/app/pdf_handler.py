import fitz  # PyMuPDF
from io import BytesIO

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    doc = fitz.open("pdf", pdf_bytes)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def create_pdf_from_text(text: str, output_path: str):
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text, fontsize=12)
    doc.save(output_path)
