import streamlit as st
from ..builder.builder import ResumeBuilder, ResumeBuilderInput, CandidateResume
from .resume_generator.preview import ResumePreview
from ..api.profile_apis import ProfileAPIs
from ..database.db import JobApplications
    
class JobAppUI:

    def __init__(self, param_str_profileName:str):
        self._str_profileName = param_str_profileName
        self._obj_profileAPIs = ProfileAPIs()
        if not "isResumeGenerating" in st.session_state:
            st.session_state["bool_isResumeGenerating"] = False
    
    @st.fragment
    def run(self):
        
        local_list_existingApps = self._get_all_applications_in_db()
        local_list_existingApps.append("Create New")
        
        st.subheader("Job Applications")
        
        local_str_selectedJobApp = st.selectbox(
            "Select Job Application",
            options=local_list_existingApps,
            index=None
        )

        if local_str_selectedJobApp == "Create New":
            local_obj_jobApp = JobApplications()

        elif len(local_list_existingApps) > 1:
            local_obj_jobApp = self._read_existing_application(local_str_selectedJobApp)
        
        else:
            st.warning("No job applications found. Please create a new one.")
            return 
    
        if local_str_selectedJobApp == None:
            st.warning("Please select a job application to proceed.")
            return

        local_obj_jobApp.str_uniqueJobTitle = st.text_input("Job Title", value=local_obj_jobApp.str_uniqueJobTitle)
        local_obj_jobApp.str_jobDescriptions = st.text_area("Job Description", value= local_obj_jobApp.str_jobDescriptions, height=300)
        local_str_additionalInstructions = st.text_area("Additional Instructions", 
                                                        value="", 
                                                        height=70)
        local_button_generateResume = st.button("Generate Resume", key="generate_resume")
        
        if local_button_generateResume:
            with st.spinner("Generating resume..."):
                st.session_state["bool_isResumeGenerating"] = True
                local_obj_resumeBuilderInput = ResumeBuilderInput(
                    str_profileName=self._str_profileName,
                    str_jobDescription=local_obj_jobApp.str_jobDescriptions,
                    str_additionalInstructions=local_str_additionalInstructions
                )
                local_obj_resumeBuilder = ResumeBuilder()
                local_obj_resume = local_obj_resumeBuilder.build(local_obj_resumeBuilderInput)
                self._update_the_db(local_obj_resume, local_obj_jobApp)
                st.success("Resume generated successfully!")
                st.session_state["bool_isResumeGenerating"] = False
                
        
        if not st.session_state["bool_isResumeGenerating"]:
            local_obj_resume = self._get_existing_resume(local_obj_jobApp.str_uniqueJobTitle)
            if local_obj_resume:
                local_obj_updatedResume = self.preview_and_export(local_obj_resume)

            
        
    
    def _get_all_applications_in_db(self) -> list[str]:
        """
        Read existing job applications for the profile using ProfileAPIs.
        """
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        local_list_jobApps = local_obj_profile.list_jobApps
        if local_list_jobApps:
            local_list_existingApps = [local_obj_jobApp.str_uniqueJobTitle for local_obj_jobApp in local_list_jobApps]
        else:
            local_list_existingApps = []
        return local_list_existingApps

    def _read_existing_application(self, param_str_uniqueID:str) -> JobApplications:
        """
        Read an existing job application from the database using ProfileAPIs.
        """
        try:
            local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
            local_obj_jobApp = local_obj_profile.list_jobApps
            if not local_obj_jobApp:
                return None
            for local_obj_app in local_obj_jobApp:
                if local_obj_app.str_uniqueJobTitle == param_str_uniqueID:
                    return local_obj_app
        except Exception as e:
            st.error(f"Error reading job application -{param_str_uniqueID} resulting in {e}")
            return None

    def _update_the_db(self, param_obj_resume:CandidateResume, param_obj_jobAPP:JobApplications):
        """
        Update or create a job application in the database using ProfileAPIs.
        """
        local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
        local_obj_existingJobApp = local_obj_profile.list_jobApps
        if local_obj_existingJobApp:
            for local_obj_app in local_obj_existingJobApp:
                if local_obj_app.str_uniqueJobTitle == param_obj_jobAPP.str_uniqueJobTitle:
                    local_obj_app.str_jobDescriptions = param_obj_jobAPP.str_jobDescriptions
                    local_obj_app.dict_jsonResume = param_obj_resume.model_dump()
                    st.info("Existing application updated successfully!")
                    break
            else:
                # If not found, append new job application
                local_obj_newJobApp = JobApplications(
                    str_uniqueJobTitle=param_obj_jobAPP.str_uniqueJobTitle,
                    str_jobDescriptions=param_obj_jobAPP.str_jobDescriptions,
                    dict_jsonResume=param_obj_resume.model_dump()
                )
                local_obj_existingJobApp.append(local_obj_newJobApp)
                st.info("New job application added successfully!")
        else:
            # Create new job application
            local_obj_jobApp = JobApplications(
                str_uniqueJobTitle=param_obj_jobAPP.str_uniqueJobTitle,
                str_jobDescriptions=param_obj_jobAPP.str_jobDescriptions,
                dict_jsonResume=param_obj_resume.model_dump()
            )
            local_obj_existingJobApp = [local_obj_jobApp]
            setattr(local_obj_profile, 'list_jobApps', local_obj_existingJobApp)
            st.info("Your First job application added successfully!")
        # Update the profile with the job applications
        self._obj_profileAPIs.update(
            self._str_profileName,
            local_obj_profile
        )
        st.write(f"Total Job Applications: {len(getattr(local_obj_profile, 'list_jobApps', []))}")

    def _get_existing_resume(self, param_str_uniqueJobTitle:str) -> CandidateResume:
        """
        Retrieve and display the existing resume for the selected job application using ProfileAPIs.
        """
        try:
            local_obj_profile = self._obj_profileAPIs.read(self._str_profileName)
            local_obj_jobApp = local_obj_profile.list_jobApps
            if not local_obj_jobApp:
                st.warning("No job applications found for this profile.")
                return None
            for local_obj_app in local_obj_jobApp:
                if local_obj_app.str_uniqueJobTitle == param_str_uniqueJobTitle:
                    if local_obj_app.dict_jsonResume:
                        return CandidateResume(**local_obj_app.dict_jsonResume)
                    else:
                        st.warning("No resume generated for this job application.")
                        return None
            else:
                st.warning("No job application found with that title.")
                return None
        except Exception as e:
            st.error(f"Error retrieving resume for {param_str_uniqueJobTitle} - {e}")
            return None
    
    def preview_and_export(self, param_obj_resume)-> CandidateResume:
        """
        Preview and export the generated resume.
        """
        st.subheader("Preview Resume")
        local_obj_resumePreview = ResumePreview()
        local_obj_resume = local_obj_resumePreview.preview_and_export(param_obj_resume)
        return local_obj_resume




