# Vector Stores with LangChain

This directory contains examples and code demonstrating how to use vector stores (specifically ChromaDB) with LangChain.

## Contents

- `vector.ipynb`: A Jupyter Notebook that demonstrates the full lifecycle of vector store usage:
  - Initializing `Chroma` and persisting it locally.
  - Generating embeddings using `HuggingFaceEmbeddings` with the `sentence-transformers/all-MiniLM-L6-v2` model.
  - Creating and adding `Document` objects with metadata to the vector store.
  - Performing vector searches: basic `similarity_search` and `similarity_search_with_score`.
  - Filtering vector search results using metadata.
  - Updating existing documents.
  - Deleting documents from the vector store using their IDs.
- `vector.py`: A Python script containing some of the core vector store setup and operations demonstrated in the notebook.

## Setup

Make sure to install the required dependencies before running the code in this directory:

```bash
pip install langchain chromadb sentence-transformers langchain_huggingface
```

## Notes

- The ChromaDB database files are persisted locally in a directory named `chroma_db/`. This directory is added to `.gitignore` to prevent committing large binary database files to version control.
- Jupyter Notebook checkpoints (`.ipynb_checkpoints/`) are also ignored to keep the repository clean.
