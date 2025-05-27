import gradio as gr
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
from vector_store import add_document, query_documents
import io

def ocr_file(file):
    # If file is None, return empty string
    if file is None:
        return ""
    # If file has a 'read' attribute, it's a file-like object
    if hasattr(file, "read"):
        if file.name.lower().endswith('.pdf'):
            file_bytes = file.read()
            pages = convert_from_bytes(file_bytes)
            text = "\n".join([pytesseract.image_to_string(page) for page in pages])
        else:
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
        add_document(getattr(file, "name", "uploaded_file"), text, metadata={"source": getattr(file, "name", "uploaded_file")})
        return text
    # If file is a string (path), open it
    elif isinstance(file, str):
        if file.lower().endswith('.pdf'):
            with open(file, "rb") as f:
                pages = convert_from_bytes(f.read())
            text = "\n".join([pytesseract.image_to_string(page) for page in pages])
        else:
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
        add_document(file, text, metadata={"source": file})
        return text
    else:
        return "Unsupported file type."

def semantic_search(query):
    results = query_documents(query)
    return str(results)

with gr.Blocks() as demo:
    gr.Markdown("# Document OCR & Semantic Search")
    with gr.Tab("Upload & OCR"):
        file_input = gr.File(label="Upload PDF or Image")
        ocr_output = gr.Textbox(label="OCR Result")
        file_input.change(ocr_file, inputs=file_input, outputs=ocr_output)
    with gr.Tab("Semantic Search"):
        query_input = gr.Textbox(label="Search Query")
        search_output = gr.Textbox(label="Search Results")
        query_input.change(semantic_search, inputs=query_input, outputs=search_output)

demo.launch(server_name="0.0.0.0", server_port=7860)
