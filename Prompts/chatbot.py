from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
# model=HuggingFaceHub(repo_id="google/gemini-2.5-flash", model_kwargs={"temperature": 0.7})

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_history=[SystemMessage(content="You are a helpful assistant.")]

while True:
    user_input=input('User: ')
    chat_history.append(HumanMessage(content=user_input))
    if(user_input.lower() in ['exit', 'quit']):
        print("Exiting the chatbot. Goodbye!")
        break

    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")

print("Chat history:", chat_history)