from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='write a concise tweet on the: {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a concise linkedin caption on the: {topic}',
    input_variables=['topic']
)

chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

print()
print("Generating content in parallel...")
result=chain.invoke({'topic': 'effects of vibecoding'})
print("The following captions are\n", result['linkedin'])
