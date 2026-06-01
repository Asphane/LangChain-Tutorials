"""
This script demonstrates how to add basic conditional logic using RunnableBranch.
It generates a detailed note and, if the note is too long, automatically summarizes it.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch

# Load environment variables
load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

def count(text):
    return len(text.split())

prompt1=PromptTemplate(
    template='write a detailed note on the topic: {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a summary on the topic: {topic}',
    input_variables=['topic']
)

# First chain to generate a detailed note
detailed_note_chain=RunnableSequence(prompt1, model, parser)

# Branching logic (IF-ELSE equivalent in LangChain):
# If the note is longer than 500 words, run it through the summary chain.
# Otherwise (else), just pass the text through unchanged using RunnablePassthrough.
branch_chain=RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

# Combine them: generate note -> check if it needs summarizing -> return final result
chain=RunnableSequence(detailed_note_chain, branch_chain)
res=chain.invoke({'topic': 'coding'})

print(res)