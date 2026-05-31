from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

chain=prompt | model | parser

result=chain.invoke({"topic": "genAI"})
print("Report: ", result)