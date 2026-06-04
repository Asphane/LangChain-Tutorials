<div align="center">
  <h1>🦜🔗 LangChain Tutorials & Explorations</h1>
  <p><i>A comprehensive, hands-on repository exploring the power of LangChain.</i></p>
</div>

---

Welcome to the **LangChain Tutorials** repository! 🚀 This project contains structured, modular implementations of various LangChain core concepts—ranging from basic models and prompt templates to advanced chains, custom tools, and full autonomous agents.

## 📁 Repository Structure

We've organized the repository into clear, focused directories. Dive into any folder to see dedicated examples and tutorials:

- **🤖 [Model/](./Model/)**: Examples of integrating and chatting with various LLM providers (e.g., HuggingFace, OpenAI, Google Generative AI).
- **📝 [Prompts/](./Prompts/)**: Learn to craft dynamic prompts, manage chat history, and utilize `PromptTemplates`.
- **⛓️ [Chains/](./Chains/)**: Explore LangChain's Runnables (LCEL), including Sequential, Parallel, and Conditional chains. See its [dedicated README](./Chains/README.md).
- **🛠️ [Tools/](./Tools/)**: Learn how to build and invoke custom tools that give LLMs real-world agency. Includes examples of the `@tool` decorator.
- **📄 [Doc_Loaders/](./Doc_Loaders/)**: Ingest data from anywhere! Examples of loading unstructured text, CSVs, and PDFs.
- **✂️ [Text_Splitters/](./Text_Splitters/)**: Techniques for chunking and splitting documents effectively for downstream tasks.
- **🗃️ [Vector_Stores/](./Vector_Stores/)**: Using vector databases (like Chroma) to store embeddings for fast semantic search.
- **🔍 [Retrievers/](./Retrievers/)**: Interfaces that fetch relevant context given a user's unstructured query.
- **📤 [Outputs/](./Outputs/)**: Parse raw LLM output into structured formats like JSON, Pydantic models, or typed dictionaries.

## 🌟 Highlighted Project

### 💱 [Currency Converter Agent](./currency_converter.ipynb/)
A standalone Jupyter Notebook project showcasing a complete **autonomous agent**. It demonstrates:
- Building custom LangChain tools connected to live external APIs.
- Real-time tool injection and sequential tool calling.
- Complex agentic loops where the model reasons, fetches a conversion rate, and uses math tools to provide an accurate answer.

---

## 🚀 Getting Started

Follow these steps to set up the repository on your local machine:

**1. Clone the repository:**
```bash
git clone https://github.com/Asphane/LangChain-Tutorials.git
cd LangChain-Tutorials
```

**2. Setup API Keys:**
Create a `.env` file at the root of the project to store your secure credentials:
```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
GOOGLE_API_KEY=your_google_key_here
```

**3. Install Dependencies:**
Ensure your virtual environment is active, then install the required packages:
```bash
pip install -r req.txt
```

**4. Run an Example!**
Fire up any of the Python scripts or Jupyter Notebooks to see LangChain in action. For example:
```bash
python Chains/parallel_chain.py
```

<div align="center">
  <p><i>Happy Building! 🛠️✨</i></p>
</div>
