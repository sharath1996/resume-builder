from textwrap import dedent
from .types import CandidateDetails, CandidateResume, Skills, WorkExperiences, Educations, Projects, Achivements
from ..database.db import Profile
from pydantic import BaseModel, Field
from ..llm import LLMFactory


class LLMBuilderInput(BaseModel):
    """
    Input data for the LLMBuilder.
    This class is used to define the structure of the input data for building a resume.
    """
    obj_profile: Profile = Field(..., description="Profile object containing all necessary information")
    str_jobDescription: str | None = Field(None, description="Job description for the position being applied for")
    str_additionalInstructions: str | None = Field(None, description="Any additional instructions for the LLM")

class LLMBuilder:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> CandidateResume:
        
        """
        Build a candidate resume from the input data.
        This method orchestrates the building of various components of the resume.
        """
        local_obj_candidateDetails = BuildCandidateDetails().build(param_obj_input)
        local_list_skills = BuildSkills().build(param_obj_input)
        local_list_experience = BuildExperience().build(param_obj_input)
        local_list_education = BuildEducation().build(param_obj_input)
        local_list_projects = BuildProjects().build(param_obj_input)
        local_list_achievements = BuildAchievements().build(param_obj_input)
        
        local_obj_candidateResume = CandidateResume(
            str_fullName=local_obj_candidateDetails.str_fullName,
            str_currentResidence=local_obj_candidateDetails.str_currentResidence,
            str_contactNumber=local_obj_candidateDetails.str_contactNumber,
            str_linkedInProfile=local_obj_candidateDetails.str_linkedInProfile,
            str_githubProfile=local_obj_candidateDetails.str_githubProfile,
            str_customProfile=local_obj_candidateDetails.str_customProfile,
            str_aboutCandidate=local_obj_candidateDetails.str_aboutCandidate,
            list_skills = local_list_skills.list_skills,
            list_workExperience = local_list_experience.list_workExperience,
            list_education = local_list_education.list_education,
            list_projects = local_list_projects.list_projects,
            list_achievements = local_list_achievements.list_achievements
            )
        
        return local_obj_candidateResume

class BuildCandidateDetails:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput)-> CandidateDetails:
        """
        Build candidate details from the input data.
        This method extracts and formats the candidate's personal information.
        """
        
        local_obj_profile = param_obj_input.obj_profile.obj_profileInfo
        return CandidateDetails(
            str_fullName=local_obj_profile.str_fullName,
            str_currentResidence=local_obj_profile.str_currentResidence,
            str_contactNumber=local_obj_profile.str_contactNumber,
            str_linkedInProfile=local_obj_profile.str_linkedInProfile,
            str_githubProfile=local_obj_profile.str_githubProfile,
            str_customProfile=local_obj_profile.str_customProfile,
            str_aboutCandidate=local_obj_profile.str_aboutCandidate
        )
    

class BuildSkills:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> Skills:
        
        local_list_availableSkills = []

        for local_obj_workExperience in param_obj_input.obj_profile.list_workExperience:
            local_list_availableSkills.extend(local_obj_workExperience.list_skills)
        
        local_list_availableSkills = list(set(local_list_availableSkills))

        if param_obj_input.str_jobDescription is not None:
            local_obj_skills = self._get_skills_relevant_to_job(local_list_availableSkills, param_obj_input.str_jobDescription)
        else:
            local_obj_skills = Skills(list_skills=local_list_availableSkills)
        # Ensure the skills are unique
        
        return local_obj_skills
    
    def _get_skills_relevant_to_job(self, param_list_availableSkills:list, param_str_jobDescription:str):

        local_obj_llm = LLMFactory.get_llm_interface()
        
        local_str_systemPrompt = dedent("""
        You are a helpful resume writer assistant, who will be responsible to figure out the skills that are needed for the given job description and available skills
        You will be given a job description and list of the skills that candidate has.
        Your job is to group the skills into multiple sections such as Languages, tools, frameworks and so on (These are not limited to). 
        Th sections should be aligned to the given job description.
        You should be forming the sections and send the responses in json format.
        There might be duplicate of skills could be available.

        This resume will be written in latex, hence make sure that your responses are compatible in latex 
        And use the special characters with appropriate syntax (such as # should be written as \# , & with \&)
        """)

        local_str_userPrompt = f"Given the job description : \n {param_str_jobDescription}"

        local_str_userPrompt += f"Applicant's skills : \n {", ".join(param_list_availableSkills)}"

        local_obj_llm.clear_messages()
        local_obj_llm.add_system_prompt(local_str_systemPrompt)
        local_obj_llm.add_user_prompt(local_str_userPrompt)
        local_obj_skills = local_obj_llm.get_structured_output(Skills)

        return local_obj_skills

