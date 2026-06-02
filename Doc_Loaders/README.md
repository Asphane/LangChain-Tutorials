# Document Loaders

This directory contains examples and scripts for loading various types of documents using LangChain's Document Loader utilities. 

Document loaders are a crucial first step when building LLM applications, as they allow you to import data from different sources and formats into standardized LangChain `Document` objects, which can then be processed, split, and embedded.

## Files

- **`csvLoader.py`**: Example of loading data from CSV files.
- **`directoryLoader.py`**: Example of loading multiple documents from a specific directory.
- **`pdfLoader.py`**: Example of parsing and loading text from PDF documents.
- **`text_based_docLoader.py`**: Example of loading raw text files.

*Note: Data files such as PDFs and CSVs are ignored in this repository.*

## How to Run

Ensure your virtual environment is activated and run the scripts from the project root:

```bash
python Doc_Loaders/pdfLoader.py
```
