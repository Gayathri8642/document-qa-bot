from pathlib import Path
import pymupdf


def load_pdf(file_path):
    """Extract text from a PDF while preserving page numbers."""
    documents = []

    pdf = pymupdf.open(file_path)

    for page_number, page in enumerate(pdf, start=1):
        text = page.get_text("text").strip()

        if text:
            documents.append(
                {
                    "text": text,
                    "source": Path(file_path).name,
                    "page": page_number,
                }
            )

    pdf.close()
    return documents


def load_text_file(file_path):
    """Read a text file as a single document."""
    path = Path(file_path)

    text = path.read_text(encoding="utf-8").strip()

    if not text:
        return []

    return [
        {
            "text": text,
            "source": path.name,
            "page": None,
        }
    ]


def load_documents(data_directory="data"):
    """Load supported documents from the data directory."""
    data_path = Path(data_directory)
    documents = []

    for file_path in sorted(data_path.iterdir()):
        if file_path.suffix.lower() == ".pdf":
            documents.extend(load_pdf(file_path))

        elif file_path.suffix.lower() == ".txt":
            documents.extend(load_text_file(file_path))

    return documents