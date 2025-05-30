from pydantic import BaseModel,SerializeAsAny
import json
from .portfolio import PortFolioExtractor
from .llm_generator import WorkDescriptionGenerator, WorkDescriptionRequest
from .llm_generator import SkillGeneratorInput, SkillGenerator
from .llm_generator import AchievementGenerator, AchievementGeneratorInput
import streamlit as st

class ProjectPairs(BaseModel):
    str_projectName:str
    int_numberOfPoints:int

class ResumeBuilderInput(BaseModel):

    str_jobDescription:str = ""
    list_adiProjects:SerializeAsAny[list[ProjectPairs]] = []
    list_mbrdiProjects:SerializeAsAny[list[ProjectPairs]] = []

class ResumeBuilder:

    def __init__(self):
        with open(r'template\common_data.json') as local_file_jsonFile:
            self._dict_baseDict = json.load(local_file_jsonFile)
    
    def create(self, param_obj_resumeBuilderInput:ResumeBuilderInput):
        
        local_dict_adiWork, local_dict_mbrdiWork = self._get_job_description(param_obj_resumeBuilderInput)
        
        self._dict_baseDict['work_experience'][0]['description'] = local_dict_adiWork
        self._dict_baseDict['work_experience'][1]['description'] = local_dict_mbrdiWork
        local_dict_skills = self._get_skills(param_obj_resumeBuilderInput.str_jobDescription, self._dict_baseDict)
        self._dict_baseDict['skills']['Languages'] = local_dict_skills['list_programmingLanguages']
        self._dict_baseDict['skills']['Tools'] = local_dict_skills['list_tools']
        self._dict_baseDict['skills']['Skills'] = local_dict_skills['list_skills']
        self._dict_baseDict['achievements'] = self._get_achivements(param_obj_resumeBuilderInput.str_jobDescription)
        return self._dict_baseDict

    def _get_job_description(self,param_obj_resumeBuilderInput:ResumeBuilderInput):

        local_obj_projectExtractor = PortFolioExtractor(r'portfolio')
        
        ## ADI Work
        local_dict_adiWork = {}
        for local_obj_projectPair in param_obj_resumeBuilderInput.list_adiProjects:
            local_str_projectText = local_obj_projectExtractor.extract("ADI", local_obj_projectPair.str_projectName)
            
            local_obj_wrkDscrReq = WorkDescriptionRequest()
            local_obj_wrkDscrReq.str_jobDescription = param_obj_resumeBuilderInput.str_jobDescription
            local_obj_wrkDscrReq.str_projectDescription = local_str_projectText
            local_obj_wrkDscrReq.int_numberOfPoints = local_obj_projectPair.int_numberOfPoints
            local_obj_workDescriptionGenerator = WorkDescriptionGenerator()
            local_dict_workDescriptionGenerated = local_obj_workDescriptionGenerator.generate(local_obj_wrkDscrReq)
            local_dict_adiWork[local_dict_workDescriptionGenerated['str_projectName']] = local_dict_workDescriptionGenerated['list_experience']
            st.toast(f"Generated {local_obj_wrkDscrReq.int_numberOfPoints} points for {local_obj_projectPair.str_projectName}")

        ### MBRDI Work
        local_dict_mbrdiWork = {}
        for local_obj_projectPair in param_obj_resumeBuilderInput.list_mbrdiProjects:
            local_str_projectText = local_obj_projectExtractor.extract("MBRDI", local_obj_projectPair.str_projectName)
            
            local_obj_wrkDscrReq = WorkDescriptionRequest()
            local_obj_wrkDscrReq.str_jobDescription = param_obj_resumeBuilderInput.str_jobDescription
            local_obj_wrkDscrReq.str_projectDescription = local_str_projectText
            local_obj_wrkDscrReq.int_numberOfPoints = local_obj_projectPair.int_numberOfPoints

            local_obj_workDescriptionGenerator = WorkDescriptionGenerator()
            local_dict_workDescriptionGenerated = local_obj_workDescriptionGenerator.generate(local_obj_wrkDscrReq)
            local_dict_mbrdiWork[local_dict_workDescriptionGenerated['str_projectName']] = local_dict_workDescriptionGenerated['list_experience']
            st.toast(f"Generated {local_obj_wrkDscrReq.int_numberOfPoints} points for {local_obj_projectPair.str_projectName}")

        return local_dict_adiWork,local_dict_mbrdiWork
        
    def _get_skills(self, param_str_jobDescription:str, param_dict_json:dict):
        local_obj_skillGeneratorInput = SkillGeneratorInput(str_jobDescription=param_str_jobDescription, dict_currentResume=param_dict_json)
        local_obj_skillGenerator = SkillGenerator()
        local_dict_skills = local_obj_skillGenerator.generate_skills(local_obj_skillGeneratorInput)
        st.toast(f"Generated skills")
        return local_dict_skills
    
    def _get_achivements(self, param_str_jobDescription:str):

        with open('portfolio//achievements//papers.md') as local_file_paper:
            local_str_paperDescription = local_file_paper.read()
            
        
        with open('portfolio//achievements//patents.md') as local_file_patent:
            local_str_patentDescription = local_file_patent.read()
        
        local_obj_achivementInputs = AchievementGeneratorInput(
            str_jobDescription=param_str_jobDescription,
            str_paperDocs=local_str_paperDescription,
            str_patentDocs=local_str_patentDescription
        )
        local_obj_achievementGenerator = AchievementGenerator()
        local_list_achievments = local_obj_achievementGenerator.generate(local_obj_achivementInputs)
        st.toast(f"Generated descriptions")
        return local_list_achievments