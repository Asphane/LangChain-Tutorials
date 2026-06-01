"""
This script demonstrates how to create a "conditional chain" or a branch in LangChain.
It analyzes the sentiment of a review and then chooses a different response path
based on whether the sentiment was positive, negative, or neutral.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
import grandalf

# Load API keys
load_dotenv()

model1=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

# Define our desired output format using Pydantic (to force the model to output a specific JSON structure)
class feedback(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description="sentiment of the feedback")

# Create a parser that ensures the output matches our Pydantic model
parser2=PydanticOutputParser(pydantic_object=feedback)

# Step 1: Create a prompt to classify the sentiment of the input text
prompt1=PromptTemplate(
    template='write a feedback for this smartphone.\n {text} \n {format_instructions}',
    input_variables=['text'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classifier_chain=prompt1 | model1 | parser2

# Step 2: Define the different templates based on the sentiment
prompt2=PromptTemplate(
    template='write an appropriate response for this positive feedback.\n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='write an appropriate response for this negative feedback.\n {feedback}',
    input_variables=['feedback']
)

prompt4=PromptTemplate(
    template='write an appropriate response for this neutral feedback.\n {feedback}',
    input_variables=['feedback']
)

# Step 3: Create a RunnableBranch which acts like an IF-ELSE statement
# It checks the 'sentiment' field and runs the corresponding prompt+model chain
branch_chain=RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model1 | parser),
    (lambda x: x.sentiment == 'neutral', prompt4 | model1 | parser),
    RunnableLambda(lambda x: "Invalid sentiment") # Fallback case
)

# Step 4: Combine the classifier and the branching logic into one massive chain
chain=classifier_chain | branch_chain

# Test the chain with a negative review
print("Feedback: ", chain.invoke({"text": "The smartphone has a worst battery life."}))