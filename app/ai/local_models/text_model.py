# app/ai/local_models/text_model.py

import os
import joblib

_model_path = os.path.join("app", "ai", "local_models", "text_model.joblib")

_text_model = None

def load_text_model():
    global _text_model
    if _text_model is None:
        if os.path.exists(_model_path):
            _text_model = joblib.load(_model_path)
    return _text_model

def predict_text(msg: str):
    model_data = load_text_model()
    if not model_data:
        return {"label": "unknown", "prob": 0.0}

    model = model_data["model"]
    vectorizer = model_data["vectorizer"]

    X = vectorizer.transform([msg])
    prob = model.predict_proba(X)[0]

    idx = prob.argmax()
    label = model.classes_[idx]

    return {"label": label, "prob": float(prob[idx])}
