import os
import cohere
from dotenv import load_dotenv

load_dotenv()

# Flag to enable/disable Cohere usage
USE_COHERE = os.getenv("USE_COHERE", "false").lower() == "true"

# Load API key safely (no printing!)
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = None
if USE_COHERE and COHERE_API_KEY:
    try:
        co = cohere.Client(COHERE_API_KEY)
    except Exception:
        co = None


def generate_response(prompt):
    """
    Generates a response using Cohere if enabled.
    If Cohere is disabled or not available, returns a simple fallback message.
    """
    # If feature is turned off from .env
    if not USE_COHERE:
        return "⚠️ AI explanation is currently disabled."

    # If client not initialized correctly
    if co is None:
        return "⚠️ AI service not available."

    try:
        response = co.generate(
            model="command-light",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        return response.generations[0].text.strip()

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"
