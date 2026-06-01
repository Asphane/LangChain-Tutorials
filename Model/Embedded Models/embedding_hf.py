"""
This script shows how to generate text embeddings using open-source models from Hugging Face.
Embeddings convert text into a mathematical representation (a list of numbers).
"""
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize the Hugging Face embedding model (using a lightweight sentence-transformer)
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# A list of sentences we want to convert to embeddings
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Convert the sentences into vector embeddings
vector = embedding.embed_documents(documents)

print(str(vector))