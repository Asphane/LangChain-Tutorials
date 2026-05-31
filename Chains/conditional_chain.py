from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
import grandalf

load_dotenv()

model1=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

parser=StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description="sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1=PromptTemplate(
    template='write a feedback for this smartphone.\n {text} \n {format_instructions}',
    input_variables=['text'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classifier_chain=prompt1 | model1 | parser2

prompt2=PromptTemplate(
    template='write an appropriate response for this positive feedback.\n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='write an appropriate response for this negative feedback.\n {feedback}',
    input_variables=['feedback']
)

prompt4=PromptTemplate(
    template='write an appropriate response for this neutral feedback.\n {feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model1 | parser),
    (lambda x: x.sentiment == 'neutral', prompt4 | model1 | parser),
    RunnableLambda(lambda x: "Invalid sentiment")
)

chain=classifier_chain | branch_chain

print("Feedback: ", chain.invoke({"text": "The smartphone has a worst battery life."}))