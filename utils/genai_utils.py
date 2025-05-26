import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GENAI_API_KEY = os.getenv("GOOGLE_GENERATIVE_AI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("Missing Gemini API key. Check your .env file.")

# Configure genai
genai.configure(api_key=GENAI_API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_answer_with_genai(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the generated answer.
    """
    try:
        response = model.generate_content(prompt)

        return (
            response.text
            if hasattr(response, "text")
            else "No answer generated."
        )

    except Exception as e:
        return f"Error generating answer: {str(e)}"


def format_chroma_results(chroma_results: list) -> str:
    """
    Converts ChromaDB query results into a human-readable context string.
    """
    if not chroma_results:
        return "No relevant context found."

    formatted = []
    for result in chroma_results:
        docs = result.get("documents", [])
        for doc in docs:
            snippet = doc[:500].strip()
            formatted.append(f"- {snippet} [...]")

    return "\n".join(formatted) if formatted else "No relevant context found."
