from resume_builder.builders.builder import ResumeBuilder, ResumeBuilderInput, ProjectPairs
import json
from resume_builder.builders.latex import LatexResumeBuilder




with open('resume.json') as local_file_inputFile:
    local_dict_json = json.load(local_file_inputFile)

local_obj_resumeBuilder = LatexResumeBuilder()
local_obj_resumeBuilder.generate(local_dict_json)