from RAG.embeddings.ollama_embedding import embed_text
from RAG.vector_store import vector_store
from RAG.similarity import cosine_similarity

def retrieve(query, k=3):
    query = embed_text(query)

    results = []

    for i in vector_store:
       score =  cosine_similarity(query, i["vector"])
       results.append([score, i["chunk"]])

    results = sorted(results, reverse=True)
    return results[:k]

def build_context(results):
    context = []

    for i in results:
        context.append(i[1])

    return "\n\n".join(context)

def query_rag(query, k=3):
    results = retrieve(query, k)
    context = build_context(results)

    return context