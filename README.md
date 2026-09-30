# Basic Document Q&A Bot using RAG

## 1. Project Overview

This project is a basic Document Question-Answering Bot built using
Retrieval-Augmented Generation (RAG).

The system allows users to ask natural-language questions about a
collection of documents. It retrieves relevant document chunks using
semantic similarity and then uses an LLM to generate an answer based
only on the retrieved context.

The application also displays the source documents and retrieved chunks
used to generate the answer.

---

## 2. Features

- Load PDF and text documents
- Extract and clean document text
- Split documents into overlapping chunks
- Generate semantic embeddings
- Store embeddings in a persistent FAISS vector index
- Retrieve the most relevant document chunks
- Generate answers using Google Gemini
- Display source filename and page information
- Display retrieved source chunks
- Handle questions that cannot be answered from the documents
- Interactive command-line interface

---

## 3. Documents

The project currently uses five documents:

1. `python_programming.pdf`
2. `sql_databases.txt`
3. `rest_api_development.txt`
4. `flask_web_development.txt`
5. `software_testing.txt`

The collection covers Python programming, SQL databases, REST APIs,
Flask web development, and software testing.

---

## 4. Technology Stack

- Python 3.11+
- PyMuPDF
- python-docx
- Sentence Transformers
- FAISS
- Google Gemini API
- python-dotenv
- NumPy

### Embedding Model

`all-MiniLM-L6-v2`

### Vector Database

FAISS using cosine similarity through normalized inner-product search.

### Language Model

Google Gemini

---

## 5. Architecture

The RAG pipeline follows these steps:

```text
Documents
    |
    v
Document Ingestion
    |
    v
Text Extraction
    |
    v
Chunking with Overlap
    |
    v
Embedding Generation
    |
    v
FAISS Vector Index
    |
    v
User Question
    |
    v
Query Embedding
    |
    v
Similarity Search
    |
    v
Top-K Retrieved Chunks
    |
    v
Gemini
    |
    v
Answer + Sources
