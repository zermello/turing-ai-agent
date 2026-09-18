from embeddings.ollama_embedding import embed_text

vector_store = []

def add_to_store(chunk, vector):
    vector_store.append({
        "chunk": chunk,
        "vector": vector
    })

add_to_store("ROS 2 is a middleware framework used for robotics.", embed_text("ROS 2 is a middleware framework used for robotics."))
add_to_store("Chocolate cake is made with cocoa and sugar.", embed_text("Chocolate cake is made with cocoa and sugar."))
add_to_store("Python is a programming language.", embed_text("Python is a programming language."))


