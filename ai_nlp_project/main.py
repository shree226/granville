import os
import json
import requests
import streamlit as st
from modules.content_generator import ContentGenerator
from modules.content_refiner import ContentRefiner


def load_config():
    config_path = os.getenv('CONFIG_PATH', '/workspaces/granville/ai_nlp_project/config.json')
    with open(config_path) as f:
        return json.load(f)

config = load_config()

api_key = 'AIzaSyAvdw9a1RiOTpaVEfzXU5edP3e83hcf_8E'  
if api_key is None:
    raise ValueError("API key is missing in config.json")

generator = ContentGenerator(api_key)
refiner = ContentRefiner()

st.title("AI Educational Content Generator")


topic_input = st.text_input("Enter the topic:")
grade_level_input = st.selectbox(
    "Select the grade level:", 
    ["Toddler", "Middle School", "High School", "Undergraduate", "Graduate"]
)

if st.button("Generate"):
    with st.spinner("Generating content..."):
        prompt = f"Generate educational content about {topic_input} for {grade_level_input}."
        content = generator.generate_content(prompt)

    if config.get('refine_content', False): 
        refined_content = refiner.refine_content(content)
    else:
        refined_content = content

    
    st.subheader("Generated Content")  
    st.text(refined_content)
