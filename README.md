# Basic Document Q&A Bot using RAG

## 1. Project Overview

This project is a basic Document Question-Answering Bot built using
Retrieval-Augmented Generation (RAG).

The system allows users to ask natural-language questions about a
collection of documents. It retrieves relevant document chunks using
semantic similarity and then uses an LLM to generate an answer based
only on the retrieved context.

The application also displays the source documents, similarity scores,
and retrieved chunks used to generate the answer.

---

## 2. Features

- Load PDF and text documents
- Extract and clean document text
- Preserve PDF page information
- Split documents into overlapping chunks
- Generate semantic embeddings in batches
- Store embeddings in a persistent FAISS vector index
- Retrieve the most relevant document chunks
- Generate answers using Google Gemini
- Use retrieved document context for answer generation
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

The documents cover:

- Python programming
- SQL databases
- REST API development
- Flask web development
- Software testing

The collection contains both PDF and text documents.

---

## 4. Technology Stack

- Python 3.11+
- PyMuPDF
- Sentence Transformers
- FAISS
- Google Gemini API
- python-dotenv
- NumPy

### Embedding Model

`all-MiniLM-L6-v2`

The embedding model converts document chunks and user questions into
vectors that can be compared for semantic similarity.

### Vector Store

FAISS is used to store and search the document embeddings.

Normalized vectors and inner-product search are used to perform
cosine-similarity-based retrieval.

### Language Model

Google Gemini is used to generate the final answer from the retrieved
document context.

---

## 5. Architecture

The RAG pipeline works as follows:

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
