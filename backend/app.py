import gradio as gr
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
from app.api.router import upload_document, search_documents

def ocr_file(file):
    # Accepts PDF or image
    if file.name.lower().endswith('.pdf'):
        pages = convert_from_bytes(file.read())
        text = "\n".join([pytesseract.image_to_string(page) for page in pages])
    else:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
    return text

def upload_and_ocr(file):
    # Use your existing upload_document logic here
    # file is a file-like object
    class DummyUploadFile:
        def __init__(self, file):
            self.filename = file.name
            self.file = file
    result = upload_document(DummyUploadFile(file))
    return f"OCR Text File: {result['ocr_text_file']}"

def semantic_search(query):
    # Use your existing search_documents logic here
    result = search_documents(query)
    return result

with gr.Blocks() as demo:
    gr.Markdown("# Document OCR & Semantic Search")
    with gr.Tab("Upload & OCR"):
        file_input = gr.File(label="Upload PDF or Image")
        ocr_output = gr.Textbox(label="OCR Result")
        file_input.change(upload_and_ocr, inputs=file_input, outputs=ocr_output)
    with gr.Tab("Semantic Search"):
        query_input = gr.Textbox(label="Search Query")
        search_output = gr.Textbox(label="Search Results")
        query_input.change(semantic_search, inputs=query_input, outputs=search_output)

iface = gr.Interface(
    fn=ocr_file,
    inputs=gr.File(label="Upload PDF or Image"),
    outputs=gr.Textbox(label="Extracted Text"),
    title="Document OCR Demo",
    description="Upload a PDF or image to extract text using OCR."
)

if __name__ == "__main__":
    iface.launch()
