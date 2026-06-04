# LangChain Tools

This folder covers the creation and usage of Tools in LangChain (`tool_calling.ipynb`, `tools_langchain.ipynb`).

## Overview
Tools are functions that an LLM can invoke to perform specific actions or fetch external information. Topics covered include:
- **Built-in Tools:** Utilizing LangChain's pre-existing tools.
- **Custom Tool Creation:** Building bespoke functions using the `@tool` decorator or extending `BaseTool`.
- **Tool Calling:** How models determine when to call tools, pass arguments, and handle the returned data in an agentic loop.
