def simulate_save_to_chroma(chunks, metadata):
    """
    Simulate saving chunks to ChromaDB by printing them to the console.
    """
    print("\n--- Simulating Save to ChromaDB ---")
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i + 1}:\n{chunk[:200]}...")  # Show first 200 characters
        print(f"Metadata: {metadata}")
    print("\n--- End Simulation ---\n")
