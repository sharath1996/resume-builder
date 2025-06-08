
import openai


class LLM:

    def __init__(self, param_str_modelName:str):
        ...
    
    def add_system_prompt(self, param_str_systemPrompt:str):
        ...
    
    def add_user_prompt(self, param_str_userPrompt:str):
        ...
    
    def get_answer(self):
        ...
    
    def get_structured_output(self):
        ...

    