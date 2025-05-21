import streamlit as st
from ...api.profile_apis import ProfileAPIs
from ...database.db import Certification
from datetime import datetime


class CertificationUI:

    def __init__(self, param_str_profileName:str):
        self._str_profileName:str = param_str_profileName
        self._obj_profileAPI =  ProfileAPIs()

    
    def run(self):
        # list all the certifications and a button to add a new certificate!

        # list all the certificates
        local_list_certificates = self._get_available_certifications()

        for local_obj_certificate in local_list_certificates:
            # convert the existing string into datetime object for rendering in UI
            with st.expander(local_obj_certificate.str_name):
                local_datetime_dateTime = datetime.strptime(local_obj_certificate.datetime_issueDate, "%Y-%m-%d")
                
                local_obj_certificate.str_name = st.text_input("Certificate Name", value = local_obj_certificate.str_name, key = f"{local_obj_certificate.str_name}_name")
                local_obj_certificate.str_issuingAuthority = st.text_input("Certification Issuing Authority", value = local_obj_certificate.str_issuingAuthority, key = f"{local_obj_certificate.str_name}_auth")
                local_str_dateTimeOfIssue = st.date_input("Date of Issueing", value=local_datetime_dateTime, key = f"{local_obj_certificate.str_name}_time").strftime("%Y-%m-%d")
                local_obj_certificate.datetime_issueDate = local_str_dateTimeOfIssue
        
        local_button_updateDetails = st.button("Update Exisitng Details")
        if local_button_updateDetails:
            self._update_existing_details(local_list_certificates)
            st.rerun()
        
        local_button_newCertificate = st.button("Add new...")
        if local_button_newCertificate:
            self._add_new_certificate_ui()
            

    @st.fragment
    def _add_new_certificate_ui(self):
        with st.container(border=True):
                st.markdown("#### Add Certification")
                local_obj_newCertificate = Certification()
                local_datetime_dateTime = datetime.now()
                
                local_obj_newCertificate.str_name = st.text_input("Certificate Name", value = local_obj_newCertificate.str_name, key = f"{local_obj_newCertificate.str_name}_name")
                local_obj_newCertificate.str_issuingAuthority = st.text_input("Certification Issuing Authority", value = local_obj_newCertificate.str_issuingAuthority, key = f"{local_obj_newCertificate.str_name}_auth")
                local_str_dateTimeOfIssue = st.date_input("Date of Issueing", value=local_datetime_dateTime, key = f"{local_obj_newCertificate.str_name}_time").strftime("%Y-%m-%d")
                local_obj_newCertificate.datetime_issueDate = local_str_dateTimeOfIssue
                local_button_addNewCertificate = st.button("Save Certificate")
                if local_button_addNewCertificate:
                    self._create_new_certification(local_obj_newCertificate)
                    st.rerun()
    
    def _get_available_certifications(self) -> list[Certification]:

        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_list_certifications = local_obj_profile.list_certifcations
        return local_list_certifications

    def _update_existing_details(self, param_list_certifications:list[Certification]):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_certifcations = param_list_certifications
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Certificates updated Successfully!")
    
    def _create_new_certification(self, param_obj_certification:Certification):
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        local_obj_profile.list_certifcations.append(param_obj_certification)
        self._obj_profileAPI.update(self._str_profileName,local_obj_profile)
        st.info("Certificates updated Successfully!")
    
    