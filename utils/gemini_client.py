import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_GENERATIVE_AI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model (text-only model)
model = genai.GenerativeModel("gemini-pro")

def generate_gemini_summary(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text


