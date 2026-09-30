import faiss
import numpy as np


def retrieve(query, model, index, chunks, top_k=5):
    """
    Retrieve the most relevant chunks for a user query.
    """

    # Convert the query into an embedding
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    # Normalize for cosine similarity
    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    faiss.normalize_L2(query_embedding)

    # Search the FAISS index
    scores, indices = index.search(query_embedding, top_k)

    results = []

    for score, index_position in zip(scores[0], indices[0]):
        if index_position == -1:
            continue

        chunk = chunks[index_position].copy()
        chunk["score"] = float(score)

        results.append(chunk)

    return results