class BuildExperience:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> WorkExperiences:
        """
        Build work experiences from the input data using LLM.
        """
        local_obj_llm = LLMFactory.get_llm_interface()
        local_str_systemPrompt = dedent("""
        You are a helpful resume writer assistant. Extract and structure the candidate's work experience from the provided profile. 
        Group responsibilities, roles, and achievements for each position. Return the result in JSON format compatible with the WorkExperiences pydantic model. 
        Ensure all LaTeX special characters are properly escaped (e.g., # as \#, & as \&).
        """)
        local_str_userPrompt = f"Candidate profile: {str(param_obj_input.obj_profile.list_workExperience)}"
        local_obj_llm.clear_messages()
        local_obj_llm.add_system_prompt(local_str_systemPrompt)
        local_obj_llm.add_user_prompt(local_str_userPrompt)
        local_obj_experience = local_obj_llm.get_structured_output(WorkExperiences)
        return local_obj_experience

class BuildEducation:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> Educations:
        """
        Build education details from the input data using LLM.
        """
        local_obj_llm = LLMFactory.get_llm_interface()
        local_str_systemPrompt = dedent("""
        You are a helpful resume writer assistant. Extract and structure the candidate's education history from the provided profile. 
        Return the result in JSON format compatible with the Educations pydantic model. 
        Ensure all LaTeX special characters are properly escaped (e.g., # as \#, & as \&).
        """)
        local_str_userPrompt = f"Candidate profile: {param_obj_input.obj_profile.list_education}"
        local_obj_llm.clear_messages()
        local_obj_llm.add_system_prompt(local_str_systemPrompt)
        local_obj_llm.add_user_prompt(local_str_userPrompt)
        local_obj_education = local_obj_llm.get_structured_output(Educations)
        return local_obj_education


class BuildProjects:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> Projects:
        """
        Build projects from the input data using LLM.
        """
        local_obj_llm = LLMFactory.get_llm_interface()
        local_str_systemPrompt = dedent("""
        You are a helpful resume writer assistant. Extract and structure the candidate's projects from the provided profile. 
        Return the result in JSON format compatible with the Projects pydantic model. 
        Ensure all LaTeX special characters are properly escaped (e.g., # as \#, & as \&).
        """)
        local_str_userPrompt = ""
        for local_obj_project in param_obj_input.obj_profile.list_professionalProjects:
            local_str_userPrompt += f"Project: {local_obj_project.str_projectTitle}, Description: {local_obj_project.str_projectContents}\n"
        local_obj_llm.clear_messages()
        local_obj_llm.add_system_prompt(local_str_systemPrompt)
        local_obj_llm.add_user_prompt(local_str_userPrompt)
        local_obj_projects = local_obj_llm.get_structured_output(Projects)
        return local_obj_projects

# TODO: This whole class needs to be refactored to use LLM for building achievements, this is not at all the right way to do it.
class BuildAchievements:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> Achivements:
        """
        Build achievements from the input data using LLM.
        """
        local_obj_llm = LLMFactory.get_llm_interface()
        local_str_systemPrompt = dedent("""
        You are a helpful resume writer assistant. Extract and structure the candidate's achievements, awards, and certifications from the provided profile. 
        Return the result in JSON format compatible with the Achivements pydantic model. 
        Ensure all LaTeX special characters are properly escaped (e.g., # as \#, & as \&).
        """)
        local_str_userPrompt = ""

        # Papers
        if param_obj_input.obj_profile.list_papers:
            for local_obj_paper in param_obj_input.obj_profile.list_papers:
                local_str_userPrompt += f"Paper published: {local_obj_paper.str_paperTile}, Description: {local_obj_paper.str_abstract},\n URL : {local_obj_paper.str_hyperLink}\n"
        
        # Patents
        if param_obj_input.obj_profile.list_patents:
            for local_obj_patent in param_obj_input.obj_profile.list_patents:
                local_str_userPrompt += f"Patent: {local_obj_patent.str_patentTitle}, Description: {local_obj_patent.str_abstract},\n"
            
        # Talks
        if param_obj_input.obj_profile.list_talks:
            for local_obj_talk in param_obj_input.obj_profile.list_talks:
                local_str_userPrompt += f"Talk: {local_obj_talk.str_title}, Description: {local_obj_talk.str_abstract},\n at : {local_obj_talk.str_place}\n"
            
        # Certifications
        for local_obj_certification in param_obj_input.obj_profile.list_certifcations:
            local_str_userPrompt += f"Certification: {local_obj_certification.str_name}, Issuing Authority: {local_obj_certification.str_issuingAuthority},\n"

        # TODO: Add Awards
        # for local_obj_award in param_obj_input.obj_profile.list_awards:
        #     local_str_userPrompt += f"Award: {local_obj_award.str_awardTitle}, Description: {local_obj_award.str_abstract},\n"
        

        local_obj_llm.clear_messages()
        local_obj_llm.add_system_prompt(local_str_systemPrompt)
        local_obj_llm.add_user_prompt(local_str_userPrompt)
        local_obj_achievements = local_obj_llm.get_structured_output(Achivements)
        return local_obj_achievements