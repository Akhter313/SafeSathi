# app/ai/local_models/__init__.py
import os
import joblib
from .url_features import extract_url_features

# Path to our (future) trained model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), "url_model.joblib")

_url_model = None   # lazy-loaded


def _load_url_model():
    """Load the URL model from disk when first needed."""
    global _url_model
    if _url_model is None and os.path.exists(MODEL_PATH):
        _url_model = joblib.load(MODEL_PATH)
    return _url_model


def predict_url(url: str):
    """
    Use the local lightweight model to classify a URL.
    If the model file is missing, returns 'unknown'.
    """
    result = {"label": "unknown", "prob": 0.0, "suggestion": None}

    # Heuristic: Check for common typos/phishing patterns in hostname
    # e.g. http.amazon.in, http-login.com
    try:
        # Basic normalization for parsing
        temp_url = url
        if not temp_url.startswith(("http://", "https://")):
            temp_url = "http://" + temp_url
        
        from urllib.parse import urlparse
        parsed = urlparse(temp_url)
        host = parsed.hostname or ""
        
        # 1. Typo checks (http.amazon.in) - only if user didn't provide a proper protocol
        # If the original URL already has http:// or https://, then "https.amazon.in" is a legitimate hostname
        has_protocol = url.lower().startswith(("http://", "https://"))
        
        if not has_protocol and host.startswith("http."):
            result["label"] = "suspicious"
            result["prob"] = 0.95
            result["suggestion"] = "http://" + url.replace("http.", "", 1)
            return result
            
        if not has_protocol and host.startswith("https."):
            result["label"] = "suspicious"
            result["prob"] = 0.95
            result["suggestion"] = "https://" + url.replace("https.", "", 1)
            return result
        
        if "http-" in host or "https-" in host:
             result["label"] = "suspicious"
             result["prob"] = 0.85
             return result

        # 2. Enforce HTTP = Suspicious (User Request)
        # If the original URL explicitly starts with http://, flag it.
        if url.lower().startswith("http://"):
            result["label"] = "suspicious"
            result["prob"] = 0.75
            result["suggestion"] = url.replace("http://", "https://", 1)
            # We can add a custom note in the result if needed, but for now label is enough.
            return result
             
    except Exception:
        pass

    feats = extract_url_features(url)
    if not feats:
        return result

    model_data = _load_url_model()
    if model_data is None:
        # Model not trained yet
        return result

    feat_order = model_data["feat_order"]
    X = [[feats[k] for k in feat_order]]

    proba = model_data["model"].predict_proba(X)[0][1]  # probability of 'suspicious'
    p = float(proba)

    if p >= 0.6:
        label = "suspicious"
    elif p < 0.45:
        label = "safe"
    else:
        label = "unknown"

    result["label"] = label
    result["prob"] = p
    return result
