from src.ingestion import load_documents


def test_load_documents():
    documents = load_documents("data")

    assert len(documents) > 0
    assert all("text" in document for document in documents)
    assert all("source" in document for document in documents)