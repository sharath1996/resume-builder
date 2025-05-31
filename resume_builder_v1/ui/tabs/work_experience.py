import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import WorkExperience
from datetime import datetime


class WorkExperienceUI:

    def __init__(self, param_str_profileName:str):
        self._str_profileName:str = param_str_profileName
        self._obj_profile = ProfileAPIs()
    
    def run(self):

        local_list_workExps = self._read_all_work_experiences()
        if len(local_list_workExps) == 0:
            st.markdown("#### This looks empty, try adding a new work experience")
        
        else:   
            for local_obj_workExperience in local_list_workExps:
                local_str_keyGenValue = f"{local_obj_workExperience.str_companyName}_{local_obj_workExperience.str_title}"
                with st.expander(f"{local_obj_workExperience.str_title} @ {local_obj_workExperience.str_companyName}"):
                    if local_obj_workExperience.dateTime_endDate == "today":
                        local_obj_endDate = "today"
                    else:
                        local_obj_endDate = datetime.strptime(local_obj_workExperience.dateTime_endDate, "%Y-%m-%d")
                    local_dateTime_startDate = datetime.strptime(local_obj_workExperience.dateTime_startDate, "%Y-%m-%d")
                    local_obj_workExperience.str_companyName = st.text_input("Name of the company", value=local_obj_workExperience.str_companyName, key=f"{local_str_keyGenValue}_work_experience")
                    local_obj_workExperience.str_title = st.text_input("Designation / Role", value=local_obj_workExperience.str_title, key=f"{local_str_keyGenValue}_work_experience_title")
                    local_obj_workExperience.dateTime_endDate = st.date_input("End Date", value=local_obj_endDate, key=f"{local_str_keyGenValue}_work_end_date").strftime("%Y-%m-%d")
                    local_obj_workExperience.dateTime_startDate = st.date_input("Start Date", value=local_dateTime_startDate, key=f"{local_str_keyGenValue}_work_start_date").strftime("%Y-%m-%d")
                    local_obj_workExperience.str_description = st.text_input("Description of Roles and Responsibilities", value=local_obj_workExperience.str_description, key=f"{local_str_keyGenValue}_work_experience_description")
                    local_obj_workExperience.list_achievements = st.text_area("Top achievements (Seperated by newline)", value="\n".join(local_obj_workExperience.list_achievements), key=f"{local_str_keyGenValue}_work_experience_achievements").split("\n")
                    local_obj_workExperience.list_skills = st.text_area("List of skills (Seperated by ',')", value = ",".join(local_obj_workExperience.list_skills), key=f"{local_str_keyGenValue}_work_skills").split(",")
            local_button_updateExisting = st.button("Update work expereince", key="update_work_experience")  
            if local_button_updateExisting:
                self._update_work_experiences(local_list_workExps)
                st.rerun()
        local_button_createNewButton = st.button("Create new work experience", key="create_new_work_experience")
        if local_button_createNewButton:
            self.add_new_work_experience()
            

    @st.fragment
    def add_new_work_experience(self):
        st.markdown("### Add new work experience")
        local_obj_workExperience = WorkExperience()
        with st.container(border=True):
            local_obj_workExperience.str_companyName = st.text_input("Name of the company", value=local_obj_workExperience.str_companyName, key="new_work_experience_company")
            local_obj_workExperience.str_title = st.text_input("Designation / Role", value=local_obj_workExperience.str_title, key="new_work_experience_title")
            local_obj_workExperience.dateTime_endDate = st.date_input("End Date", value="today", key="new_work_experience_end_date").strftime("%Y-%m-%d")
            local_obj_workExperience.dateTime_startDate = st.date_input("Start Date", value="today", key="new_work_experience_start_date").strftime("%Y-%m-%d")
            local_obj_workExperience.str_description = st.text_input("Description of Roles and Responsibilities", value=local_obj_workExperience.str_description, key="new_work_experience_description")
            local_obj_workExperience.list_achievements = st.text_area("Top achievements (Seperated by newline)", value="\n".join(local_obj_workExperience.list_achievements), key='new_work_experience_achievements').split("\n")
            local_obj_workExperience.list_skills = st.text_area("List of skills (Seperated by ',')", value = ",".join(local_obj_workExperience.list_skills), key='new_work_experience_skills').split(",")
            if local_obj_workExperience.dateTime_endDate == datetime.now().strftime("%Y-%m-%d"):
                local_obj_workExperience.dateTime_endDate = "today"
            local_button_saveNewWorkExperience = st.button("Update new work experience", key="update_new_work_experience")
            if local_button_saveNewWorkExperience:
                self._create_new_work_experience(local_obj_workExperience)
                st.rerun()


    def _read_all_work_experiences(self):
        local_obj_profile = self._obj_profile.read(self._str_profileName)
        return local_obj_profile.list_workExperience
    
    
    def _update_work_experiences(self, param_list_workExperience:list[WorkExperience]):
        local_obj_profile = self._obj_profile.read(self._str_profileName)
        local_obj_profile.list_workExperience = param_list_workExperience
        st.info("Work Experience updated successfully")

    def _create_new_work_experience(self, param_obj_workExperience:WorkExperience):
        local_obj_profile = self._obj_profile.read(self._str_profileName)
        local_obj_profile.list_workExperience.append(param_obj_workExperience)
        self._obj_profile.update(self._str_profileName, local_obj_profile)
        st.info("Work Experience added successfully")
