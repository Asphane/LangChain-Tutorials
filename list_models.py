import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
try:
    for model in client.models.list():
        print(model.name, model.supported_actions)
except Exception as e:
    print("Error:", e)
