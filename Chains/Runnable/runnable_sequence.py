"""
This script demonstrates how to chain multiple steps together using RunnableSequence.
It passes the output of one step (an analysis) as the input to the next step (finding advantages).
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

# Load environment variables (like API keys)
load_dotenv()

# Initialize the Gemini model
model=GoogleGenerativeAI(model='gemini-2.5-flash')

# Define the first prompt (generates an analysis)
prompt1=PromptTemplate(
    template='write a detailed analysis on {topic}',
    input_variables=['topic']
)

# Define the second prompt (uses the analysis text as input)
prompt2=PromptTemplate(
    template='write the advantages of joining in {text}',
    input_variables=['text']
)

parser=StrOutputParser()

# Create a sequence: prompt1 -> model -> string -> prompt2 -> model -> string
chain=RunnableSequence(prompt1, model, parser, prompt2, model, parser)

# Run the entire sequence
result=chain.invoke({'topic': 'faang'})

print("Analysis: ", result)