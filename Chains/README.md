# LangChain Chains

This directory contains examples of different types of LangChain runnables and chain combinations. Each script demonstrates a unique way to combine prompts, models, and parsers.

## Available Chains

- **[`simple_chain.py`](./simple_chain.py)**: Demonstrates a basic, linear chain consisting of `PromptTemplate -> ChatHuggingFace -> StrOutputParser`. This is the fundamental building block of LangChain execution.

- **[`sequential_chain.py`](./sequential_chain.py)**: Shows how to run multiple steps in a sequence where the output of one step becomes the input of the next.

- **[`parallel_chain.py`](./parallel_chain.py)**: Highlights the use of `RunnableParallel`. It runs multiple chains at the same time and combines their outputs into a single dictionary, which is then passed to a final merged chain. Also demonstrates visualizing the execution graph.

- **[`conditional_chain.py`](./conditional_chain.py)**: Demonstrates conditional routing, allowing the chain to take different paths or execute different logic based on the input or intermediate outputs.

## Usage

You can run any of these chains directly from the root of the project. For example:
```bash
python Chains/parallel_chain.py
```
