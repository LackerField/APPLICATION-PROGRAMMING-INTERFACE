from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="Hugging Face Sentiment Analysis API",
    description="A simple FastAPI application wrapping a Hugging Face model for sentiment analysis.",
    version="1.0.0"
)

try:
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    classifier = None

class InputData(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Sentiment Analysis API!",
        "description": "This API provides text sentiment classification using a pre-trained Hugging Face model.",
        "endpoints": {
            "GET /": "API introduction and information",
            "GET /health": "System health check",
            "POST /predict": "Performs sentiment analysis prediction on input text"
        }
    }

@app.get("/health")
def health_check():
    if classifier is None:
        raise HTTPException(status_code=500, detail="Model failed to initialize.")
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict")
def predict_sentiment(data: InputData):
    if not data.text or not data.text.strip():
        raise HTTPException(status_code=400, detail="Input validation error: 'text' cannot be empty or whitespace.")
    
    if classifier is None:
        raise HTTPException(status_code=500, detail="Model is not available for inference.")
    
    try:
        result = classifier(data.text)[0]
        return {
            "input_text": data.text,
            "prediction": {
                "label": result["label"],
                "score": round(float(result["score"]), 4)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model inference error: {str(e)}")