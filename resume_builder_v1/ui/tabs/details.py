from ...api.profile_apis import ProfileAPIs
import streamlit as st

class ProfileBasicDetails:

    def __init__(self, param_str_profileName:str):
        self._str_profileName = param_str_profileName
        self._obj_profileAPI = ProfileAPIs()
    
    def run(self):
        
        local_obj_profile = self._obj_profileAPI.read(self._str_profileName)
        
        local_obj_profile.obj_profileInfo.str_fullName = st.text_input("Full Name", value=local_obj_profile.obj_profileInfo.str_fullName, key="profile_full_name")
        local_obj_profile.obj_profileInfo.str_aboutCandidate = st.text_area("About You!", local_obj_profile.obj_profileInfo.str_aboutCandidate, key="profile_about_candidate")
        local_obj_profile.obj_profileInfo.str_currentResidence = st.text_input("Current Residence", value=local_obj_profile.obj_profileInfo.str_currentResidence, key="profile_current_residence")
        local_obj_profile.obj_profileInfo.str_contactNumber = st.text_input("Phone Details", value=local_obj_profile.obj_profileInfo.str_contactNumber, key="profile_contact_number")
        local_obj_profile.obj_profileInfo.str_email = st.text_input("Email Address", value=local_obj_profile.obj_profileInfo.str_email, key="profile_email_address")
        local_obj_profile.obj_profileInfo.str_linkedInProfile = st.text_input("LinkedIn Profile URL", value=local_obj_profile.obj_profileInfo.str_linkedInProfile, key="profile_linkedin_profile")
        local_obj_profile.obj_profileInfo.str_githubProfile = st.text_input("Github profile url", value=local_obj_profile.obj_profileInfo.str_githubProfile, key="profile_github_profile")
        local_obj_profile.obj_profileInfo.str_customProfile = st.text_input("Custom Portfolio website", value=local_obj_profile.obj_profileInfo.str_customProfile, key="profile_custom_profile")
        local_obj_button = st.button('Save Profile Information')
        if local_obj_button:
            self._obj_profileAPI.update(self._str_profileName, local_obj_profile)
            st.rerun()