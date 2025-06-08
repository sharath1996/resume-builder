from pydantic import BaseModel, Field
from ..database.db import Profile, ProfileDataBase
from .types import CandidateResume
from .llm_builder import LLMBuilderInput, LLMBuilder



class ResumeBuilderInput(BaseModel):
    """
    """
    str_jobDescription:str = Field(..., description="Job description for which the resume is being built")
    str_additionalInstructionsAndNotes: str | None = Field(None, description="Any additional instructions or notes for the resume builder")
    str_profileName: str = Field(..., description="Candidate name")


class ResumeBuilder:

    def __init__(self):
        ...
    
    def build(self, param_obj_input: ResumeBuilderInput)-> CandidateResume:
        """
        Build the resume.
        """
        local_obj_profileData = self._get_profile_data(param_obj_input.str_profileName)
        local_obj_llmBuilderInput = LLMBuilderInput(
            obj_profile=local_obj_profileData,
            str_jobDescription=param_obj_input.str_jobDescription,
            str_additionalInstructions=param_obj_input.str_additionalInstructionsAndNotes
        )
        local_obj_llmBuilder = LLMBuilder()
        local_obj_candidateResume = local_obj_llmBuilder.build(local_obj_llmBuilderInput)
        return local_obj_candidateResume

    
    def _get_profile_data(self, param_str_profileName: str) -> Profile:
        """
        Get the profile data from the database.
        """
        local_obj_profileDataBase = ProfileDataBase()
        local_obj_profile = local_obj_profileDataBase.read(param_str_profileName)
        return local_obj_profile
