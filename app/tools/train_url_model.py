# app/tools/train_url_model.py

import os
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Adjust import path if running as script
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.ai.local_models.url_features import extract_url_features


def main():
    """
    Trains a Logistic Regression model for URL scam detection.
    Reads data from app/data/urls_demo.csv.
    Saves model to app/ai/local_models/url_model.joblib.
    """
    # CSV is in app/data/urls_demo.csv
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    csv_path = os.path.join(base_dir, "app", "data", "urls_demo.csv")
    
    if not os.path.exists(csv_path):
        print(f"❌ CSV not found at {csv_path}")
        return

    print(f"📂 Loading data from {csv_path}...")
    df = pd.read_csv(csv_path)

    rows = []
    labels = []

    print("⚙️ Extracting features...")
    for _, row in df.iterrows():
        feats = extract_url_features(row["url"])
        if feats:
            rows.append(feats)
            labels.append(int(row["label"]))

    if not rows:
        print("❌ No valid rows, nothing to train.")
        return

    feat_order = list(rows[0].keys())
    X = [[r[k] for k in feat_order] for r in rows]
    y = labels

    print(f"🧠 Training model on {len(X)} samples...")
    pipe = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=200)),
        ]
    )

    pipe.fit(X, y)

    model_data = {"model": pipe, "feat_order": feat_order}

    out_path = os.path.join(base_dir, "app", "ai", "local_models", "url_model.joblib")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    joblib.dump(model_data, out_path)

    print(f"✅ Saved model to {out_path}")
    print("ℹ️  Note: Risk levels are determined by probability thresholds in predict_url().")


if __name__ == "__main__":
    main()
