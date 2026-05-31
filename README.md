# LangChain Tutorials

This repository contains basic implementations of various LangChain concepts, models, prompts, and chains.

## Project Structure

- **[Chains/](./Chains/README.md)**: Contains examples of different types of LangChain runnables. See its [dedicated README](./Chains/README.md) for details.
- **Model/**: Example integrations with various LLM providers (e.g., HuggingFace, Google Generative AI).
- **Outputs/**: Examples of utilizing different Output Parsers, such as `StructuredOutputParser`.
- **Prompts/**: Examples demonstrating the usage of prompt templates, chat history, and variables.

## Getting Started

1. Create a `.env` file at the root of the project with your API keys:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   GOOGLE_API_KEY=your_key_here
   ```
2. Install dependencies (make sure your virtual environment is active):
   ```bash
   pip install -r req.txt
   ```
3. Run any of the examples directly using Python:
   ```bash
   python Chains/parallel_chain.py
   ```
