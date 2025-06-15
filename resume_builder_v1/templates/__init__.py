from .standard_eu import StandardEU
from .base import BaseResume
from .standard_us import StandardUS
from .colorful_eu import ColorfulEU

class ResumeTemplates:

    def __init__(self):
        ...
    
    def list_available_templates(self) -> list[str]:
        """
        List all available resume templates.
        """
        return ["standard_eu", "standard_us", "colorful_eu"]
    
    def get_template(self, param_str_templateName:str)->BaseResume:

        if param_str_templateName == "standard_eu":
            return StandardEU()
        
        elif param_str_templateName == "standard_us":
            return StandardUS()
        
        elif param_str_templateName == "colorful_eu":
            return ColorfulEU()
        
        else:
            raise ValueError(f"Template {param_str_templateName} not found.")