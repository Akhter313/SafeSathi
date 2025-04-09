# app/ai/cohere_gpt.py
import os
import cohere
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def generate_response(prompt):
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
