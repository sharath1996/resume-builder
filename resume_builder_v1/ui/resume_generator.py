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
        local_list_tempalates = self._get_templates()
        local_str_template = st.selectbox("Select Template", local_list_tempalates, index=None)
        local_button_preview = st.button("Preview Resume")
        if local_button_preview:
            st.info("Not so early!! Please wait until we spin this up for you later!!!!")
        
    
    def _get_templates(self):
        local_list_templates = [
            "Indian Resume",
            "US Resume",
            "European Resume",
            "UK Resume",
        ]
        return local_list_templates