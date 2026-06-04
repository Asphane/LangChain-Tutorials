# Currency Converter Agent

This folder contains a Jupyter Notebook (`note.ipynb`) that demonstrates how to build a LangChain-based autonomous agent capable of currency conversion.

## Overview
- **Custom Tools:** Shows how to use the `@tool` decorator to create custom tools like `get_conversion_factor` (using the ExchangeRate-API) and `convert` (which calculates the final amount).
- **Sequential Tool Calling:** Demonstrates how to pass injected arguments between tools and handle the outputs.
- **LLM Binding:** Showcases binding tools to a HuggingFace endpoint (`Qwen/Qwen2.5-72B-Instruct`) and parsing its tool calls.
