from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

"""
This script shows how to connect to OpenAI's language models (like ChatGPT).
It creates a basic chat model and asks it a simple question.
"""

# Load environment variables (like your OPENAI_API_KEY) from the .env file
load_dotenv()

# Set up the OpenAI chat model (using gpt-3.5-turbo)
llm =ChatOpenAI(model="gpt-3.5-turbo")

# Ask the model a question
res=llm.invoke("What is the capital of India?")

# Print the model's response
print(res)