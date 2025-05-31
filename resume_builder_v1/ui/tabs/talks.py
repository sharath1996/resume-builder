import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import Talks
from datetime import datetime

class TalksUI:

    def __init__(self, param_str_profileName:str):
        self._str_profileName:str = param_str_profileName
        self._obj_profileAPI =  ProfileAPIs()
    
    def run(self):
        local_list_talks = self._get_available_talks()
        if len(local_list_talks)>0:
            for local_obj_talk in local_list_talks:
                with st.expander(f"{local_obj_talk.str_title} @ {local_obj_talk.str_place}"):
                    local_datetime_dateTime = datetime.strptime(local_obj_talk.datetime_date, "%Y-%m-%d")
                    local_obj_talk.str_title = st.text_input("Title of the talk", value=local_obj_talk.str_title, key = f"{local_obj_talk.str_title}_talk_title")
                    local_obj_talk.str_abstract = st.text_area("Abstract of the talk", value=local_obj_talk.str_abstract, key = f"{local_obj_talk.str_title}_talk_abstract")
                    local_obj_talk.str_place = st.text_input("Place", value=local_obj_talk.str_patentOffice, key=f"{local_obj_talk.str_title}_talk_place")
                    local_obj_talk.datetime_date = st.date_input("Date Of talk", value=local_datetime_dateTime,key=f"{local_obj_talk.str_title}_talk_date" ).strftime("%Y-%m-%d")
            local_button_updateDetails = st.button("Update talks", key="update_talks")
            if local_button_updateDetails:
                self._update_existing_talks(local_list_talks)
        local_button_newCertificate = st.button("Add new talk", key="add_new_talk")
        if local_button_newCertificate:
            self._add_new_talk()
            
    
    @st.fragment
    def _add_new_talk(self):
        with st.container(border=True):
            st.markdown("#### Add Talk")
            local_obj_newtalk = Talks()
            local_datetime_dateTime = datetime.now()
            local_obj_newtalk.str_title = st.text_input("Title of the Talk", value=local_obj_newtalk.str_title, key = f"{local_obj_newtalk.str_title}_talk_title")
            local_obj_newtalk.str_abstract = st.text_area("Abstract of the talk", value=local_obj_newtalk.str_abstract, key = f"{local_obj_newtalk.str_title}_talk_abstract")
            local_obj_newtalk.str_place = st.text_input("Place", value=local_obj_newtalk.str_place, key=f"{local_obj_newtalk.str_title}_talk_place")
            local_obj_newtalk.datetime_date = st.date_input("Date Of Talk", value=local_datetime_dateTime,key=f"{local_obj_newtalk.str_title}_talk_date" ).strftime("%Y-%m-%d")
            local_obj_saveNewtalk = st.button("Save new talk", key="save_new_talk")
            if local_obj_saveNewtalk:
                self._create_new_talk(local_obj_newtalk)
                st.rerun()

    def _get_available_talks(self) -> list[Talks]:

        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_list_talks = local_obj_profile.list_talks
        return local_list_talks

    def _update_existing_talks(self, param_list_talks:list[Talks]):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_talks = param_list_talks
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Talks updated Successfully!")
    
    def _create_new_talk(self, param_obj_patent:Talks):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_talks.append(param_obj_patent)
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Talks updated Successfully!")