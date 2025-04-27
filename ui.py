import streamlit as st
from resume_builder.builders.builder import ResumeBuilder, ResumeBuilderInput, ProjectPairs
from resume_builder.builders.llm_generator import CoverLetterGenerator, CoverLetterInputs
import json
from resume_builder.builders.latex import LatexResumeBuilder
import json

local_list_adiProjects = ['cell_simulator', 'simulator_dev', 'sw_agents']
local_list_mbrdiProjects = ['IOTesting', 'Multicore', 'NCT']

st.title("Resume Builder V1")

local_col_jd, local_col_projects = st.columns(2)
local_str_jobDescription = local_col_jd.text_area(label="Job Description for which you need to apply", value="Update JD here")
local_col_projects.markdown("### ADI Projects")
local_dict_ADIcounter = {}

for local_str_adiProject in local_list_adiProjects:
    local_int_counter = local_col_projects.number_input(f"{local_str_adiProject} points", value=0, key=f"{local_str_adiProject}_adi_count")
    local_dict_ADIcounter[local_str_adiProject] = local_int_counter

local_col_projects.markdown("### MBRDI Projects")
local_dict_MRDICounter = {}
for local_str_mbrdiProject in local_list_mbrdiProjects:
    local_int_counter = local_col_projects.number_input(f"{local_str_mbrdiProject} points", value=0, key=f"{local_str_mbrdiProject}_adi_count")
    local_dict_MRDICounter[local_str_mbrdiProject] = local_int_counter

local_button_generate = local_col_projects.button("Generate Resume")


if local_button_generate:
    with st.spinner("Generating resume...."):
        local_list_adiPairs = []
        for local_str_project in local_dict_ADIcounter:
            local_int_counter = local_dict_ADIcounter[local_str_project]
            if local_int_counter >0:
                local_list_adiPairs.append(ProjectPairs(str_projectName=local_str_project, int_numberOfPoints=local_int_counter))
        
        local_list_mdrdiPairs = []
        for local_str_project in local_dict_MRDICounter:
            local_int_counter = local_dict_MRDICounter[local_str_project]
            if local_int_counter >0:
                local_list_mdrdiPairs.append(ProjectPairs(str_projectName = local_str_project, int_numberOfPoints=local_int_counter))

        local_obj_resumeBuilderInput = ResumeBuilderInput(str_jobDescription=local_str_jobDescription,
                                                    list_adiProjects=local_list_adiPairs,
                                                    list_mbrdiProjects=local_list_mdrdiPairs)
        local_dict_output = ResumeBuilder().create(local_obj_resumeBuilderInput)

        with open('resume.json', 'w') as fileName:
            json.dump(local_dict_output, fileName, indent=4)
        
        with open('resume.json') as local_file_inputFile:
            local_dict_json = json.load(local_file_inputFile)

        local_obj_resumeBuilder = LatexResumeBuilder()
        local_obj_resumeBuilder.generate(local_dict_json)

        st.success("Resume Generated!!!")


