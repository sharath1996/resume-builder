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
from .resume_generator import JobAppUI
from ..api.profile_apis import ProfileAPIs

class ProfileUI:

    def __init__(self):
        st.set_page_config(page_title="Resume Assistant" , layout="wide")
        if "profileName" not in st.session_state:
            st.session_state["profileName"] = None
        
        if "task" not in st.session_state:
            st.session_state["task"] = None
        
        self._str_profileName = st.session_state["profileName"]
    
    def run(self):
        
        self.side_bar()
        if self._str_profileName == None:
            st.title("Please select a profile")
            st.warning("Please select a profile from the sidebar")
        else: 
            if st.session_state["task"] == "Job Applications":
                self.run_job_applications()
            elif st.session_state["task"] == "Profile":
                self.run_profile_page()

    
    def side_bar(self):
        with st.sidebar:
            
            local_list_profileNames = ProfileAPIs().read_all_profiles()
            lcoal_str_profileSelected = st.selectbox("Select Profile", local_list_profileNames, index=None)

            local_list_tasks = ["Profile", "Job Applications"]
            local_str_taskSelected = st.selectbox("Select Task", local_list_tasks, index=None)
            
            local_column_button = st.columns([1, 2])
            local_button_login = local_column_button[0].button("Login")
            
            if local_button_login:

                if lcoal_str_profileSelected:
                    st.session_state["profileName"] = lcoal_str_profileSelected
                    st.session_state["task"] = local_str_taskSelected
                    st.rerun()

            with local_column_button[1].popover("Create New"):
                
                local_str_newProfileName = st.text_input("Enter Profile Name", key="new_profile_name")
                local_button_create = st.button("Create Profile", key="create_profile_btn")
                
                if local_button_create:
                    if local_str_newProfileName and local_str_newProfileName.strip() != "":
                        try:
                            ProfileAPIs().create(local_str_newProfileName)
                        except Exception as e:
                            st.error(f"Error creating profile: {e}")
                            return 
                        st.session_state["profileName"] = local_str_newProfileName
                        st.success(f"Profile {local_str_newProfileName} created successfully")
                        st.rerun()
                    else:
                        st.error("Please enter a valid profile name")

    def run_job_applications(self):
        st.title(f"Hey :blue[{self._str_profileName}...]")
        JobAppUI().run()

    def run_profile_page(self):
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
        
            