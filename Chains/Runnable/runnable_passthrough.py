"""
This script shows how to use RunnablePassthrough to pass data along without changing it.
It generates a joke, then passes that exact joke to one branch and an explanation of the joke to another.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

# Load environment variables
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

# First, we create a chain just to generate a joke
joke_gen_chain=RunnableSequence(prompt1, model, parser)

# Next, we create a parallel chain that does two things:
# 1. 'joke' branch uses RunnablePassthrough() which simply passes the raw joke string forward as-is.
# 2. 'explanation' branch runs the joke through prompt2 and the model to get a new explanation.
parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

# Combine everything: First generate the joke, then run the parallel chain on it
final_chain=RunnableSequence(joke_gen_chain, parallel_chain)

# Run the complete chain
res=final_chain.invoke({'topic': 'cricket'})
print()
print(res['joke'], "\n", res['explanation'])
