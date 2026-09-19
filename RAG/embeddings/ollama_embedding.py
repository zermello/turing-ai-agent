import ollama

MODEL_NAME = "nomic-embed-text"

def embed_text(text):
    response = ollama.embed(
        model = MODEL_NAME,
        input = text
    )

    return response.embeddings[0]