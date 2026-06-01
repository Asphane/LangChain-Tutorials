"""
This script shows how to include custom Python functions inside a LangChain using RunnableLambda.
It generates a joke and then uses a Python function to count the number of words in the joke.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

# Load environment variables
load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

# Custom Python function to count words
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

# Chain 1: Just generates the joke
joke_gen_chain=RunnableSequence(prompt1, model, parser)

# Chain 2 (Parallel): Keeps the joke as is AND runs our custom `count` function on it
parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(), # Keeps the raw joke text
    'word_count': RunnableLambda(count) # Runs our custom python function to count the words
})

# Combine everything
chain=RunnableSequence(joke_gen_chain, parallel_chain)
res=chain.invoke({'topic': 'coding'})

# Format and print the final result using the generated outputs
final_res="""{} \n contains {} words""".format(res['joke'], res['word_count'])
print(final_res)