from ..builder.builder import CandidateResume

class BaseResume:

    def __init__(self):
        ...
    
    def build(self, param_obj_input: CandidateResume) -> str:
        """
        Build the resume.
        """
        raise NotImplementedError("Subclasses should implement this method to export the resume in desired latex format.")