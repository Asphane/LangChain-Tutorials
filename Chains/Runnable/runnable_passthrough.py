from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='generate a joke on: {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a explanation of the joke : {text}',
    input_variables=['text']
)

joke_gen_chain=RunnableSequence(prompt1, model, parser)

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain=RunnableSequence(joke_gen_chain, parallel_chain)

res=final_chain.invoke({'topic': 'cricket'})
print()
print(res['joke'], "\n", res['explanation'])
