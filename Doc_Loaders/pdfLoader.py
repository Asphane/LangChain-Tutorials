# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("Doc_Loaders/Bisakh Patra Resume ML.pdf")

docs=loader.load()

print(docs[0].page_content)