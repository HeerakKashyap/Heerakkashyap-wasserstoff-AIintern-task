# Chatbot Theme Identifier 

---

## 🛠️ Features

- **Document Upload:** Upload PDFs or images for processing.
- **OCR:** Extracts text using Tesseract OCR and pdf2image.
- **Semantic Search:** Stores and indexes extracted text using ChromaDB and Sentence Transformers.
- **Gradio UI:** User-friendly interface for upload, OCR, and search.

---

## 🐳 Deployment (Docker)

The app is designed to run in a Docker container.  
**Key system dependencies (Poppler, Tesseract) are installed in the Dockerfile.**

**To build and run locally:**
```sh
docker build -t doc-ocr-semantic .
docker run -p 7860:7860 doc-ocr-semantic
```
Then visit [http://localhost:7860](http://localhost:7860)

---

## 📝 How to Use

1. **Upload a PDF or image** in the "Upload & OCR" tab.
2. **View the extracted text** in the OCR Result box.
3. **Use the "Semantic Search" tab** to query your uploaded documents by meaning.

---

## ⚙️ Requirements

- Python 3.8+
- Docker (for local deployment)
- See `requirements.txt` for Python dependencies

---

## 📦 Key Dependencies

- [gradio](https://gradio.app/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [pdf2image](https://pypi.org/project/pdf2image/)
- [chromadb](https://www.trychroma.com/)
- [sentence-transformers](https://www.sbert.net/)

---

## 🧑‍💻 Author

- **Heerak Kashyap**

---

## 🌐 Live Demo

[https://huggingface.co/spaces/heerk30/docker-testing](https://huggingface.co/spaces/heerk30/docker-testing)

---

## 📄 License

This project is for educational and demonstration purposes.

---
