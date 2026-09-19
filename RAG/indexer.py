from RAG.chunker import chunk_text
from RAG.embeddings.ollama_embedding import embed_text
from RAG.vector_store import add_to_store
from tools.document_reader import read_document

def index_document(file_path):
    text = read_document(file_path)

    if isinstance(text, list):
        text = "\n".join(text)

    chunks = chunk_text(text)

    for chunk in chunks:
        vector = embed_text(chunk)
        add_to_store(chunk, vector)