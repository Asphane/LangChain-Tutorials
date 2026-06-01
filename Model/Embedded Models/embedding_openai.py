# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# result = embedding.embed_query("Delhi is the capital of India")

# print(str(result))

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

"""
This script demonstrates how to convert text into embeddings (lists of numbers)
using OpenAI's embedding models. Embeddings are useful for searching and comparing text.
"""

# Load environment variables (like your OPENAI_API_KEY)
load_dotenv()

# Set up the OpenAI embedding model, specifying the model name and desired dimensions
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# A list of simple sentences to embed
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Convert the sentences into embeddings (number vectors)
result = embedding.embed_documents(documents)

print(str(result))