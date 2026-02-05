from pathlib import Path
import json
import joblib

from fastapi import FastAPI
from pydantic import BaseModel


# --------------------------------------------------
# Resolve project root and artifact paths
# --------------------------------------------------
MODEL_PATH = Path("artifacts/model_trainer/models/LinearSVM.pkl")
VECTORIZER_PATH = Path("artifacts/data_preprocessing/tfidf_vectorizer.pkl")
LABEL_MAP_PATH = Path("artifacts/data_preprocessing/label_mapping.json")

# --------------------------------------------------
# Load model artifacts once at startup
# --------------------------------------------------
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

with open(LABEL_MAP_PATH, "r") as f:
    label_mapping = json.load(f)

inverse_label_mapping = {v: k for k, v in label_mapping.items()}


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------
app = FastAPI(
    title="Spam Detection Service",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    text: str


@app.get("/")
def health_check():
    return {"status": "running"}


@app.post("/predict")
def predict(request: PredictionRequest):
    features = vectorizer.transform([request.text])
    prediction = model.predict(features)[0]

    return {
        "text": request.text,
        "label": inverse_label_mapping[int(prediction)]
    }
