# Runnable Chains

This directory contains examples of using LangChain Expression Language (LCEL) Runnables to create complex, composable chains. 

## Files Included

* **`runnable_sequence.py`**: Demonstrates how to chain multiple runnables together in a sequence, passing the output of one as the input to the next.
* **`runnable_parallel.py`**: Shows how to run multiple runnables concurrently on the same input and combine their outputs.
* **`runnable_lambda.py`**: Illustrates wrapping custom Python functions as Runnables within a chain, allowing arbitrary logic to be included in the pipeline.
* **`runnable_passthrough.py`**: Demonstrates passing inputs through unchanged or adding additional keys to a dictionary before passing them to the next step.
* **`runnable_branch.py`**: Shows how to add conditional logic (if-else branching) into chains based on the input.

## Getting Started

Make sure you have your `.env` file configured with the necessary API keys (like HuggingFace or Google API keys depending on the model used).
Run any of the examples directly to see the chains in action:

```bash
python runnable_sequence.py
```
