from pydantic import BaseModel, Field
from ..templates import ResumeTemplates
from ..builder.builder import CandidateResume


class ExporterInput(BaseModel):
    """
    Base class for exporter input data.
    This class is used to define the structure of the exporter input data.
    """
    str_templateName: str = Field("simple", description="Name of the template to be used for exporting the resume")
    obj_resume: CandidateResume  = Field(..., description="Resume object containing all the details to be exported")
    str_exportPath: str  = Field(..., description="Path where the exported pdf resume will be saved")
class Exporter:
    
    def __init__(self):
        ...
    
    def export(self, param_obj_input:ExporterInput) -> None:
        
        """
        Exports the resume to a PDF file using the specified template.
        
        :param param_obj_resume: CandidateResume object containing all the details to be exported
        :param param_str_templateName: Name of the template to be used for exporting the resume
        """
        ...
    
    def _create_latex_resume(self, param_obj_resume:CandidateResume, param_str_resumeName:str):
        ...
    
    def _save_pdf_resume(self, param_str_latexString:str, param_str_saveToPath:str):
        ...