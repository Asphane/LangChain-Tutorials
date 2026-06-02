# Text Splitters

This directory contains examples and scripts for splitting large documents into smaller chunks using LangChain's Text Splitter utilities. 

Splitting text is a crucial step when working with Large Language Models (LLMs), as they often have context length limits. By breaking down large documents into smaller, manageable chunks, we can process them more efficiently and accurately.

## Files

- **`length_based.py`**: A demonstration of how to use the `CharacterTextSplitter` class. It loads a PDF document and splits it into chunks of a fixed character length (e.g., 100 characters) without any overlap, using a specific separator.

## How to Run

Make sure you are in the project root and your virtual environment is activated, then run:

```bash
python Text_Splitters/length_based.py
```
