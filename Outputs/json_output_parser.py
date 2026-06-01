"""
This script shows how to force the model to respond in raw JSON format.
This is incredibly useful when you want to pass the data to another program or API.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

# Set up the JsonOutputParser which knows how to ask the model for JSON
parser=JsonOutputParser()

# We inject parser.get_format_instructions() so the model knows exactly how to format the JSON
template=PromptTemplate(
    template="write a 5 points report on {topic}. /n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain=template | model | parser
result=chain.invoke({"topic": "black hole"})
print("5 points Report: ", result)