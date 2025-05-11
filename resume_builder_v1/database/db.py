
from pydantic import BaseModel

class Profile(BaseModel):
    ...
    
class ProfileDataBase:

    def __init__(self):
        ...
    
    def read(self, param_str_profileName:str):
        ...
    
    def create(self, param_str_profileName:str, param_obj_profile:dict):
        ...
    
    def update(self, param_str_profileName:str, param_obj_profile:dict):
        ...
    
    def delete(self, param_str_profileName:str):
        ...

    def read_all_profiles(self)->list[str]:
        ...