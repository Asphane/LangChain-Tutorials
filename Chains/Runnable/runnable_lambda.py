from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

def count(text):
    return len(text.split())

prompt1=PromptTemplate(
    template='write a joke on the topic: {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='no. of lines in the topic: {topic}',
    input_variables=['topic']
)

joke_gen_chain=RunnableSequence(prompt1, model, parser)

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(count)
})

chain=RunnableSequence(joke_gen_chain, parallel_chain)
res=chain.invoke({'topic': 'coding'})

final_res="""{} \n contains {} words""".format(res['joke'], res['word_count'])
print(final_res)