from embeddings.ollama_embedding import embed_text
from vector_store import vector_store
from similarity import cosine_similarity

def retrieve(query):
    query = embed_text(query)

    best_score = 0
    best_chunk = ""

    for i in vector_store:
       score =  cosine_similarity(query, i["vector"])
       if score > best_score:
        best_score = score
        best_chunk = i["chunk"]

    return best_chunk

result = retrieve("What is used for building robot software?")
print(result)