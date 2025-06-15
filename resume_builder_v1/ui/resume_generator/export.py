from ...builder.types import CandidateResume
from ...templates import ResumeTemplates
from ...exporter.exporter import ExporterInput,Exporter
import streamlit as st
import os

class ResumeExporter:

    def __init__(self):
        ...
    
    @st.fragment
    def export(self, param_obj_resume:CandidateResume):

        """
        Exports the resume to a PDF file using the specified template.
        
        :param param_obj_resume: CandidateResume object containing all the details to be exported
        """
        with st.container(border=True):
            st.subheader("Export Resume")
            st.write("Select a template and specify the export path to save your resume as a PDF file.")
            local_str_templateName = st.selectbox("Select Template", ResumeTemplates().list_available_templates(), key="export_template")
            local_str_exportPath = st.text_input("Export Path", value=".output/", key="export_path", help="Folder path where the resume will be saved. Ensure the folder exists.")
            
            # check wehter the path existis as folder or not using os.path.isdir
            if not os.path.isdir(local_str_exportPath):
                st.error(f"The specified export path '{local_str_exportPath}' does not exist. Please create the folder first.")
                return
            
            if st.button("Export Resume"):
                # create input object for exporter
                local_obj_exporterInput = ExporterInput(
                    str_templateName=local_str_templateName,
                    obj_resume=param_obj_resume,
                    str_exportPath=local_str_exportPath
                )

                # call the exporter
                local_obj_exporter = Exporter()
                local_obj_exporter.export(local_obj_exporterInput)
                st.success(f"Resume exported successfully to {local_str_exportPath}")