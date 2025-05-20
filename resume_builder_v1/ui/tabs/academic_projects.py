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
                with st.container(border=True):
                    local_obj_academicProject.str_projectTitle = st.text_input("Project Title", value=local_obj_academicProject.str_projectTitle)
                    local_obj_academicProject.str_projectContents = st.text_area("Detailed Information about the project in Markdown", value=local_obj_academicProject.str_projectContents)
                    local_obj_academicProject.str_highlights = st.text_area("Highlights of this project", local_obj_academicProject.str_highlights)
                    
                    st.markdown("**The below two items should match your `Education` profile details!!!** ")

                    local_obj_academicProject.str_institueName = st.text_input("Name of the institute", value=local_obj_academicProject.str_institueName)
                    local_obj_academicProject.str_degreeName = st.text_input("Name of the degree", local_obj_academicProject.str_degreeName)

            local_button_updateExistingAcademicProject = st.button("Update Existing Academic Projects")
            if local_button_updateExistingAcademicProject:
                self._update_academic_projects(local_list_academicProjects)
        
        local_button_addNewAcademicProject = st.button("Add new academic project")
        if local_button_addNewAcademicProject:
            self._add_new_academic_project()

    @st.fragment
    def _add_new_academic_project(self):
        
        st.markdown("#### Add new academic project")
        
        local_obj_academicProject = AcademicProject()
        
        local_obj_academicProject.str_projectTitle = st.text_input("Project Title", value=local_obj_academicProject.str_projectTitle)
        local_obj_academicProject.str_projectContents = st.text_area("Detailed Information about the project in Markdown", value=local_obj_academicProject.str_projectContents)
        local_obj_academicProject.str_highlights = st.text_area("Highlights of this project", local_obj_academicProject.str_highlights)
        
        st.markdown(":red[**The below two items should match your `Education` profile details!!!**]")

        local_obj_academicProject.str_institueName = st.text_input("Name of the institute", value=local_obj_academicProject.str_institueName)
        local_obj_academicProject.str_degreeName = st.text_input("Name of the degree", local_obj_academicProject.str_degreeName)

        local_button_createNewAcademicProject = st.button("Update New academic project")
        if local_button_createNewAcademicProject:
            self._create_new_academic_project(local_obj_academicProject)
    
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

