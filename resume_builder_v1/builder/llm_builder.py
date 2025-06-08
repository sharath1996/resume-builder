from .types import CandidateDetails, CandidateResume, Skill, Experience, Education, Project
from ..database.db import Profile
from pydantic import BaseModel, Field


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
        ...
        
        

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
    
    def build(self, param_obj_input:LLMBuilderInput) -> list[Skill]:
        ...

class BuildExperience:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> list[Experience]:
        ...

class BuildEducation:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> list[Education]:
        ...

class BuildProjects:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> list[Project]:
        ...

class BuildAchievements:

    def __init__(self):
        ...
    
    def build(self, param_obj_input:LLMBuilderInput) -> list[str]:
        # Assuming achievements are stored as a list of strings in the Profile
        ...