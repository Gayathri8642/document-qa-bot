from src.chunking import chunk_text


def test_chunking_creates_chunks():
    text = " ".join(["Python"] * 700)

    chunks = chunk_text(
        text,
        chunk_size=300,
        overlap=50
    )

    assert len(chunks) > 1
    assert all(chunk for chunk in chunks)


def test_empty_text_returns_empty_list():
    assert chunk_text("") == []