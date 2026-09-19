from RAG.embeddings.ollama_embedding import embed_text

vector_store = []

def add_to_store(chunk, vector):
    vector_store.append({
        "chunk": chunk,
        "vector": vector
    })