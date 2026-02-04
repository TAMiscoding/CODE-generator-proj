import os
from dotenv import load_dotenv
from google import genai

# Load .env variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Use ONLY models confirmed available for your account
MODEL_NAME = "models/gemini-flash-latest"
# Alternative (stronger but slower):
# MODEL_NAME = "models/gemini-pro-latest"


def generate_code(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if not response or not response.text:
            raise RuntimeError("Empty response from Gemini")

        return response.text.strip()

    except Exception as e:
        raise RuntimeError(f"LLM generation failed: {e}")
