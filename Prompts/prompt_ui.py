"""
This script builds a simple web UI using Streamlit to generate research paper summaries.
It loads a saved PromptTemplate and uses the Gemini model to generate the text based on user selections.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, load_prompt
import os

# Load environment variables
load_dotenv()
# Set up the Gemini model
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Set the title of our Streamlit web app
st.header("Research Paper Summarizer")

# Create dropdown menus in the UI for the user to make selections
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template="""
#         Please summarize the research paper titled "{paper_input}" with the following specifications:
#         Explanation Style: {style_input}  
#         Explanation Length: {length_input}  
#         1. Mathematical Details:  
#         - Include relevant mathematical equations if present in the paper.  
#         - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
#         2. Analogies:  
#         - Use relatable analogies to simplify complex ideas.  
#         If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
#         Ensure the summary is clear, accurate, and aligned with the provided style and length.
#         """,
#         input_variables=['paper_input', 'style_input','length_input'],
#         validate_template=True
# )

# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })

# Load the previously saved prompt template from our JSON file
template_path = os.path.join(os.path.dirname(__file__), "research_paper_summary_template.json")
template=load_prompt(template_path)

# Wait for the user to click the "Generate Summary" button
if st.button("Generate Summary"):
    # Show a loading spinner while waiting for the model
    with st.spinner("Generating summary..."):
        # Chain the template and the model together using the pipe (|) operator
        chain=template | model
        # Pass the user's UI selections into the chain
        response = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })
        # Display the final summary on the screen
        st.subheader("Summary:")
        st.write(response.content)