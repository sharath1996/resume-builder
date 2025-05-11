import streamlit as st
from ..api.profile_apis import ProfileAPIs
from ..database.db import  Profile, WorkExperience, Roles
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
                st.text("Certifications")

            with st.expander("Papers"):
                st.text("Papers")
            
            with st.expander("Patents"):
                st.text("Patents")
            
            with st.expander("Talks"):
                st.text("Talks")

            if st.form_submit_button("Update Profile"):
                self._obj_profileAPI.update("Sharath", local_obj_profile)
                st.toast("Updated Profile ", icon="😄")

            else:
                return None
        

    def run_ui(self):
        
        local_obj_renderResults = self.render_profile("Sharath")    
        if local_obj_renderResults != None:
            st.success("Updated Profile")
    
    
    
