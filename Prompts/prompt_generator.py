"""
This script shows how to create a detailed PromptTemplate and save it to a file.
Saving prompts to a JSON file allows you to reuse them in other scripts (like our UI).
"""
import os
from langchain_core.prompts import PromptTemplate

# Define a complex template with clear instructions and required variables
template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation Style: {style_input}  
        Explanation Length: {length_input}  
        1. Mathematical Details:  
        - Include relevant mathematical equations if present in the paper.  
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
        2. Analogies:  
        - Use relatable analogies to simplify complex ideas.  
        If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
        Ensure the summary is clear, accurate, and aligned with the provided style and length.
        """,
        input_variables=['paper_input', 'style_input','length_input'],
        validate_template=True # Ensure all variables in the template text match the input_variables list
)

# Save the created template as a JSON file in the same directory as this script
save_path = os.path.join(os.path.dirname(__file__), "research_paper_summary_template.json")
template.save(save_path)