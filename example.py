from resume_builder.builders.builder import ResumeBuilder, ResumeBuilderInput, ProjectPairs
import json
from resume_builder.builders.latex import LatexResumeBuilder


local_str_jobInputs = """
You will be part of the Qualcomm CR&D Software team that focuses on the overall system stability for an AI inferencing solution by building an environment closer to large-scale deployment.

In this role, the candidate will be working on a team responsible for testing drivers/features for Qualcomm’s Real-time OS and hardware blocks such as Neural Network processor, I2C/SPI controller, power management IC (PMIC) and PCIe.

The team contributes to testing throughout the life cycle, including unit, integration, and system-level testing. As a part of this team, your responsibilities would be to create complex test strategies, define user-oriented test case scenarios, automate/integrate those test cases as part of the automation framework and execute those test cases for a longer duration to find software stability issues. The role involves a good mix of hands on testing of the products and SW development of test cases and automation using a combination of Python and C++.

The candidate will be responsible for the development of test plans and automated test cases for new features.

You would be further doing the initial triage of the issues found and would work closely with various development, test and customer engineering teams to resolve such issues on priority.

Responsibilities

 Test development, troubleshooting and problem resolution on reference designs and customer platforms
 Test application design, coding and test development for system-on-chip products
 Interact in a team environment with developers, system engineers and testers
 Work closely with systems, software teams and test teams to develop test/test apps at both API level and system level for specific drivers, Artificial technologies like Deep learning, NLP and Computer vision, operating system and system level features like thermal mitigation, and power optimization
 Flexibility in work assignments and the ability to multi-task are crucial


Required Skills And Aptitudes

 Bachelor’s/Master’s degree in Computer Science or related field experience
 2+ years of relevant testing experience in System Testing preferable on embedded systems.
 Experience with ML frameworks such as PyTorch, Caffe2, TensorFlow
 Excellent programming skills in one or more programming languages (Python, Bash, C++)
 Excellent problem solving, analytical and debugging skills
 Experience in source control management like Git, Gerrit and Perforce.
 Excellent English communication (written and verbal) and interpersonal skills
 Interest in developing test cases and automation with strong programming skills (in C/C++)
 Good understanding of test methodology and test processes, including requirements collection, test plan development, and test case implementation
 Lab and hands-on debugging skills; ability to do initial debug and isolate failures
 A basic understanding of system-on-chip technologies will assure the success of the candidate
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