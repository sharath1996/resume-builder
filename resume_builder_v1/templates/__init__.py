from .simple import SimpleResume
from .base import BaseResume

class ResumeTemplates:

    def __init__(self):
        ...
    
    def get_template(self, param_str_templateName:str)->BaseResume:

        if param_str_templateName == "simple":
            return SimpleResume()
        
        else:
            raise ValueError(f"Template {param_str_templateName} not found.")