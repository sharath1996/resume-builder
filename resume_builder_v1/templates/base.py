from ..builder.builder import CandidateResume

class BaseResume:

    def __init__(self):
        ...
    
    def build(self, param_obj_input: CandidateResume) -> str:
        """
        Build the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to export the resume in desired latex format.")
    
    def _add_header(self) -> str:
        """
        Add the header for the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to add the header for the resume.")
    
    def _add_candidate_details(self, param_obj_input: CandidateResume) -> str:
        """
        Add the candidate's details to the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to add candidate details to the resume.")
    
    def _add_summary(self, param_obj_input: CandidateResume) -> str:
        """
        Add the summary section to the resume.
        
        """
        raise NotImplementedError("Subclasses should implement this method to add the summary section to the resume.")
    
    def _add_skills(self, param_obj_input: CandidateResume) -> str:
        """
        Add the skills section to the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to add the skills section to the resume.")
    
    def _add_work_experience(self, param_obj_input: CandidateResume) -> str:
        """
        Add the work experience section to the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to add the work experience section to the resume.")
    
    def _add_education(self, param_obj_input: CandidateResume) -> str:
        """
        Add the education section to the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to add the education section to the resume.")
    
    def _add_achievements(self, param_obj_input: CandidateResume) -> str:
        """
        Add the achievements section to the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to add the achievements section to the resume.")
    
    def _add_projects(self, param_obj_input: CandidateResume) -> str:
        """
        Add the projects section to the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to add the projects section to the resume.")