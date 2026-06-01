from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model=GoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='write a detailed analysis on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write the advantages of joining in {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result=chain.invoke({'topic': 'faang'})

print("Analysis: ", result)