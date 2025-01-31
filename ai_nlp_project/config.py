import os
import json
import requests
import streamlit as st
from modules.content_generator import ContentGenerator
from modules.content_refiner import ContentRefiner

# Load configuration
def load_config():
    config_path = os.getenv('CONFIG_PATH', '/workspaces/granville/ai_nlp_project/config.json')
    with open(config_path) as f:
        return json.load(f)

config = load_config()

# Initialize components
api_key = 'AIzaSyAvdw9a1RiOTpaVEfzXU5edP3e83hcf_8E'  # Get API key from config
if api_key is None:
    raise ValueError("API key is missing in config.json")

generator = ContentGenerator(api_key)
refiner = ContentRefiner()

st.title("AI Educational Content Generator")

# Input fields
topic_input = st.text_input("Enter the topic:")
grade_level_input = st.selectbox(
    "Select the grade level:", 
    ["Toddler", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Middle School", "High School", "Undergraduate", "Graduate"]
)

if st.button("Generate"):
    with st.spinner("Generating content..."):
        prompt = f"Generate educational content about {topic_input} for {grade_level_input}."
        content = generator.generate_content(prompt)

    if config.get('refine_content', False):  # Use .get with default
        refined_content = refiner.refine_content(content)
    else:
        refined_content = content

    # Display generated content as plain text
    st.subheader("Generated Content")  
    st.text(refined_content)  # Using st.text() for normal/plain text display
