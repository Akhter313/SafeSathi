# app/tools/train_text_model.py

import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def main():
    """
    Trains a TF-IDF + Logistic Regression model for scam text detection.
    Reads data from app/data/scam_texts.csv.
    Saves model to app/ai/local_models/text_model.joblib.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    csv_path = os.path.join(base_dir, "app", "data", "scam_texts.csv")
    
    if not os.path.exists(csv_path):
        print(f"❌ Dataset not found: {csv_path}")
        return

    print(f"📂 Loading data from {csv_path}...")
    df = pd.read_csv(csv_path)

    texts = df["text"].astype(str).values
    labels = df["label"].astype(str).values

    print(f"🧠 Training model on {len(texts)} samples...")
    vectorizer = TfidfVectorizer(
        ngram_range=(1,2),
        min_df=1,
        max_features=3000
    )

    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(max_iter=500)
    model.fit(X, labels)

    model_data = {
        "model": model,
        "vectorizer": vectorizer,
    }

    out_path = os.path.join(base_dir, "app", "ai", "local_models", "text_model.joblib")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    joblib.dump(model_data, out_path)

    print(f"✅ Saved scam text model to {out_path}")


if __name__ == "__main__":
    main()
