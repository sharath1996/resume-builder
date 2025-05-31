import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import AcademicProject
from datetime import datetime

class AcademicProjectsUI:

    def __init__(self, param_str_profileName:str):
        self._obj_profileAPIs = ProfileAPIs()
        self._str_profileName = param_str_profileName
    
    def run(self):
        local_list_academicProjects = self._read_all_academic_projects()
        if len(local_list_academicProjects) == 0:
            st.markdown("### No academic projects found!")
        
        else:
            for local_obj_academicProject in local_list_academicProjects:
                with st.expander(local_obj_academicProject.str_projectTitle):
                    local_obj_academicProject.str_projectTitle = st.text_input("Project Title", value=local_obj_academicProject.str_projectTitle, key = f"{local_obj_academicProject.str_projectTitle}_proj_exi")
                    local_obj_academicProject.str_projectContents = st.text_area("Detailed Information about the project in Markdown", value=local_obj_academicProject.str_projectContents, key = f"{local_obj_academicProject.str_projectTitle}_proj_exi")
                    local_obj_academicProject.str_highlights = st.text_area("Highlights of this project", local_obj_academicProject.str_highlights, key = f"{local_obj_academicProject.str_projectTitle}_proj_exi")
                    
                    local_str_currentEducation = f'{local_obj_academicProject.str_degreeName} @ {local_obj_academicProject.str_institueName}'
                    local_list_educationDegrees = self._get_education_institute(self._str_profileName)
                    local_int_index = local_list_educationDegrees.index(local_str_currentEducation)
                    local_str_selectedEducation = st.selectbox("Select your education degree", local_list_educationDegrees, index=local_int_index, key=f"{local_obj_academicProject.str_projectTitle}_ed_proj_exi")
                    local_list_options = local_str_selectedEducation.split("@")
                    local_obj_academicProject.str_degreeName = local_list_options[0].strip()
                    local_obj_academicProject.str_institueName = local_list_options[1].strip()

            local_button_updateExistingAcademicProject = st.button("Update Existing Academic Projects", key="update_existing_academic_projects")
            if local_button_updateExistingAcademicProject:
                self._update_academic_projects(local_list_academicProjects)
                st.rerun()
        
        local_button_addNewAcademicProject = st.button("Add new academic project", key="add_new_academic_project")
        if local_button_addNewAcademicProject:
            self._add_new_academic_project()
            

    @st.fragment
    def _add_new_academic_project(self):
        st.markdown("#### Add new academic project")
        
        local_obj_academicProject = AcademicProject()
        
        local_obj_academicProject.str_projectTitle = st.text_input("Project Title", value=local_obj_academicProject.str_projectTitle, key=f"{local_obj_academicProject.str_projectTitle}_proj_new")
        local_obj_academicProject.str_projectContents = st.text_area("Detailed Information about the project in Markdown", value=local_obj_academicProject.str_projectContents, key=f"{local_obj_academicProject.str_projectTitle}_proj_new")
        local_obj_academicProject.str_highlights = st.text_area("Highlights of this project", local_obj_academicProject.str_highlights, key=f"{local_obj_academicProject.str_projectTitle}_proj_new")
        
        local_list_educationDegrees = self._get_education_institute(self._str_profileName)
        local_str_selectedEducation = st.selectbox("Select your education degree", local_list_educationDegrees, index=0, key=f"{local_obj_academicProject.str_projectTitle}_ed_proj_new")
        local_list_options = local_str_selectedEducation.split("@")
        local_obj_academicProject.str_degreeName = local_list_options[0].strip()
        local_obj_academicProject.str_institueName = local_list_options[1].strip()
        local_button_createNewAcademicProject = st.button("Update New academic project", key="update_new_academic_project")
        if local_button_createNewAcademicProject:
            self._create_new_academic_project(local_obj_academicProject)
            st.rerun()
    
    def _read_all_academic_projects(self):
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        return local_obj_profile.list_academicProjects
    
    def _update_academic_projects(self, param_list_academicProjects:list[AcademicProject]):
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        local_obj_profile.list_academicProjects = param_list_academicProjects
        st.info("Academic project modified succesfully")

    def _create_new_academic_project(self, param_obj_academicProjects:AcademicProject):
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        local_obj_profile.list_academicProjects.append(param_obj_academicProjects)
        self._obj_profileAPIs.update(self._str_profileName, local_obj_profile)
        st.info("Academic project added succesfully")

    def _get_education_institute(self, param_str_profileName:str):
        local_obj_profile = self._obj_profileAPIs.read(param_str_profileName)
        local_list_educationInstitutes = local_obj_profile.list_education
        local_list_educatios = [f'{local_obj_education.str_degree} @ {local_obj_education.str_institutionName}' for local_obj_education in local_list_educationInstitutes]
        return local_list_educatios
