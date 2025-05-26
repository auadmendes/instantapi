def format_chroma_results_and_references(chroma_results):
    if not chroma_results or not chroma_results[0].get("documents"):
        return "No relevant references found in ChromaDB.", ""
    
    formatted_snippets = []
    how_to_references = []
    
    for result in chroma_results:
        for doc, metadata in zip(result.get("documents", []), result.get("metadatas", [])):
            snippet = doc[:500]
            doc_type = metadata.get("type", "").lower()
            source = metadata.get("source", "unknown")
            formatted = f"- ({doc_type.upper()} from {source}) {snippet} [...]"
            
            if doc_type == "kb":
                how_to_references.append(formatted)
            else:
                formatted_snippets.append(formatted)
    
    chroma_context = "\n".join(formatted_snippets)
    kb_reference_block = "\n".join(how_to_references)
    
    return chroma_context, kb_reference_block

