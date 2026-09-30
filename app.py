from src.embeddings import load_embedding_model
from src.vector_store import load_index
from src.retrieval import retrieve
from src.generator import create_client, generate_answer


def main():
    print("Loading embedding model...")
    embedding_model = load_embedding_model()

    print("Loading FAISS index...")
    index, chunks = load_index()

    print("Connecting to Gemini...")
    client = create_client()

    print("\nDocument Q&A Bot")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask a question: ").strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        if not query:
            print("Please enter a question.\n")
            continue

        print("\nRetrieving relevant documents...")

        retrieved_chunks = retrieve(
            query,
            embedding_model,
            index,
            chunks,
            top_k=5
        )

        answer = generate_answer(
            client,
            query,
            retrieved_chunks
        )

        print("\nAnswer:")
        print(answer)

        print("\nSources:")

        for chunk in retrieved_chunks:
            source = chunk["source"]
            page = chunk.get("page")
            score = chunk.get("score", 0)

            if page:
                location = f"{source}, page {page}"
            else:
                location = source

            print(f"- {location} (score: {score:.3f})")

        print("\nRetrieved Chunks:")

        for number, chunk in enumerate(retrieved_chunks, start=1):
            source = chunk["source"]
            page = chunk.get("page")

            if page:
                location = f"{source}, page {page}"
            else:
                location = source

            print(f"\n[{number}] {location}")
            print("-" * 60)
            print(chunk["text"])

        print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()