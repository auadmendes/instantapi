import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GENAI_API_KEY = os.getenv("GOOGLE_GENERATIVE_AI_API_KEY")

if not GENAI_API_KEY:
    raise ValueError("GOOGLE_GENERATIVE_AI_API_KEY is missing in .env")

def generate_questions_from_subject_and_description(subject: str, description: str) -> list:
    """Generates questions using Gemini AI based on the provided subject and description."""
    if not subject or not description:
        raise ValueError("Both subject and description are required")

    prompt = (
        "You are an AI assistant helping with technical support and knowledge retrieval.\n\n"
        "Your task is to generate useful search queries based on the following support case.\n"
        "These queries will be used to search a vector database (ChromaDB) for relevant documents.\n\n"
        "Given the subject and description below, create 3–5 clear, concise, and information-rich questions or search phrases "
        "that could help retrieve helpful troubleshooting documentation, guides, or previous cases.\n"
        "For each query, also provide a short keyword-based version (5-8 words max).\n\n"
        f"Subject: {subject}\n"
        f"Description: {description}\n\n"
        "Return the result in this format:\n\n"
        "1. Full Question: Why is the API returning a 403 error when authentication is successful?\n"
        "   Keywords: API 403 error after authentication\n\n"
        "2. Full Question: What can cause intermittent Salesforce sync issues after recent updates?\n"
        "   Keywords: Salesforce sync issues after update"
    )


    client = genai.Client(api_key=GENAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    if response and response.candidates:
        raw_text = response.candidates[0].content.parts[0].text
        return [q.strip("-•* ").strip() for q in raw_text.split("\n") if q.strip()]
    
    return []

