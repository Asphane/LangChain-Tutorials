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

### `pydantic_practice.py`
A complete, hands-on practice script demonstrating the utilization of Pydantic (`BaseModel`) for runtime data validation, type conversion, and advanced constraint enforcement.
- **BaseModel & Serialization**: Creating models, parsing, and exporting to dicts (`model_dump()`) or JSON (`model_dump_json()`).
- **Data Types & Validation**: Type conversion, default values, optional fields, and handling validation errors.
- **Field Constraints (`Field`)**: Specifying metadata, default factories, and value constraints (e.g., `gt`, `ge`, `lt`, `le`).
- **Complex Structures**: Nested Pydantic models and models within lists.
- **Field Validators (`@field_validator`)**: Writing simple validators, cleaners (stripping/case adjustments), and schema checks (like emails).
- **LangChain Structured Output Modeling**:
  - `ResumeAnalysis`: Schema modeling candidates with structured fields and nested collections.
  - `ProductReview` & `SentimentAnalysis`: Sentiment parsing with confidence levels.
  - `Review`: Advanced rating and summary schema mapping.
- **Interview revision sheet**: Cheat sheet summarizing BaseModel usage, validation helpers, and comparison between TypedDict (static) and Pydantic (runtime).

---

## 🚀 Getting Started

To run either of the practice files, ensure you have Python 3.8+ and Pydantic installed (or activate your virtual environment) and execute:

```bash
# To run TypedDict examples
python Outputs/typedict_practice.py

# To run Pydantic examples
python Outputs/pydantic_practice.py
```

---

## 💡 Why use TypedDict & Pydantic in LangChain?

1. **Structured Outputs**: Helps map incoming JSON outputs from LLMs directly into structured Python objects with static analysis and runtime validation support using `model.with_structured_output(SchemaName)`.
2. **State Management**: Commonly used in LangGraph to define the input, output, and internal state of agent workflows.
3. **API Integration**: Simplifies validation of parameters sent to and received from external service APIs.
4. **Annotated Metadata / Descriptions**: Enables embedding field descriptions using `Annotated[Type, "description"]` (in TypedDict) or `Field(description="description")` (in Pydantic) that LLMs leverage as prompt instructions during structured extraction.
5. **TypedDict vs Pydantic**:
   - **TypedDict**: Static typing only (no runtime validation overhead). Best for lightweight schemas and defining simple dictionaries or LangGraph state models where runtime enforcement isn't needed.
   - **Pydantic**: Robust runtime data validation, automatic type conversion, and advanced constraint checks. Highly recommended for production-grade LangChain apps, LLM output parser targets, and FastAPI integrations.
