"""
This script shows how to create a very basic LCEL (LangChain Expression Language) chain.
It connects a prompt, a HuggingFace language model, and an output parser in a straight line.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser

# Load environment variables
load_dotenv()

# Set up the HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

# Set up an output parser to extract the text response
parser=StrOutputParser()

# Create a prompt template asking for a report
prompt=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# Connect them using the pipe (|) operator to form a chain
chain=prompt | model | parser

# Run the chain with a specific topic
result=chain.invoke({"topic": "genAI"})
print("Report: ", result)