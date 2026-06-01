"""
This script shows how to manually parse the model's output without using an LCEL chain.
Instead of using StrOutputParser, we extract the text manually using `.content`.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="write a 3 line summary on the following text./n {text}",
    input_variables=["text"]
)

# First step: Create and invoke the first prompt manually
prompt1 = template1.invoke({"topic": "black hole"})
result1 = model.invoke(prompt1)

# Second step: Manually extract the text using `.content` and pass it to the second prompt
prompt2 = template2.invoke({"text": result1.content})
result2 = model.invoke(prompt2)

print("Detailed Report: ", result1.content)
print()
print("Summary: ", result2.content)