from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model():
    """Load the sentence-transformer embedding model."""
    return SentenceTransformer(MODEL_NAME)


def create_embeddings(chunks, model, batch_size=32):
    """Create embeddings for all chunks using batched encoding."""
    texts = [chunk["text"] for chunk in chunks]

    if not texts:
        return []

    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
    )

    return embeddings