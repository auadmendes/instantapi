from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from utils.chroma_query import query_chromadb_questions
from utils.genai_utils import generate_answer_with_genai, format_chroma_results

load_dotenv()

ask_bp = Blueprint("ask", __name__)
system_message = (
    "You are an AI assistant for DocuSign.\n" 
    "Answer the DocuSign agent's question as helpfully and clearly as possible, using the provided context when available.\n"
    "If there is a how-to document, provide a summary of the relevant steps.\n"
    "If there is a troubleshooting document, provide a summary of the relevant steps.\n"
)

@ask_bp.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"error": "No question provided"}), 400

        # Get relevant context from ChromaDB
        chroma_results = query_chromadb_questions([question])
        print(f"{chroma_results} ------------------------------------------------------")
        context = format_chroma_results(chroma_results)

        # Create prompt
        prompt = f"{system_message}\n\nQuestion: {question}\n\nContext:\n{context}\n\nAnswer:"

        # Get answer from Gemini
        answer = generate_answer_with_genai(prompt)

        return jsonify({
            "answer": answer,
            "chroma_context": context
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
