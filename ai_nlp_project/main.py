import os
import json
import requests
import streamlit as st
from modules.content_generator import ContentGenerator
from modules.content_refiner import ContentRefiner



    
def load_config():
    # Correct path to the config.json file in the modules folder
    config_path = os.path.join(os.path.dirname(__file__), 'modules', 'config.json')
    try:
        with open(config_path) as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("config.json file not found.")
        return {}
    except json.JSONDecodeError:
        st.error("Error decoding config.json file.")
        return {}


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
