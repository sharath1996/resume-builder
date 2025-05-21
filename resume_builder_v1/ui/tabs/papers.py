import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import Papers
from datetime import datetime

class PapersUI:

    def __init__(self, param_str_profileName:str):
        self._str_profileName:str = param_str_profileName
        self._obj_profileAPI =  ProfileAPIs()
    
    def run(self):
        local_list_papers = self._get_available_papers()
        if len(local_list_papers)>0:
            for local_obj_paper in local_list_papers:
                # convert the existing string into datetime object for rendering in UI
                with st.expander(local_obj_paper.str_paperTile):
                    local_datetime_dateTime = datetime.strptime(local_obj_paper.datetime_publicationDate, "%Y-%m-%d")
                    
                    local_obj_paper.str_paperTile = st.text_input("Title of the paper", value=local_obj_paper.str_paperTile, key = f"{local_obj_paper.str_paperTile}_title")
                    local_obj_paper.str_abstract = st.text_area("Abstract of the paper", value=local_obj_paper.str_abstract, key = f"{local_obj_paper.str_paperTile}_abstract")
                    local_obj_paper.str_publisherDetails = st.text_input("Publisher Details", value=local_obj_paper.str_publisherDetails, key=f"{local_obj_paper.str_paperTile}_publisher")
                    local_obj_paper.str_hyperLink = st.text_input("Hyper link to publication", value=local_obj_paper.str_hyperLink,key=f"{local_obj_paper.str_paperTile}_link" )
                    local_obj_paper.datetime_publicationDate = st.date_input("Date Of Publication", value=local_datetime_dateTime,key=f"{local_obj_paper.str_paperTile}_date" ).strftime("%Y-%m-%d")
            
            local_button_updateDetails = st.button("Update Exisitng Papers")
            if local_button_updateDetails:
                self._update_existing_details(local_list_papers)
                st.rerun()
        
        local_button_newCertificate = st.button("Add new paper")
        if local_button_newCertificate:
            self._add_new_paper()
            
    
    @st.fragment
    def _add_new_paper(self):

        with st.container(border=True):
            st.markdown("#### Add Paper")
            local_obj_newPaper = Papers()
            local_datetime_dateTime = datetime.now()

            local_obj_newPaper.str_paperTile = st.text_input("Title of the paper", value=local_obj_newPaper.str_paperTile, key = f"{local_obj_newPaper.str_paperTile}_title")
            local_obj_newPaper.str_abstract = st.text_area("Abstract of the paper", value=local_obj_newPaper.str_abstract, key = f"{local_obj_newPaper.str_paperTile}_abstract")
            local_obj_newPaper.str_publisherDetails = st.text_input("Publisher Details", value=local_obj_newPaper.str_publisherDetails, key=f"{local_obj_newPaper.str_paperTile}_publisher")
            local_obj_newPaper.str_hyperLink = st.text_input("Hyper link to publication", value=local_obj_newPaper.str_hyperLink,key=f"{local_obj_newPaper.str_paperTile}_link" )
            local_obj_newPaper.datetime_publicationDate = st.date_input("Date Of Publication", value=local_datetime_dateTime,key=f"{local_obj_newPaper.str_paperTile}_date" ).strftime("%Y-%m-%d")
            local_obj_saveNewPaper = st.button("Save new paper")
            if local_obj_saveNewPaper:
                self._create_new_paper(local_obj_newPaper)
                st.rerun()

    def _get_available_papers(self) -> list[Papers]:

        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_list_papers = local_obj_profile.list_papers
        return local_list_papers

    def _update_existing_details(self, param_list_papers:list[Papers]):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_papers = param_list_papers
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Papers updated Successfully!")
    
    def _create_new_paper(self, param_obj_paper:Papers):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_papers.append(param_obj_paper)
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Papers updated Successfully!")