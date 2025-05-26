from fastapi import APIRouter, UploadFile, File, Query
import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from app.services.vector_store import add_document, query_documents
import uuid

router = APIRouter()

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/upload-document")
def upload_document(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    extracted_text = ""
    if file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # OCR for images
        image = Image.open(file_location)
        extracted_text = pytesseract.image_to_string(image)
    elif file.filename.lower().endswith('.pdf'):
        # OCR for PDFs
        try:
            pages = convert_from_path(file_location)
            text_list = [pytesseract.image_to_string(page) for page in pages]
            extracted_text = "\n".join(text_list)
        except Exception as e:
            extracted_text = f"Error processing PDF: {str(e)}"
    else:
        extracted_text = "OCR not supported for this file type."

    # Save extracted text
    text_filename = file.filename + ".txt"
    text_path = os.path.join(UPLOAD_DIR, text_filename)
    with open(text_path, "w", encoding="utf-8") as tf:
        tf.write(extracted_text)

    # Store in vector DB
    doc_id = str(uuid.uuid4())
    add_document(doc_id, extracted_text, metadata={"filename": file.filename, "path": file_location})

    return {"filename": file.filename, "saved_to": file_location, "ocr_text_file": text_path, "vector_id": doc_id}

@router.get("/search")
def search_documents(query: str = Query(..., description="Search query"), n_results: int = 3):
    results = query_documents(query, n_results)
    return results 