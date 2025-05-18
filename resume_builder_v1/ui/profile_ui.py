import streamlit as st
from .tabs.details import ProfileBasicDetails
from .tabs.certifications import CertificationUI
from .tabs.papers import PapersUI
from .tabs.patents import PatentsUI

class ProfileUI:

    def __init__(self, param_str_profileName:str):
        self._str_profileName:str = param_str_profileName
    
    def run(self):
        
        local_list_tabs = ['About You', 'Work Experience', 'Education', 'Certifications', 'Papers', 'Patents', 'Talks']

        local_list_stTabs = st.tabs(local_list_tabs)

        # About you
        with local_list_stTabs[0]:
            st.header("About You")
            local_obj_profileDetails = ProfileBasicDetails(self._str_profileName)
            local_obj_profileDetails.run()
        
        with local_list_stTabs[1]:
            st.header("Work Experience")
            
        
        with local_list_stTabs[2]:
            st.header("Education")
        
        with local_list_stTabs[3]:
            st.header("Certifications")
            local_obj_certifications = CertificationUI(self._str_profileName)
            local_obj_certifications.run()
        
        with local_list_stTabs[4]:
            st.header("Papers")
            local_obj_papers = PapersUI(self._str_profileName)
            local_obj_papers.run()
            
        
        with local_list_stTabs[5]:
            st.header("Patents")
            local_obj_patents =PatentsUI(self._str_profileName)
            local_obj_patents.run()
        
        with local_list_stTabs[6]:
            st.header("Talks")