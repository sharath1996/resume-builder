import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import Patents
from datetime import datetime

class PatentsUI:

    def __init__(self, param_str_profileName:str):
        self._str_profileName:str = param_str_profileName
        self._obj_profileAPI =  ProfileAPIs()
    
    def run(self):
        local_list_patents = self._get_available_patents()
        if len(local_list_patents)>0:
            for local_obj_patent in local_list_patents:
                # convert the existing string into datetime object for rendering in UI
                with st.container(border=True):
                    local_datetime_dateTime = datetime.strptime(local_obj_patent.datetime_publicationDate, "%Y-%m-%d")
                    
                    local_obj_patent.str_patentTitle = st.text_input("Title of the patent", value=local_obj_patent.str_patentTitle, key = f"{local_obj_patent.str_patentTitle}_title")
                    local_obj_patent.str_abstract = st.text_area("Abstract of the patent", value=local_obj_patent.str_abstract, key = f"{local_obj_patent.str_patentTitle}_abstract")
                    local_obj_patent.str_patentOffice = st.text_input("Patent office", value=local_obj_patent.str_patentOffice, key=f"{local_obj_patent.str_patentTitle}_patentOffice")
                    local_obj_patent.datetime_publicationDate = st.date_input("Date Of Publication/Issue", value=local_datetime_dateTime,key=f"{local_obj_patent.str_patentTitle}_date" ).strftime("%Y-%m-%d")
            
            local_button_updateDetails = st.button("Update patents")
            if local_button_updateDetails:
                self._update_existing_patents(local_list_patents)
        
        local_button_newCertificate = st.button("Add new patent")
        if local_button_newCertificate:
            self._add_new_patent()
    
    @st.fragment
    def _add_new_patent(self):

        with st.container(border=True):
            st.markdown("#### Add Patent")
            local_obj_newpatent = Patents()
            local_datetime_dateTime = datetime.now()
            local_obj_newpatent.str_patentTitle = st.text_input("Title of the patent", value=local_obj_newpatent.str_patentTitle, key = f"{local_obj_newpatent.str_patentTitle}_title")
            local_obj_newpatent.str_abstract = st.text_area("Abstract of the patent", value=local_obj_newpatent.str_abstract, key = f"{local_obj_newpatent.str_patentTitle}_abstract")
            local_obj_newpatent.str_patentOffice = st.text_input("Patent office", value=local_obj_newpatent.str_patentOffice, key=f"{local_obj_newpatent.str_patentTitle}_patentOffice")
            local_obj_newpatent.datetime_publicationDate = st.date_input("Date Of Publication", value=local_datetime_dateTime,key=f"{local_obj_newpatent.str_patentTitle}_date" ).strftime("%Y-%m-%d")
            local_obj_saveNewpatent = st.button("Save new patent")
            if local_obj_saveNewpatent:
                self._create_new_patent(local_obj_newpatent)

    def _get_available_patents(self) -> list[Patents]:

        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_list_patents = local_obj_profile.list_patents
        return local_list_patents

    def _update_existing_patents(self, param_list_patents:list[Patents]):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_patents = param_list_patents
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Patents updated Successfully!")
    
    def _create_new_patent(self, param_obj_patent:Patents):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_patents.append(param_obj_patent)
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Patents updated Successfully!")