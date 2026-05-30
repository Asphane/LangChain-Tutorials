# 📦 LangChain Outputs & Schema Modeling (TypedDict)

Welcome to the **Outputs and Schema Modeling** module! This directory focuses on defining and managing structured schemas and type-safe dictionary patterns, which are essential for parsing LLM outputs, defining LangChain agent states, and modeling API responses.

## 📁 Directory Contents

### `typedict_practice.py`
A comprehensive, hands-on practice script demonstrating the utilization of Python's `TypedDict` for type safety and dictionary validation.
- **Basic TypedDict**: Declaring structured dictionaries where all fields are required by default.
- **Optional Fields (`total=False`)**: Allowing dictionaries to be created with any subset of the defined keys.
- **Selective Optional Fields (`NotRequired`)**: Marking specific individual fields as optional while keeping others required.
- **Nested TypedDicts**: Structuring complex hierarchical objects.
- **Lists in TypedDict**: Embedding collections inside typed schemas.
- **TypedDict Inheritance**: Extending schema definitions cleanly.
- **Real-World API Modeling**: Complete examples simulating:
  - Weather API responses with optional rainfall metrics.
  - GitHub User Profile data.
  - E-commerce Product representations with discount variables.
- **LangChain Structured Output Schemas**:
  - `ResumeAnalysis`: Schema for extracting candidate information (skills, experience, email, recommendation) using Annotated types.
  - `ProductReview` & `MovieReview`: Rating, sentiment, and reviewer extraction patterns.
  - `Review`: Extracting key themes, summary, pros, cons, and sentiments from text review comments.
- **Interview revision sheet**: Synthesized cheat sheet summarizing rules, optional keys (`NotRequired`, `total=False`), `Annotated` descriptions, and `Literal` restrictions.

---

## 🚀 Getting Started

To run the `TypedDict` practice file, ensure you have Python 3.8+ installed (or activate your virtual environment) and execute:

```bash
python Outputs/typedict_practice.py
```

---

## 💡 Why use TypedDict in LangChain?

1. **Structured Outputs**: Helps map incoming JSON outputs from LLMs directly into structured Python objects with static analysis support using `model.with_structured_output(SchemaName)`.
2. **State Management**: Commonly used in LangGraph to define the input, output, and internal state of agent workflows.
3. **API Integration**: Simplifies validation of parameters sent to and received from external service APIs.
4. **Annotated Metadata**: Enables embedding field descriptions using `Annotated[Type, "description"]` that LLMs leverage as prompt instructions during structured extraction.
