from langchain_openai import OpenAI
from dotenv import load_dotenv

"""
This script demonstrates how to connect to OpenAI's language models.
It uses the base OpenAI class to generate a response for a given prompt.
"""

# Load environment variables (like your OPENAI_API_KEY) from the .env file
load_dotenv()

# Set up the OpenAI model (using gpt-3.5-turbo)
llm =OpenAI(model="gpt-3.5-turbo")

# Ask the model a question
res=llm.invoke("What is the capital of India?")

# Print the model's response
print(res)