import json
from textwrap import dedent
from typing import Type
from openai import OpenAI
import os
from pydantic import BaseModel, Field

class WorkDescriptionResponse(BaseModel):
    
    str_projectName:str = Field(..., description="Name of the project")
    list_experience :list[str] = Field(..., description="List of points that are extracted from project")

class WorkDescriptionRequest(BaseModel):
    str_jobDescription :str = ""
    str_projectDescription:str = ""
    str_additionalInstructions : str|None = None
    int_numberOfPoints: int = 10


class WorkDescriptionGenerator:

    def __init__(self):
        ...

    def generate(self, param_obj_llmRequest:WorkDescriptionRequest):

        local_str_prompt = "This is the job description:\n"
        local_str_prompt += param_obj_llmRequest.str_jobDescription
        local_str_prompt += "\n\nThis is the project that I am working on"
        local_str_prompt += param_obj_llmRequest.str_projectDescription
        local_str_prompt += dedent(f"""
        I am trying to add a work-experience section in my resume based on the given project for the given job description. This section contains a bullet points that I should be inserting in the main resume.
        Your job is to generate the bullet points for the given job description. Note that, the points should be clear, consice and effective in what is the project is all about.
        Your points should contain the following:
        - Brief idea on the project
        - Technical complexities and solution in detail
        - Key highlights that are relavant to the job descriptions with technical depth.
        - KPIs if any that are relavant to the hob description.
        - Tools and technologies used
        - You should generate {param_obj_llmRequest.int_numberOfPoints} bullet points in detail.
        - Do not use any "%" symbols
        """)


        if param_obj_llmRequest.str_additionalInstructions:
            local_str_prompt += f"Additional Instructions = {param_obj_llmRequest.str_additionalInstructions}"

        
        local_obj_llm = LLMInference()
        local_obj_llmInput = LLMInputs(str_systemPrompt="", list_userPrompts=[local_str_prompt], obj_template=WorkDescriptionResponse)
        local_list_out = local_obj_llm.infer(local_obj_llmInput)
        return local_list_out
        

class SkillGeneratorInput(BaseModel):

    str_jobDescription:str = ""
    dict_currentResume:dict = {}

class SkillGeneratorOutput(BaseModel):
    list_programmingLanguages:list[str] = Field(..., description="List of the programming languages that are used in the given json resume")
    list_skills:list[str] = Field(..., description="List of skills that are relevant to job description and are present in the json resume")
    list_tools : list[str] = Field(..., description="List of the tools that are relevant to the job description and are present in the given json resume")
class SkillGenerator:

    def __init__(self):
        ...
    
    def generate_skills(self, param_obj_input:SkillGeneratorInput):
        
        local_str_sysPrompt = "You are an helpful assistant who can extract the programming languages, skills and tools from the given json resume according to the given job description"
        local_str_userPrompt = f"Json resume \n: {param_obj_input.dict_currentResume} "
        local_str_userPrompt += f"\n Job Description \n : {param_obj_input.str_jobDescription}"

        local_obj_llm = LLMInference()
        local_obj_llmInput = LLMInputs(str_systemPrompt=local_str_sysPrompt, list_userPrompts=[local_str_userPrompt], obj_template=SkillGeneratorOutput)
        local_list_out = local_obj_llm.infer(local_obj_llmInput)
        return local_list_out


class CoverLetterInputs(BaseModel):
    str_jobDescription:str = Field(..., description="Job Description")
    dict_jsonResume:dict = Field(..., description="Resume in Json format")

class CoverLetterOutput(BaseModel):
    str_coverLetter:str = Field(..., description="Cover Letter for the given job in markdown")


class CoverLetterGenerator:

    def __init__(self):
        ...
    
    def generate(self, param_obj_input:CoverLetterInputs):

        local_str_sysprompt= dedent("""
        You are an helpful assistant who can write the personalized cover letter to the hiring manager of the company depending on the job description and json resume.
        You should consider the following for the cover letter:
        Begin with a header that includes your name, contact details, and, if relevant, links to your portfolio or professional profiles. Address the letter with a greeting that personalizes it, using the hiring manager's name if available or a professional salutation like "Dear Hiring Manager." In the introduction, state who you are, the position you're applying for, and briefly highlight your strengths, demonstrating alignment with the job’s requirements. Mention any referrals if applicable.
        In the qualifications section, expand on your achievements and skills, focusing on how they meet the company’s needs. Use specific examples to show your impact and problem-solving abilities. Then, discuss your values and goals, showcasing your understanding of the company’s mission and how you’ll contribute to its culture. Align your professional aspirations with the organization’s objectives.
        Conclude with a call to action, summarizing your interest, expressing gratitude, and suggesting the next steps, like scheduling an interview. Always emphasize how your skills add value to the team.
        Generate a cover letter within 400 words.
        """)
        local_str_userPrompt = f"Job Description \n: {param_obj_input.str_jobDescription}"

        local_str_userPrompt += f"Json resume \n: {param_obj_input.dict_jsonResume}"

        local_obj_llm = LLMInference()
        local_obj_llmInput = LLMInputs(str_systemPrompt=local_str_sysprompt, list_userPrompts=[local_str_userPrompt], obj_template=CoverLetterOutput)
        local_dict_out = local_obj_llm.infer(local_obj_llmInput)
        return local_dict_out["str_coverLetter"]


class LLMInputs(BaseModel):
    str_systemPrompt :str = ""
    list_userPrompts : list[str] = ""
    obj_template:Type[BaseModel]|None = None

class LLMInference:

    def __init__(self):
        self._obj_openAi = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    
    def infer(self, param_obj_input:LLMInputs):

        local_list_messages = []
        if param_obj_input.str_systemPrompt != "":
            local_dict_message = {"role": "system", "content":param_obj_input.str_systemPrompt}
            local_list_messages.append(local_dict_message)
        
        for local_str_userMesage in param_obj_input.list_userPrompts:
            local_dict_message = {'role' : 'user', "content": local_str_userMesage}
            local_list_messages.append(local_dict_message)
        


        local_str_response = self._obj_openAi.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=local_list_messages,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
        response_format=param_obj_input.obj_template
        )

        local_str_json =  local_str_response.choices[0].message.content
        return json.loads(local_str_json)