from pathlib import Path
import json
import faiss
import numpy as np


INDEX_PATH = Path("storage/faiss.index")
METADATA_PATH = Path("storage/metadata.json")


def create_index(embeddings):
    """Create a FAISS index using cosine similarity."""
    embeddings = np.asarray(embeddings, dtype="float32")

    # Normalize vectors so inner product represents cosine similarity.
    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    return index


def save_index(index, chunks):
    """Save the FAISS index and chunk metadata to disk."""
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(INDEX_PATH))

    with open(METADATA_PATH, "w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=2)


def load_index():
    """Load the FAISS index and metadata from disk."""
    if not INDEX_PATH.exists() or not METADATA_PATH.exists():
        raise FileNotFoundError(
            "FAISS index or metadata not found. Run index.py first."
        )

    index = faiss.read_index(str(INDEX_PATH))

    with open(METADATA_PATH, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    return index, chunks