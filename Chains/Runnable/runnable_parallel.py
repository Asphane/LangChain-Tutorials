"""
This script shows how to run two different chains simultaneously (in parallel).
It generates a tweet and a LinkedIn caption for the same topic at the exact same time.
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

# Load environment variables
load_dotenv()

model=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

# Define two different prompts (one for a tweet, one for LinkedIn)
prompt1=PromptTemplate(
    template='write a concise tweet on the: {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a concise linkedin caption on the: {topic}',
    input_variables=['topic']
)

# Run both the tweet generator and the LinkedIn generator in parallel
chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

print()
print("Generating content in parallel...")
# Run the parallel chain
result=chain.invoke({'topic': 'effects of vibecoding'})

# The result is a dictionary containing both the tweet and the linkedin caption
print("The following captions are\n", result['linkedin'])
