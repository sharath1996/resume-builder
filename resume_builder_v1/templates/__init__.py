from .simple import SimpleResume
from .base import BaseResume

class ResumeTemplates:

    def __init__(self):
        ...
    
    def list_available_templates(self) -> list[str]:
        """
        List all available resume templates.
        """
        return ["simple"]
    
    def get_template(self, param_str_templateName:str)->BaseResume:

        if param_str_templateName == "simple":
            return SimpleResume()
        
        else:
            raise ValueError(f"Template {param_str_templateName} not found.")