from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch

load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

def count(text):
    return len(text.split())

prompt1=PromptTemplate(
    template='write a detailed note on the topic: {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a summary on the topic: {topic}',
    input_variables=['topic']
)

detailed_note_chain=RunnableSequence(prompt1, model, parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

chain=RunnableSequence(detailed_note_chain, branch_chain)
res=chain.invoke({'topic': 'coding'})

print(res)