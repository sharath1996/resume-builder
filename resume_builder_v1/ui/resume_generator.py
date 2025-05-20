import streamlit as st
class ResumeGenerator:

    def __init__(self):
        ...
    
    def view(self):
        ...
    
    def view_preview_resume(self, param_str_jobDescription, param_str_profileName:str):
        ...

    def generate_pdf_resume(self, param_dict_jsonResume:dict):
        ...
    
class JobAppUI:

    def __init__(self):
        ...
    
    def run(self):
        local_str_jobDescription = st.text_area("Job Description", height=300)
        local_str_instructions = st.text_area("Instructions")
        local_button_generate = st.button("Generate Resume")
        if local_button_generate:
            st.info("Not so early!! Please wait until we spin this up for you later!!!!")