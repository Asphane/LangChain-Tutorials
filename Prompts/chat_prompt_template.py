"""
This script demonstrates how to build a ChatPromptTemplate.
Chat models expect a list of messages (like System and Human messages) instead of a single string.
"""
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
# Define the structure of the chat: setting the system's role and the human's input format
chat_template=ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

# Provide the specific details to fill in the placeholders {domain} and {topic}
prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})
print(prompt)