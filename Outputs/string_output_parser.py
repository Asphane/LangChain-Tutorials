"""
This script shows how to parse (extract) just the string text from the model's output using StrOutputParser.
This prevents the output from being an AIMessage object and makes it easier to pass to the next prompt.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Set up the HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

# Use StrOutputParser to grab the actual text from the model's response
parser=StrOutputParser()

# First prompt creates a long report
template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# Second prompt takes the long report and creates a summary
template2=PromptTemplate(
    template="write a 3 line summary on the following text./n {text}",
    input_variables=["text"]
)

# The chain runs template1 -> model -> parser extracts string -> template2 -> model -> parser extracts string
chain=template1 | model | parser | template2 | model | parser

# Run the chain starting with the topic "black hole"
result=chain.invoke({"topic": "black hole"})
print("Summary: ", result)