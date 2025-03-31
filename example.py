from resume_builder.builders.latex import LatexResumeBuilder
import json

with open('examples//input_data.json') as local_file_inputFile:
    local_dict_json = json.load(local_file_inputFile)

local_obj_resumeBuilder = LatexResumeBuilder()
local_obj_resumeBuilder.generate(local_dict_json)