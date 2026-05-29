<div align="center">
  <img src="https://raw.githubusercontent.com/hwchase17/langchain/master/docs/static/img/langchain_logo.png" alt="LangChain Logo" width="200"/>
  <h1>🦜🔗 LangChain Tutorials</h1>
  <p><i>A practical, hands-on repository for exploring Large Language Models, Embeddings, and AI tools using LangChain.</i></p>

  [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](#)
  [![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-green.svg)](#)
  [![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%20|%20GPT--4-orange.svg)](#)
  [![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue.svg)](#)
  [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Models-yellow.svg)](#)
</div>

---

## 🌟 Overview

Welcome to the **LangChain Tutorials** repository! This project serves as a comprehensive playground to experiment with LangChain integrations, including API interactions with state-of-the-art LLMs, generating vector embeddings, and performing semantic search and document similarity.

## 📂 Project Structure

This repository is organized into distinct modules based on functionality:

### 💬 Chat Models (`/Chat_Models`)
Learn how to initialize and converse with various Chat Models using LangChain.
- **`chat_openAI.py`**: Interacting with OpenAI's `gpt-3.5-turbo`.
- **`chat_gemini.py`**: Connecting to Google's powerful `gemini-1.5-flash` model.
- **`chat_hf_api.py`**: Using open-source models (like Qwen) via the Hugging Face Serverless API.

### 🧠 LLMs (`/LLMs`)
- **`llm_demo.py`**: Basic setup for traditional text-completion Language Models.

### 🧩 Embedded Models & Similarity (`/Embedded Models`)
Explore vector representations of text and how to measure semantic closeness.
- **`embedding_openai.py`**: Generating text embeddings using OpenAI's `text-embedding-3-large`.
- **`embedding_hf.py`**: Local open-source embeddings using Hugging Face `sentence-transformers`.
- **`doc_similarity.py`**: A practical script demonstrating **Semantic Search** using Cosine Similarity on a dataset of cricketers!

### 🛠️ Utilities
- **`list_models.py`**: Utility to list available Google Gemini models.
- **`req.txt`**: Complete list of Python dependencies.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Asphane/LangChain-Tutorials.git
cd LangChain-Tutorials
```

### 2. Set up the Environment
Create a virtual environment and install the required packages:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r req.txt
```

### 3. Configure API Keys
Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY="your-openai-api-key"
GOOGLE_API_KEY="your-google-api-key"
HF_TOKEN="your-huggingface-token"
```
> **Note:** The `.env` file is excluded from Git tracking for your security. Never commit your API keys!

---

## 💻 Usage Examples

**Testing Document Similarity:**
Run the similarity script to see how the code matches a query (e.g., "tell me about bumrah") to the most relevant document:
```bash
python "Embedded Models/doc_similarity.py"
```

**Testing a Chat Model:**
```bash
python "Chat_Models/chat_openAI.py"
```

---

## 🤝 Contributing
Feel free to open issues or submit pull requests if you have ideas for new tutorials, better implementations, or bug fixes!

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
