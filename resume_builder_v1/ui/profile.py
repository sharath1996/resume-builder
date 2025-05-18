import streamlit as st
from ..api.profile_apis import ProfileAPIs
from ..database.db import  Profile, WorkExperience, Roles, Certification
from datetime import datetime
class ProfileUI:

    def __init__(self):
        st.set_page_config("Profile Details", layout="wide")
        self._obj_profileAPI = ProfileAPIs()
    
    @st.fragment
    def render_profile(self, param_str_profileName:str):
        
        local_obj_profile = self._obj_profileAPI.read(param_str_profileName)
        st.header("Profile Details")
        with st.form('Profile'):
            with st.expander("Profile Details"):
                local_obj_profile.obj_profileInfo.str_fullName = st.text_input("Full Name", value=local_obj_profile.obj_profileInfo.str_fullName)
                local_obj_profile.obj_profileInfo.str_aboutCandidate = st.text_area("About You!", local_obj_profile.obj_profileInfo.str_aboutCandidate)
                local_obj_profile.obj_profileInfo.str_currentResidence = st.text_input("Current Residence", value=local_obj_profile.obj_profileInfo.str_currentResidence)
                local_obj_profile.obj_profileInfo.str_contactNumber = st.text_input("Phone Details", value=local_obj_profile.obj_profileInfo.str_contactNumber)
                local_obj_profile.obj_profileInfo.str_linkedInProfile = st.text_input("LinkedIn Profile URL", value=local_obj_profile.obj_profileInfo.str_linkedInProfile)
                local_obj_profile.obj_profileInfo.str_githubProfile = st.text_input("Github profile url", value=local_obj_profile.obj_profileInfo.str_githubProfile)
                local_obj_profile.obj_profileInfo.str_customProfile = st.text_input("Custom Portfolio website", value=local_obj_profile.obj_profileInfo.str_customProfile)
            
            with st.expander("Work Experience"):
                local_list_workExperiences = local_obj_profile.list_workExperience
                local_list_companyNames = [local_obj_workExperience.str_companyName for local_obj_workExperience in local_list_workExperiences]
                local_list_companyNames.append("Add New")

                local_str_selectedCompanyName = st.selectbox("Select the company", local_list_companyNames, index=None)

                if local_str_selectedCompanyName == "Add New":

                    with st.container():
                        local_obj_workExperience = WorkExperience()
                        local_obj_workExperience.str_companyName = st.text_input("Name of the company", value=local_obj_workExperience.str_companyName)
                        
                
                else:
                    ...
                
            
            with st.expander("Education"):
                st.text("Education")
            
            with st.expander("Certifications"):
                local_list_availableCertificates = local_obj_profile.list_certifcations
                local_obj_newCertification = Certification()
                local_obj_newCertification.str_name = ""
                local_list_availableCertificates.append(local_obj_newCertification)
                local_index_certificationIndex = 0
                for local_obj_certifications in local_list_availableCertificates:
                    with st.container(border=True):
                        try:
                            local_datetime_dateTime = datetime.strptime(local_obj_certifications.datetime_issueDate, "%Y-%m-%d")
                        except:
                            local_datetime_dateTime = datetime.today()
                        if local_obj_certifications.str_name == "":
                            st.markdown("##### :blue[Add New Certification Details]")
                        
                        local_obj_certifications.str_name = st.text_input("Name of the certification", value=local_obj_certifications.str_name, key=f"{local_obj_certifications.str_name}_cert_name")
                        local_obj_certifications.str_issuingAuthority = st.text_input("Issuing Authority", value=local_obj_certifications.str_issuingAuthority, key=f"{local_obj_certifications.str_name}_cert_auth")
                        local_obj_certifications.datetime_issueDate = st.date_input("Issuing Date", value=local_datetime_dateTime, key=f"{local_obj_certifications.str_name}_cert_date").strftime("%Y-%m-%d")
                        
                        local_obj_column = st.columns(2)
                        local_button_updateButton = local_obj_column[0].form_submit_button(f"Update {local_obj_certifications.str_name} Details")
                        if local_button_updateButton:
                            local_obj_profile.list_certifcations[local_index_certificationIndex] = local_obj_certifications
                        
                        
                        # local_button_updateButton = local_obj_column[1].form_submit_button(f"Delete {local_obj_certifications.str_name} Details")
                        # if local_button_updateButton:
                        #     local_obj_profile.list_certifcations.pop(local_index_certificationIndex)
                    
                    local_index_certificationIndex+= 1

            with st.expander("Papers"):
                st.text("Papers")
            
            with st.expander("Patents"):
                st.text("Patents")
            
            with st.expander("Talks"):
                st.text("Talks")

            if st.form_submit_button("Update Profile"):
                self._obj_profileAPI.update("Sharath", local_obj_profile)
                st.info(f"Number of certifications = {len(local_obj_profile.list_certifcations)}")
                st.toast("Updated Profile ", icon="😄")

            else:
                return None
    
    @st.dialog("Add New")   
    def pop_up(self, param_callable_callableLayout:callable):
        param_callable_callableLayout()

    def run_ui(self):
        
        local_obj_renderResults = self.render_profile("Sharath")    
        if local_obj_renderResults != None:
            st.success("Updated Profile")
    
    
    
