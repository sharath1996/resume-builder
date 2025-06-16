from pydantic import BaseModel, Field
from ..templates import ResumeTemplates
from ..builder.builder import CandidateResume
import subprocess
import os
import logging

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
        local_str_latexResume = self._create_latex_resume(param_obj_input.obj_resume, param_obj_input.str_templateName)
        self._save_pdf_resume(local_str_latexResume, param_obj_input.str_exportPath)
    
    def _create_latex_resume(self, param_obj_resume:CandidateResume, param_str_resumeName:str):
        local_obj_resumeTemplate = ResumeTemplates().get_template(param_str_resumeName)
        local_str_latexResume = local_obj_resumeTemplate.build(param_obj_resume)
        return local_str_latexResume
    
    def _save_pdf_resume(self, param_str_latexString: str, param_str_saveToPath: str):
    # Ensure the directory exists
        os.makedirs(param_str_saveToPath, exist_ok=True)
        

        local_str_texResumePath = os.path.join(param_str_saveToPath, 'resume.tex')
        with open(local_str_texResumePath, 'w') as local_obj_file:
            local_obj_file.write(param_str_latexString)

        # Run pdflatex in the target directory
        local_obj_process = subprocess.Popen(
            ["pdflatex", "resume.tex"],
            cwd=param_str_saveToPath,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = local_obj_process.communicate()

        logging.info(stdout.decode())
        if stderr:
            logging.error(f"Error : {stderr.decode()}")