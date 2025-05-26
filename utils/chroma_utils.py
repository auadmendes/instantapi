import chromadb
from chromadb.config import Settings
import uuid
import os



os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"  # Set BEFORE importing SentenceTransformer

from sentence_transformers import SentenceTransformer
embedder = SentenceTransformer('./models/all-MiniLM-L6-v2')



# Persistent storage directory
CHROMA_DB_DIR = "chroma_db"

client = chromadb.Client(Settings(
    persist_directory=CHROMA_DB_DIR,
    anonymized_telemetry=False
))

COLLECTION_NAME = "documents"
collection = client.get_or_create_collection(name=COLLECTION_NAME)


def embed_text(text):
    """
    Generate embedding for a single string.
    """
    return embedder.encode(text).tolist()


def save_to_chroma(chunks, metadata):
    """
    Save the chunks and metadata to ChromaDB.
    """
    print(f"\n--- Saving to ChromaDB ({COLLECTION_NAME}) ---")

    documents = chunks
    metadatas = [metadata for _ in chunks]
    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"✅ Saved {len(chunks)} chunks to ChromaDB.")
    print("--- End Save ---\n")


def get_all_documents():
    """
    Retrieve all stored document metadata from ChromaDB.
    """
    docs = collection.get()
    return [{"id": doc_id, "metadata": metadata} for doc_id, metadata in zip(docs["ids"], docs["metadatas"])]


def search_similar_documents(query_text, n_results=5):
    """
    Search for documents similar to the given query.
    """
    query_embedding = embed_text(query_text)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return [
        {
            "id": doc_id,
            "metadata": metadata,
            "distance": distance
        }
        for doc_id, metadata, distance in zip(
            results["ids"][0], results["metadatas"][0], results["distances"][0]
        )
    ]
