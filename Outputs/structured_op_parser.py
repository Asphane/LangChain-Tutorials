from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

response_schemas = [
    ResponseSchema(name="point1", description="First key point"),
    ResponseSchema(name="point2", description="Second key point"),
    ResponseSchema(name="point3", description="Third key point"),
    ResponseSchema(name="point4", description="Fourth key point"),
    ResponseSchema(name="point5", description="Fifth key point")
]
parser = StructuredOutputParser.from_response_schemas(response_schemas)

template=PromptTemplate(
    template="write a 5 points report on {topic}. \n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain=template | model | parser
result=chain.invoke({"topic": "black hole"})
print("5 points Report: ", result)