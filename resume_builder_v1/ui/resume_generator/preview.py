import streamlit as st
from .export import ResumeExporter
from ...builder.types import CandidateResume
class ResumePreview:

    def __init__(self):
        ... 
    
    @st.fragment
    def preview_and_export(self, param_obj_resume:CandidateResume)-> CandidateResume:
        """
        Preview and edit the resume, before finalizing the export.
        Allows the user to edit all contents of the resume interactively.
        """
        local_obj_resume = param_obj_resume
        # Personal Details
        with st.expander("Applicant Details", expanded=False):
            local_obj_resume.str_fullName = st.text_input("Full Name", local_obj_resume.str_fullName, key="full_name")
            local_obj_resume.str_currentResidence = st.text_input("Current Residence", local_obj_resume.str_currentResidence, key="current_residence")
            local_obj_resume.str_contactNumber = st.text_input("Contact Number", local_obj_resume.str_contactNumber, key="contact_number")
            local_obj_resume.str_linkedInProfile = st.text_input("LinkedIn Profile", local_obj_resume.str_linkedInProfile or "", key="linkedin_profile")
            local_obj_resume.str_githubProfile = st.text_input("GitHub Profile", local_obj_resume.str_githubProfile or "", key="github_profile")
            local_obj_resume.str_customProfile = st.text_input("Custom Profile", local_obj_resume.str_customProfile or "", key="custom_profile")
            local_obj_resume.str_aboutCandidate = st.text_area("About / Summary", local_obj_resume.str_aboutCandidate, key="about_candidate")

        with st.expander("Skills", expanded=False):
            for local_obj_skillIndex, local_obj_skill in enumerate(local_obj_resume.list_skills):
                local_obj_columns = st.columns((1,3))
                local_obj_skill.str_sectionTitle = local_obj_columns[0].text_input(f"Skill Section Title {local_obj_skillIndex+1}", local_obj_skill.str_sectionTitle, key=f"skill_section_{local_obj_skillIndex}")
                local_obj_skill.list_skills = local_obj_columns[1].text_area(f"Skills (comma separated) for {local_obj_skill.str_sectionTitle}", ", ".join(local_obj_skill.list_skills), key=f"skills_{local_obj_skillIndex}").split(",")
                local_obj_skill.list_skills = [s.strip() for s in local_obj_skill.list_skills if s.strip()]

        with st.expander("Work Experience", expanded=False):
            for local_obj_expIndex, local_obj_exp in enumerate(local_obj_resume.list_workExperience):
                with st.container(border=True):
                    local_obj_columns = st.columns((2,1,1))
                    local_obj_exp.str_companyName = local_obj_columns[0].text_input(f"Company Name", local_obj_exp.str_companyName, key=f"company_{local_obj_expIndex}")
                    local_obj_exp.str_designation = local_obj_columns[1].text_input(f"Designation", local_obj_exp.str_designation, key=f"designation_{local_obj_expIndex}")
                    local_obj_exp.str_startDate = local_obj_columns[0].text_input(f"Start Date", local_obj_exp.str_startDate, key=f"start_{local_obj_expIndex}")
                    local_obj_exp.str_endDate = local_obj_columns[1].text_input(f"End Date", local_obj_exp.str_endDate or "", key=f"end_{local_obj_expIndex}")
                    local_obj_exp.str_location = local_obj_columns[2].text_input(f"Location", local_obj_exp.str_location or "", key=f"location_{local_obj_expIndex}")
                    local_obj_exp.list_rolesAndResponsibilities = st.text_area(f"Roles & Responsibilities (one per line)", "\n".join(local_obj_exp.list_rolesAndResponsibilities), key=f"roles_{local_obj_expIndex}").splitlines()

        with st.expander("Education", expanded=False):
            for local_obj_eduIndex, local_obj_edu in enumerate(local_obj_resume.list_education):
                local_obj_columns = st.columns((1,1))
                local_obj_edu.str_institutionName = local_obj_columns[0].text_input(f"Institution Name", local_obj_edu.str_institutionName, key=f"edu_institution_{local_obj_eduIndex}")
                local_obj_edu.str_degree = local_obj_columns[1].text_input(f"Degree", local_obj_edu.str_degree, key=f"edu_degree_{local_obj_eduIndex}")
                local_obj_columns = st.columns((1,1,1,1))
                local_obj_edu.str_startDate = local_obj_columns[0].text_input(f"Start Date", local_obj_edu.str_startDate, key=f"edu_start_{local_obj_eduIndex}")
                local_obj_edu.str_endDate = local_obj_columns[1].text_input(f"End Date", local_obj_edu.str_endDate or "", key=f"edu_end_{local_obj_eduIndex}")
                local_obj_edu.str_grade = local_obj_columns[2].text_input(f"Grade", local_obj_edu.str_grade or "", key=f"edu_grade_{local_obj_eduIndex}")
                local_obj_edu.str_location = local_obj_columns[3].text_input(f"Location", local_obj_edu.str_location or "", key=f"edu_location_{local_obj_eduIndex}")
                local_obj_edu.str_description = st.text_area(f"Description", local_obj_edu.str_description or "", key=f"edu_desc_{local_obj_eduIndex}")

        with st.expander("Projects", expanded=False):
            for local_obj_projIndex, local_obj_proj in enumerate(local_obj_resume.list_projects):
                with st.container(border=True):
                    local_obj_proj.str_projectTitle = st.text_input(f"Project Title", local_obj_proj.str_projectTitle or "", key=f"proj_title_{local_obj_projIndex}", label_visibility="collapsed")
                    local_obj_proj.list_projectContents = st.text_area(f"Project Description (one per line)", "\n".join(local_obj_proj.list_projectContents or []), key=f"proj_desc_{local_obj_projIndex}", label_visibility="collapsed").splitlines()

        with st.expander("Achievements", expanded=False):
            local_obj_achievementsStr = st.text_area("Achievements (one per line)", "\n".join(local_obj_resume.list_achievements), key="achievements")
            local_obj_resume.list_achievements = [a.strip() for a in local_obj_achievementsStr.splitlines() if a.strip()]

        local_button_export = st.button("Export Resume", key="export_resume")
        
        if local_button_export:
            # Here you would implement the logic to export the resume, e.g., to a PDF or DOCX file.
            self.export(local_obj_resume)
        
        return local_obj_resume

    
    def export(self, param_obj_resume:CandidateResume):
        """
        Export the resume to a file format like PDF or DOCX.
        This function would typically involve generating a document from the resume data.
        """
        # Placeholder for export logic
        local_obj_exporter = ResumeExporter()
        local_obj_exporter.export(param_obj_resume)

        # You can implement the actual export logic here, e.g., using a library like ReportLab or python-docx.


