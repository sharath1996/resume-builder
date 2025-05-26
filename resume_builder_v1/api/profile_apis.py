from ..database.db import Profile,ProfileDataBase


class ProfileAPIs:

    def __init__(self):
        self._obj_db = ProfileDataBase()
    
    def create(self, param_str_profileName:str)->None:
        
        local_obj_profile = Profile()
        
        self._obj_db.create(param_str_profileName,local_obj_profile)
    
    def read(self, param_str_profileName:str)->Profile:
        
        return self._obj_db.read(param_str_profileName)

    
    def update(self, param_str_profileName:str, param_obj_profile:Profile)->None:
        
        self._obj_db.update(param_str_profileName, param_obj_profile)
    
    def delete(self, param_str_profileName:str)->None:
        
        self._obj_db.delete(param_str_profileName)
    
    def read_all_profiles(self)->list[str]:
        
        return self._obj_db.read_all_profiles()