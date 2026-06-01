"""
This script shows how to run prompts one after another (sequentially).
The output of the first prompt is automatically fed into the next prompt.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

# First prompt: Generate a long detailed report
prompt1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# Second prompt: Take the text (from prompt1) and summarize it
prompt2=PromptTemplate(
    template="write a 5 point summary on {text}",
    input_variables=["text"]
)

# Link everything together sequentially using the pipe (|) operator
# Flow: prompt1 -> model -> text -> prompt2 -> model -> final summary
chain=prompt1 | model | parser | prompt2 | model | parser

# Run the chain starting with the initial topic
result=chain.invoke({"topic": "genAI"})
print("Report: ", result)