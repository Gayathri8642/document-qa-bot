def chunk_text(text, chunk_size=300, overlap=50):
    """
    Split text into overlapping word-based chunks.
    """
    words = text.split()

    if not words:
        return []

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        if end >= len(words):
            break

        start = end - overlap

    return chunks


def create_chunks(documents, chunk_size=300, overlap=50):
    """
    Create chunks while preserving document metadata.
    """
    all_chunks = []

    for document in documents:
        text_chunks = chunk_text(
            document["text"],
            chunk_size=chunk_size,
            overlap=overlap
        )

        for chunk in text_chunks:
            all_chunks.append(
                {
                    "text": chunk,
                    "source": document["source"],
                    "page": document["page"],
                }
            )

    return all_chunks
