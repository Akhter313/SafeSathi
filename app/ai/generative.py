# app/ai/generative.py

import os
from dotenv import load_dotenv

load_dotenv()

USE_COHERE = os.getenv("USE_COHERE", "false").lower() == "true"


def explain_risk_local(text: str) -> str:
    """
    Simple, local, rule-based explanation.
    No external API. Always safe and offline.
    """
    return (
        "⚠️ This may be risky. Be careful with unknown links or messages, especially "
        "if they ask for OTP, bank details, or urgent payments. "
        "Verify using official apps or websites instead of clicking directly."
    )


def explain_risk(text: str) -> str:
    """
    If USE_COHERE=true and key is set, try Cohere to generate a nicer explanation.
    Otherwise fall back to a fixed local message.
    """
    if not USE_COHERE:
        # Cohere is disabled -> always local explanation
        return explain_risk_local(text)

    try:
        # Lazy import so project works even if cohere is not fully set
        from app.ai.cohere_gpt import generate_response

        prompt = (
            "Explain in simple WhatsApp-style language why this might be a risky "
            "link or message and what the user should do to stay safe:\n\n"
            f"{text}"
        )

        response = generate_response(prompt)
        # If Cohere is not available, generate_response will return an error string.
        # We can detect that and fall back to local.
        if response.startswith("⚠️ AI"):
            return explain_risk_local(text)
        return response

    except Exception:
        # Any error -> fallback to safe local explanation
        return explain_risk_local(text)
