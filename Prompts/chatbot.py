"""
This script creates a simple interactive chatbot that runs in your terminal.
It keeps track of the conversation history so the model remembers what was said earlier.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
# model=HuggingFaceHub(repo_id="google/gemini-2.5-flash", model_kwargs={"temperature": 0.7})

# Set up the Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

# Convert the base model into a chat model so it understands messages
model = ChatHuggingFace(llm=llm)

# Initialize chat history with a system message setting the AI's persona
chat_history=[SystemMessage(content="You are a helpful assistant.")]

# Start an infinite loop to chat with the user
while True:
    user_input=input('User: ')
    
    # Add the user's message to the history
    chat_history.append(HumanMessage(content=user_input))
    
    # Check if the user wants to quit
    if(user_input.lower() in ['exit', 'quit']):
        print("Exiting the chatbot. Goodbye!")
        break

    # Pass the entire conversation history to the model
    response=model.invoke(chat_history)
    
    # Save the model's response to the history so it remembers it next time
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")

# Print out the full history when the chat ends
print("Chat history:", chat_history)