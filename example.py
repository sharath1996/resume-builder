from resume_builder.builders.builder import ResumeBuilder, ResumeBuilderInput, ProjectPairs
import json
from resume_builder.builders.latex import LatexResumeBuilder


local_str_jobInputs = """
"""
local_list_adiProjects = [ProjectPairs(str_projectName="sw_agents", int_numberOfPoints=10)]
local_list_mbrdiProjects = [ProjectPairs(str_projectName="IOTesting", int_numberOfPoints=4)]




local_obj_resumeBuilderInput = ResumeBuilderInput(str_jobDescription=local_str_jobInputs,
                                                list_adiProjects=local_list_adiProjects,
                                                list_mbrdiProjects=local_list_mbrdiProjects)
local_dict_output = ResumeBuilder().create(local_obj_resumeBuilderInput)

with open('resume.json', 'w') as fileName:
    json.dump(local_dict_output, fileName, indent=4)



with open('resume.json') as local_file_inputFile:
    local_dict_json = json.load(local_file_inputFile)

local_obj_resumeBuilder = LatexResumeBuilder()
local_obj_resumeBuilder.generate(local_dict_json)