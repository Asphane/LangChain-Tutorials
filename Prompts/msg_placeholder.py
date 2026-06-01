"""
This script shows how to use MessagesPlaceholder in a chat prompt.
A placeholder is useful when you have a list of messages (like chat history)
that you want to insert directly into the prompt without converting them to text.
"""
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder
# Create a chat template with system instructions, a placeholder for history, and the new query
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]

# Read past chat history from a text file and add it to our list
with open('Prompts/chat_history.txt', 'r') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# Fill in the template with our history and the specific question
prompt=chat_template.invoke({
    'chat_history': chat_history,
    'query': 'Where is my refund?'
})