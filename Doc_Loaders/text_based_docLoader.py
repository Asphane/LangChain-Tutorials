from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader

load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

prompt=PromptTemplate(
    template='write a joke about: {topic}',
    input_variables=['topic']
)

loader=TextLoader('Doc_Loaders/text.txt')

docs=loader.load()

# print(docs)
# print(len(docs))
chain=prompt | model | parser

print(chain.invoke({'topic': docs[0].page_content}))
