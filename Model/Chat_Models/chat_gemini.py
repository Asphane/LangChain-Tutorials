from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

"""
This script shows how to connect to Google's Gemini language model.
We use ChatGoogleGenerativeAI to create a chat model instance and send it a basic question.
"""

# Load environment variables (like your GEMINI API key) from the .env file
load_dotenv()

# Set up the Gemini model (using gemini-2.5-flash for fast responses)
llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Ask the model a question
res=llm.invoke("What is the capital of India?")

# Print out the text content of the model's response
print(res.content)