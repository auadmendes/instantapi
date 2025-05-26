import chromadb
from chromadb.config import Settings
import uuid
import os

# Persistent storage directory
CHROMA_DB_DIR = "chroma_db"

client = chromadb.Client(Settings(
    persist_directory=CHROMA_DB_DIR,
    anonymized_telemetry=False
))

# You can reuse the same collection name or make it dynamic
COLLECTION_NAME = "documents"
collection = client.get_or_create_collection(name=COLLECTION_NAME)


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
