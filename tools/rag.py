from RAG.retriever import query_rag

def rag_tool(query, k=3):
    return query_rag(query, k)