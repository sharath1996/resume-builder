import streamlit as st
from .tabs.details import ProfileBasicDetails
from .tabs.certifications import CertificationUI
from .tabs.papers import PapersUI
from .tabs.patents import PatentsUI
from .tabs.talks import TalksUI
from .tabs.education import EducationUI
from .tabs.work_experience import WorkExperienceUI
from .tabs.academic_projects import AcademicProjectsUI
from .tabs.professional_projects import ProfessionalProjectsUI

class ProfileUI:

    def __init__(self, param_str_profileName:str):
        st.set_page_config(page_title="Resume Assistant" , layout="wide")
        self._str_profileName:str = param_str_profileName
    
    def run(self):
        
        st.title(f"Hey :blue[{self._str_profileName}...]")
        local_list_tabs = ['About You', 'Work Experience', 'Professional Projects','Education', 'Academic Projects', 'Certifications', 'Papers', 'Patents', 'Talks']

        local_list_stTabs = st.tabs(local_list_tabs)

        # About you
        with local_list_stTabs[0]:
            st.header("About You")
            local_obj_profileDetails = ProfileBasicDetails(self._str_profileName)
            local_obj_profileDetails.run()
        
        with local_list_stTabs[1]:
            st.header("Work Experience")
            local_obj_workExperience = WorkExperienceUI(self._str_profileName)
            local_obj_workExperience.run()
        
        with local_list_stTabs[2]:
            st.header("Professional projects")
            local_obj_professionalExperience = ProfessionalProjectsUI(self._str_profileName)
            local_obj_professionalExperience.run()

        with local_list_stTabs[3]:
            st.header("Education")
            local_obj_education = EducationUI(self._str_profileName)
            local_obj_education.run()
        
        with local_list_stTabs[4]:
            st.header("Academic Projects")
            local_obj_academicProjects = AcademicProjectsUI(self._str_profileName)
            local_obj_academicProjects.run()

        with local_list_stTabs[5]:
            st.header("Certifications")
            local_obj_certifications = CertificationUI(self._str_profileName)
            local_obj_certifications.run()
        
        with local_list_stTabs[6]:
            st.header("Papers")
            local_obj_papers = PapersUI(self._str_profileName)
            local_obj_papers.run()
            
        
        with local_list_stTabs[7]:
            st.header("Patents")
            local_obj_patents =PatentsUI(self._str_profileName)
            local_obj_patents.run()
        
        with local_list_stTabs[8]:
            st.header("Talks")
            local_obj_talks = TalksUI(self._str_profileName)
            local_obj_talks.run()
            