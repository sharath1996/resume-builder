import json
from textwrap import dedent
from openai import OpenAI
import os
from pydantic import BaseModel, Field

class LLMRepsonse(BaseModel):
    list_experience :list[str] = Field(..., description="List of points that are extracted from project")

class LLMRequest(BaseModel):
    str_jobDescription :str = ""
    str_projectDescription:str = ""
    str_additionalInstructions : str|None = None
    int_numberOfPoints: int = 10


class WorkDescriptionGenerator:

    def __init__(self):
        self._obj_openAi = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    
    def generate(self, param_obj_llmRequest:LLMRequest):

        local_str_prompt = "This is the job description:\n"
        local_str_prompt += param_obj_llmRequest.str_jobDescription
        local_str_prompt += "\n\nThis is the project that I am working on"
        local_str_prompt += param_obj_llmRequest.str_projectDescription
        local_str_prompt += dedent(f"""
        I am trying to add a work-experience section in my resume based on the given project for the given job description. This section contains a bullet points that I should be inserting in the main resume.
        Your job is to generate the bullet points for the given job description. Note that, the points should be clear, consice and effective in what is the project is all about.
        Your points should contain the following:
        - Brief idea on the project
        - Technical complexities and solution
        - Key highlights that are relavant to the job descriptions.
        - KPIs if any that are relavant to the hob description.
        - Tools and technologies used
        - You should generate {param_obj_llmRequest.int_numberOfPoints} bullet points in detail.
        - Do not use any "%" symbols
        """)


        if param_obj_llmRequest.str_additionalInstructions:
            local_str_prompt += f"Additional Instructions = {param_obj_llmRequest.str_additionalInstructions}"

        local_dict_messages = {"role": "user", "content":local_str_prompt}

        local_str_response = self._obj_openAi.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[local_dict_messages],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
        response_format=LLMRepsonse
        )

        local_str_json =  local_str_response.choices[0].message.content
        return json.loads(local_str_json)


