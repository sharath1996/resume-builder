import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import ProfessionalProject

class ProfessionalProjectsUI:

    def __init__(self, param_str_profileName:str):
        self._obj_profileAPIs = ProfileAPIs()
        self._str_profileName = param_str_profileName
    
    def run(self):
        local_list_professionalProjects = self._read_all_professional_projects()
        if len(local_list_professionalProjects) == 0:
            st.markdown("### No professional projects found!")
        
        else:
            for local_obj_professionalProject in local_list_professionalProjects:
                with st.expander(local_obj_professionalProject.str_projectTitle ):
                    local_obj_professionalProject.str_projectTitle = st.text_input("Project Title", value=local_obj_professionalProject.str_projectTitle)
                    local_obj_professionalProject.str_projectContents = st.text_area("Detailed Information about the project in Markdown", value=local_obj_professionalProject.str_projectContents)
                    local_obj_professionalProject.str_highlights = st.text_area("Highlights of this project", local_obj_professionalProject.str_highlights)
                    
                    local_str_currentWorkExperience = f'{local_obj_professionalProject.str_companyName} @ {local_obj_professionalProject.str_designation}'
                    local_list_workExperience = self._get_work_experience(self._str_profileName)
                    local_int_index = local_list_workExperience.index(local_str_currentWorkExperience)
                    local_str_selectedWorkExperience = st.selectbox("Select your work experience", local_list_workExperience, index=local_int_index, key=f"{local_obj_professionalProject.str_projectTitle}_prof_proj_exi")
                    local_list_options = local_str_selectedWorkExperience.split("@")
                    local_obj_professionalProject.str_companyName = local_list_options[0].strip()
                    local_obj_professionalProject.str_designation = local_list_options[1].strip()

            local_button_updateExistingprofessionalProject = st.button("Update Existing professional Projects")
            if local_button_updateExistingprofessionalProject:
                self._update_professional_projects(local_list_professionalProjects)
                st.rerun()
        
        local_button_addNewprofessionalProject = st.button("Add new professional project")
        if local_button_addNewprofessionalProject:
            self._add_new_professional_project()
            

    @st.fragment
    def _add_new_professional_project(self):
        
        st.markdown("#### Add new professional project")
        
        local_obj_professionalProject = ProfessionalProject()
        
        local_obj_professionalProject.str_projectTitle = st.text_input("Project Title", value=local_obj_professionalProject.str_projectTitle)
        local_obj_professionalProject.str_projectContents = st.text_area("Detailed Information about the project in Markdown", value=local_obj_professionalProject.str_projectContents)
        local_obj_professionalProject.str_highlights = st.text_area("Highlights of this project", local_obj_professionalProject.str_highlights)
        
        local_list_workExperience = self._get_work_experience(self._str_profileName)
        local_str_selectedWorkExperience = st.selectbox("Select your work experience", local_list_workExperience, index=0, key=f"{local_obj_professionalProject.str_projectTitle}_prof_proj_new")
        local_list_options = local_str_selectedWorkExperience.split("@")
        local_obj_professionalProject.str_companyName = local_list_options[0].strip()
        local_obj_professionalProject.str_designation = local_list_options[1].strip()
    

        local_button_createNewprofessionalProject = st.button("Update New professional project")
        if local_button_createNewprofessionalProject:
            self._create_new_professional_project(local_obj_professionalProject)
            st.rerun()
            
    
    def _read_all_professional_projects(self):
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        return local_obj_profile.list_professionalProjects
    
    def _update_professional_projects(self, param_list_professionalProjects:list[ProfessionalProject]):
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        local_obj_profile.list_professionalProjects = param_list_professionalProjects
        st.info("professional project modified succesfully")

    def _create_new_professional_project(self, param_obj_professionalProjects:ProfessionalProject):
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        local_obj_profile.list_professionalProjects.append(param_obj_professionalProjects)
        self._obj_profileAPIs.update(self._str_profileName, local_obj_profile)
        st.info("professional project added succesfully")

    def _get_work_experience(self, param_str_profileName:str):
        local_obj_profile = self._obj_profileAPIs.read(param_str_profileName)
        local_list_workExperience = []
        for local_obj_workExperience in local_obj_profile.list_workExperience:
            local_list_workExperience.append(f"{local_obj_workExperience.str_companyName} @ {local_obj_workExperience.str_title}")
        return local_list_workExperience