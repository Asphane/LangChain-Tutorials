"""
This script lists all the available models in your Google GenAI account.
It helps you see which models (like gemini-1.5-pro) you can use and what actions they support.
"""
import os
from google import genai
from dotenv import load_dotenv

# Load environment variables (like GEMINI_API_KEY) from the .env file
load_dotenv()

# Create a client to interact with the Google GenAI API
client = genai.Client()
try:
    # Loop through all models available to your account
    for model in client.models.list():
        # Print the model name and what actions it can perform (e.g., generateContent)
        print(model.name, model.supported_actions)
except Exception as e:
    # Catch and print any errors (like an invalid API key)
    print("Error:", e)
