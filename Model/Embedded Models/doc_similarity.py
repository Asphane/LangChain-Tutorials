from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

"""
This script shows how to find the most relevant document for a given question.
It uses OpenAI embeddings to convert text into numbers (vectors), and then calculates
the "cosine similarity" to find the closest match.
"""

# Load environment variables (like your OPENAI_API_KEY)
load_dotenv()

# Initialize the OpenAI embeddings model
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# A list of facts about cricketers
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# The question we want to find the answer to
query = 'tell me about bumrah'

# Convert our list of documents and our query into number vectors
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Calculate how similar the query vector is to each document vector
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find the index of the document with the highest similarity score
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)