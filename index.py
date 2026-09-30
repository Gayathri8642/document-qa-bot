from src.ingestion import load_documents
from src.chunking import create_chunks
from src.embeddings import load_embedding_model, create_embeddings
from src.vector_store import create_index, save_index


def main():
    print("Loading documents...")
    documents = load_documents("data")
    print(f"Loaded {len(documents)} document records.")

    print("Creating chunks...")
    chunks = create_chunks(documents, chunk_size=300, overlap=50)
    print(f"Created {len(chunks)} chunks.")

    print("Loading embedding model...")
    model = load_embedding_model()

    print("Creating embeddings...")
    embeddings = create_embeddings(chunks, model)
    print(f"Created embeddings with shape: {embeddings.shape}")

    print("Creating FAISS index...")
    index = create_index(embeddings)

    print("Saving FAISS index and metadata...")
    save_index(index, chunks)

    print("Indexing completed successfully.")


if __name__ == "__main__":
    main()