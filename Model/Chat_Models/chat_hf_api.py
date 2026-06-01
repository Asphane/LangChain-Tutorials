from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

"""
This script demonstrates how to use open-source language models hosted on Hugging Face.
It uses HuggingFaceEndpoint to connect to the model, and ChatHuggingFace to format the inputs.
"""

# Load environment variables (like your HuggingFace API token) from the .env file
load_dotenv()

# Set up the connection to the Hugging Face model (Qwen 2.5 in this case)
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

# Wrap the endpoint in a Chat model to make it behave like a conversational bot
model = ChatHuggingFace(llm=llm)

# Send a question to the model
result = model.invoke("What is the capital of India")

# Print the text content of the result
print(result.content)