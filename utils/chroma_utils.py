import chromadb
from chromadb.config import Settings
import uuid
import os
import json



os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"  # Set BEFORE importing SentenceTransformer

from sentence_transformers import SentenceTransformer
embedder = SentenceTransformer('./models/all-MiniLM-L6-v2')



# Persistent storage directory
CHROMA_DB_DIR = "chroma_db"

# Ensure reproducibility
os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"

# Persistent ChromaDB storage

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection(name="documents")

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

def query_chromadb_questions(questions: list[str], n_results: int = 10) -> list[dict]:
    results = []

    for question in questions:
        try:
            print(f"Querying ChromaDB with the question: {question}")
            response = collection.query(
                query_texts=[question],
                n_results=n_results,
                include=["documents", "metadatas"]
            )

            print("Raw ChromaDB Results:")
            print(json.dumps(response, indent=4))

            if response.get("documents") and response.get("metadatas"):
                documents = response["documents"][0]
                metadatas = response["metadatas"][0]

                paired_docs = list(zip(documents, metadatas))

                results.append({
                    "question": question,
                    "documents": paired_docs
                })
            else:
                results.append({
                    "question": question,
                    "documents": []
                })

        except Exception as e:
            #print(f"Error querying ChromaDB: {str(e)}")
            results.append({
                "question": question,
                "error": str(e),
                "documents": []
            })

    return results
