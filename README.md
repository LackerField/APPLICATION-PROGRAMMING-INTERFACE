# Computational Thinking - Practice 01: Application Programming Interface

## Student Information

- **Full Name:** Phan Anh Kiệt
- **Student ID:** 25127204
- **Faculty:** Faculty of Information Technology, VNUHCM-University of Science
- **Course:** Computational Thinking
- **Lab Instructors:** Nguyen Ngoc Minh Chau, Le Duc Khoan

## Model Information

- **Selected Model:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Hugging Face Page:** [https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)

## Project Structure

```text
├── main.py
├── test_api.py
├── requirements.txt
└── README.md
```

## Installation & Environment Setup Instructions (using Conda)

```bash
git clone https://github.com/LackerField/APPLICATION-PROGRAMMING-INTERFACE.git
cd APPLICATION-PROGRAMMING-INTERFACE

conda create -n fastapi-env python=3.10 -y
conda activate fastapi-env
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

## API Usage & Examples

### 1. Root Endpoint (`GET /`)

- **Request:** `GET http://127.0.0.1:8000/`
- **Response:**
  ```json
  {
    "message": "Welcome to the Sentiment Analysis API!",
    "description": "This API provides text sentiment classification using a pre-trained Hugging Face model.",
    "endpoints": {
      "GET /": "API introduction and information",
      "GET /health": "System health check",
      "POST /predict": "Performs sentiment analysis prediction on input text"
    }
  }
  ```

### 2. Health Check Endpoint (`GET /health`)

- **Request:** `GET http://127.0.0.1:8000/health`
- **Response:**
  ```json
  {
    "status": "healthy",
    "model_loaded": true
  }
  ```

### 3. Prediction Endpoint (`POST /predict`)

- **Request:** `POST http://127.0.0.1:8000/predict`
- **Headers:** `Content-Type: application/json`
- **Body:**
  ```json
  {
    "text": "I really enjoy building applications with FastAPI and Hugging Face!"
  }
  ```
- **Response:**
  ```json
  {
    "input_text": "I really enjoy building applications with FastAPI and Hugging Face!",
    "prediction": {
      "label": "POSITIVE",
      "score": 0.9998
    }
  }
  ```

## Testing

```bash
python test_api.py
```

## Demonstration Video

- **Video Link:** [Insert your YouTube or Google Drive link here]
