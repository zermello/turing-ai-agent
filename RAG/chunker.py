def chunk_text(text, chunk_size=500, overlap=50):

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk_text = text[start:end]
        chunks.append(chunk_text)

        start = end - overlap

    return chunks