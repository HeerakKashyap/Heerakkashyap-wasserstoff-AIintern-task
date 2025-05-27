FROM python:3.10-slim

WORKDIR /app

# Create a writable cache directory for Hugging Face models
RUN mkdir -p /app/hf_cache && chmod 777 /app/hf_cache

# Install system dependencies for pdf2image and tesseract
RUN apt-get update && \
    apt-get install -y poppler-utils tesseract-ocr && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set Hugging Face cache directory to a writable location
ENV HF_HOME=/app/hf_cache

# Optional: Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 7860

CMD ["python", "app.py"] 