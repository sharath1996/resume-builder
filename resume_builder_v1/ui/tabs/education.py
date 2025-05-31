import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import Education
from datetime import datetime

class EducationUI:

    def __init__(self, param_str_profileName):
        self._str_profileName:str = param_str_profileName
        self._obj_profile = ProfileAPIs()
    
    def run(self):
        local_list_educationDetails = self._read_all_institutes()
        for local_obj_education in local_list_educationDetails:
            local_dateTime_endDate = local_obj_education.datetime_endDate if local_obj_education.datetime_endDate == "today" else datetime.strptime(local_obj_education.datetime_endDate, "%Y-%m-%d")
            local_dateTime_startDate =  datetime.strptime(local_obj_education.datetime_endDate, "%Y-%m-%d")
            with st.expander(f"{local_obj_education.str_degree} @ {local_obj_education.str_institutionName} "):
                local_obj_education.str_institutionName = st.text_input("Name of the institution", value=local_obj_education.str_institutionName, key=f"{local_obj_education.str_institutionName}_edu_exi")
                local_obj_education.str_degree = st.text_input("Degree Obtained",value=local_obj_education.str_degree, key=f"{local_obj_education.str_institutionName}_degree_exi")
                local_obj_education.str_grade = st.text_input("Grade Obtained", value=local_obj_education.str_grade, key=f"{local_obj_education.str_institutionName}_grade_exi")
                local_obj_education.str_place = st.text_input("Place of Study", value=local_obj_education.str_place, key=f"{local_obj_education.str_institutionName}_place_exi")
                local_obj_education.str_description = st.text_area("Description of your course and highlights", value=local_obj_education.str_description, key=f"{local_obj_education.str_institutionName}_description_exi")
                local_obj_columns = st.columns(2)
                local_obj_education.datetime_startDate = local_obj_columns[0].date_input("Start Date", value=local_dateTime_startDate, key=f"{local_obj_education.str_institutionName}_start_date").strftime("%Y-%m-%d")
                local_obj_education.datetime_endDate = local_obj_columns[1].date_input("End Date", value=local_dateTime_endDate, key=f"{local_obj_education.str_institutionName}_end_date").strftime("%Y-%m-%d")
                if local_obj_education.datetime_endDate == datetime.now().strftime("%Y-%m-%d"):
                    local_obj_education.datetime_endDate = "today"
                
        local_button_updateEducationDetails = st.button("Update Education Details", key="update_education_details")
        if local_button_updateEducationDetails:
            self._update_education(local_list_educationDetails)
            st.rerun()
        local_obj_addNewEducation = st.button("Add New Education", key="add_new_education")
        if local_obj_addNewEducation:
            self._create_new_education()
    
    @st.fragment
    def _create_new_education(self):
        st.markdown("#### Add New education")
        local_obj_education = Education()
        with st.container(border=True):
            local_obj_education.str_institutionName = st.text_input("Name of the institution", value=local_obj_education.str_institutionName, key="new_education_institution")
            local_obj_education.str_degree = st.text_input("Degree Obtained",value=local_obj_education.str_degree, key="new_education_degree")
            local_obj_education.str_grade = st.text_input("Grade Obtained", value=local_obj_education.str_grade, key="new_education_grade")
            local_obj_education.str_place = st.text_input("Place of Study", value=local_obj_education.str_place, key="new_education_place")
            local_obj_education.str_description = st.text_area("Description of your course and highlights", value=local_obj_education.str_description, key="new_education_description")
            local_obj_columns = st.columns(2)
            local_obj_education.datetime_startDate = local_obj_columns[0].date_input("Start Date", value="today", key="new_education_start_date").strftime("%Y-%m-%d")
            local_obj_education.datetime_endDate = local_obj_columns[1].date_input("End Date", value="today", key="new_education_end_date").strftime("%Y-%m-%d")
            local_button_addNewEducation = st.button("Update new education details", key="update_new_education_details")
            if local_button_addNewEducation:
                self._add_new_education(local_obj_education)
                st.rerun()
        
    
    def _read_all_institutes(self)->list[Education]:
        local_obj_profile = self._obj_profile.read(self._str_profileName)
        return local_obj_profile.list_education
    
    def _update_education(self, param_list_education:list[Education]):
        local_obj_profile = self._obj_profile.read(self._str_profileName)
        local_obj_profile.list_education = param_list_education
        self._obj_profile.update(self._str_profileName, local_obj_profile)
        st.info("Updated education details")
    
    def _add_new_education(self, param_obj_education:Education):
        local_obj_profile = self._obj_profile.read(self._str_profileName)
        local_obj_profile.list_education.append(param_obj_education)
        self._obj_profile.update(self._str_profileName, local_obj_profile)
        st.info("Added new education details")