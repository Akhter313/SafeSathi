import re
import math
from urllib.parse import urlparse
import tldextract

SHORTENERS = {"bit.ly","tinyurl.com","t.co","goo.gl","is.gd","cutt.ly","rb.gy"}

def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    from collections import Counter
    counts = Counter(s)
    n = len(s)
    return -sum((c/n) * math.log2(c/n) for c in counts.values())

def extract_url_features(url: str):
    try:
        if not url.startswith(("http://","https://")):
            url = "http://" + url

        parsed = urlparse(url)
        host = parsed.hostname or ""
        path = parsed.path or ""

        ext = tldextract.extract(host)
        domain = (ext.domain + "." + ext.suffix) if ext.suffix else ext.domain
        tld = ext.suffix.lower() if ext.suffix else ""

        features = {
            "len_url": len(url),
            "len_host": len(host),
            "dots": host.count("."),
            "subdomains": max(0, host.count(".") - 1),
            "has_ip": bool(re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", host)),
            "has_at": "@" in url,
            "has_dash": "-" in host,
            "digits_ratio": sum(ch.isdigit() for ch in url) / max(1, len(url)),
            "pct_encoded": url.count("%") / max(1, len(url)),
            "q_params": (parsed.query.count("&") + 1 if parsed.query else 0),
            "tld_len": len(tld),              # numeric instead of string
            "is_shortener": domain in SHORTENERS,
            "entropy_host": shannon_entropy(host),
            "entropy_path": shannon_entropy(path),
            "https": 1 if parsed.scheme == "https" else 0,
        }

        return features

    except Exception:
        return None
