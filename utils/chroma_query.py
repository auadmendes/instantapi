from chromadb.config import Settings
import chromadb
import uuid
import os

from sentence_transformers import SentenceTransformer

# Disable SSL check for HuggingFace models (only if really needed)
os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"

# Load the embedder
embedder = SentenceTransformer('./models/all-MiniLM-L6-v2')

# Set ChromaDB directory
CHROMA_DB_DIR = "chroma_db"

# Create client and collection
client = chromadb.Client(Settings(
    persist_directory=CHROMA_DB_DIR,
    anonymized_telemetry=False
))
collection = client.get_or_create_collection(name="documents")


def embed_text(text):
    return embedder.encode(text).tolist()


def query_chromadb_questions(questions, n_results=3):
    """
    Accepts a list of questions, queries ChromaDB for each, and returns a list of result dicts.
    Each dict contains the question and associated documents.
    """
    results = []

    for question in questions:
        embedding = embed_text(question)

        query_result = collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )

        documents = query_result.get("documents", [[]])[0] if "documents" in query_result else []
        metadatas = query_result.get("metadatas", [[]])[0] if "metadatas" in query_result else []
        distances = query_result.get("distances", [[]])[0] if "distances" in query_result else []

        results.append({
            "question": question,
            "documents": documents,
            "metadatas": metadatas,
            "distances": distances
        })

    return results
