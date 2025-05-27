# Document Research & Theme Identification Chatbot

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

![image](https://github.com/user-attachments/assets/5d822ee6-6d23-47f6-b36f-768c3e6df483)



---

## 📄 License

This project is for educational and demonstration purposes.

---
