"""
This file is a comprehensive practice notebook for LangChain.
It covers everything from basic model calls to complex LCEL chains and RAG simulations.
Each section demonstrates a different LangChain concept with clear examples.
"""
# LangChain Chains Complete Notes & Practice File
"""
LANGCHAIN CHAINS COMPLETE PRACTICE FILE

Topics Covered:

1. ChatOpenAI
2. Prompt Templates
3. LCEL
4. RunnableSequence
5. StrOutputParser
6. invoke()
7. RunnablePassthrough
8. RunnableParallel
9. Dictionary Runnables
10. Basic RAG Pattern

Useful For:
- LangChain
- RAG
- AI Applications
- Agents
- LangGraph
"""

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableParallel
)

load_dotenv()


# ============================================================
# 1. BASIC MODEL CALL
# ============================================================

model = ChatOpenAI()

result = model.invoke(
    "What is the capital of India?"
)

print(result.content)


# ============================================================
# 2. PROMPT TEMPLATE
# ============================================================

prompt = ChatPromptTemplate.from_template(
    "Tell me a joke about {topic}"
)

formatted_prompt = prompt.invoke(
    {
        "topic": "cats"
    }
)

print(formatted_prompt)


# ============================================================
# 3. FIRST CHAIN
# ============================================================

chain = (
    prompt
    | model
)

response = chain.invoke(
    {
        "topic": "cats"
    }
)

print(response.content)


# ============================================================
# 4. STR OUTPUT PARSER
# ============================================================

chain = (
    prompt
    | model
    | StrOutputParser()
)

response = chain.invoke(
    {
        "topic": "cats"
    }
)

print(response)
print(type(response))


# ============================================================
# 5. TRANSLATION CHAIN
# ============================================================

translation_prompt = ChatPromptTemplate.from_template(
    "Translate {word} to French"
)

translation_chain = (
    translation_prompt
    | model
    | StrOutputParser()
)

result = translation_chain.invoke(
    {
        "word": "hello"
    }
)

print(result)


# ============================================================
# 6. EXPLANATION CHAIN
# ============================================================

explain_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 3 lines"
)

explain_chain = (
    explain_prompt
    | model
    | StrOutputParser()
)

result = explain_chain.invoke(
    {
        "topic": "LangChain"
    }
)

print(result)


# ============================================================
# 7. RUNNABLE PASSTHROUGH
# ============================================================

passthrough = RunnablePassthrough()

result = passthrough.invoke(
    "Hello World"
)

print(result)


# Input
# "Hello World"

# Output
# "Hello World"


# ============================================================
# 8. DICTIONARY RUNNABLE
# ============================================================

chain = {
    "question": RunnablePassthrough()
}

result = chain.invoke(
    "What is Python?"
)

print(result)


# Output:
#
# {
#   "question": "What is Python?"
# }


# ============================================================
# 9. SUMMARY CHAIN
# ============================================================

summary_prompt = ChatPromptTemplate.from_template(
    """
    Summarize the following text:

    {text}
    """
)

summary_chain = (
    summary_prompt
    | model
    | StrOutputParser()
)


# ============================================================
# 10. KEYWORD CHAIN
# ============================================================

keyword_prompt = ChatPromptTemplate.from_template(
    """
    Extract 5 keywords from:

    {text}
    """
)

keyword_chain = (
    keyword_prompt
    | model
    | StrOutputParser()
)


# ============================================================
# 11. RUNNABLE PARALLEL
# ============================================================

parallel_chain = RunnableParallel(
    summary=summary_chain,
    keywords=keyword_chain
)

result = parallel_chain.invoke(
    {
        "text": """
        LangChain is a framework for building
        LLM applications.
        """
    }
)

print(result)


# Example Output
#
# {
#   "summary": "...",
#   "keywords": "..."
# }


# ============================================================
# 12. JOKE CHAIN
# ============================================================

joke_prompt = ChatPromptTemplate.from_template(
    "Write a joke about {topic}"
)

joke_chain = (
    joke_prompt
    | model
    | StrOutputParser()
)


# ============================================================
# 13. POEM CHAIN
# ============================================================

poem_prompt = ChatPromptTemplate.from_template(
    "Write a short poem about {topic}"
)

poem_chain = (
    poem_prompt
    | model
    | StrOutputParser()
)


# ============================================================
# 14. JOKE + POEM PARALLEL
# ============================================================

creative_chain = RunnableParallel(
    joke=joke_chain,
    poem=poem_chain
)

result = creative_chain.invoke(
    {
        "topic": "cats"
    }
)

print(result)


# Example Output
#
# {
#   "joke": "...",
#   "poem": "..."
# }


# ============================================================
# 15. RAG STYLE PATTERN
# ============================================================

# Imagine retriever returns documents

def fake_retriever(question):

    return """
    LangChain is a framework
    for building LLM applications.
    """


class FakeRetriever:

    def invoke(self, question):
        return fake_retriever(question)


retriever = FakeRetriever()


# ============================================================
# 16. UNDERSTANDING RAG FLOW
# ============================================================

question = "What is LangChain?"

rag_input = {
    "question": question,
    "context": retriever.invoke(question)
}

print(rag_input)


# Output:
#
# {
#   "question": "What is LangChain?",
#   "context": "LangChain is a framework..."
# }


# ============================================================
# 17. RAG PROMPT
# ============================================================

rag_prompt = ChatPromptTemplate.from_template(
    """
    Use the following context
    to answer the question.

    Context:
    {context}

    Question:
    {question}
    """
)

formatted_prompt = rag_prompt.invoke(
    {
        "question": "What is LangChain?",
        "context": """
        LangChain is a framework
        for building LLM applications.
        """
    }
)

print(formatted_prompt)


# ============================================================
# 18. COMPLETE RAG CHAIN (SIMULATION)
# ============================================================

rag_chain = (
    rag_prompt
    | model
    | StrOutputParser()
)

result = rag_chain.invoke(
    {
        "question": "What is LangChain?",
        "context": """
        LangChain is a framework
        for building LLM applications.
        """
    }
)

print(result)


# ============================================================
# INTERVIEW NOTES
# ============================================================

"""
1. model.invoke()
   -> Direct LLM call

2. ChatPromptTemplate
   -> Creates reusable prompts

3. LCEL
   -> LangChain Expression Language

4. |
   -> Connects components

5. prompt | model
   -> RunnableSequence

6. StrOutputParser()
   -> Converts AIMessage -> string

7. chain.invoke()
   -> Executes chain

8. RunnablePassthrough()
   -> Returns input unchanged

9. RunnableParallel()
   -> Executes multiple chains simultaneously

10. RunnableParallel Output
    -> Dictionary

11. Dictionary Runnable

    {
        "question": RunnablePassthrough(),
        "context": retriever
    }

12. RAG Pattern

    {
        "question": RunnablePassthrough(),
        "context": retriever
    }
    | prompt
    | model
    | parser

13. Prompt Variables

    {question}
    {context}

    require:

    {
        "question": value,
        "context": value
    }

14. Without Parser

    Output:
    AIMessage

15. With StrOutputParser

    Output:
    str
"""