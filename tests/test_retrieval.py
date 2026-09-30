from src.embeddings import load_embedding_model
from src.vector_store import load_index
from src.retrieval import retrieve


def test_retrieval_returns_results():
    model = load_embedding_model()
    index, chunks = load_index()

    results = retrieve(
        "What is a primary key?",
        model,
        index,
        chunks,
        top_k=3
    )

    assert len(results) == 3
    assert all("text" in result for result in results)
    assert all("source" in result for result in results)