
from pydantic import BaseModel, Field, SerializeAsAny
from pymongo import MongoClient
from datetime import datetime

class ProfileInformation(BaseModel):
    str_fullName:str |None = Field(None, description="Full Name of the candidate")
    str_currentResidence:str | None = Field(None, description="Current residence of the candidate")
    str_contactNumber:str | None = Field(None, description= "Contact number including the country code")
    str_linkedInProfile:str | None = Field(None, description="LinkedIn Profile URL")
    str_githubProfile:str | None = Field(None, description="Github profile link")
    str_customProfile:str | None = Field(None, description="Any other custome Profile Link")
    str_aboutCandidate:str | None = Field(None, description="About the candidate")

class Project(BaseModel):
    str_projectTitle:str | None = Field(None, description="Title of the project")
    str_projectContents:str | None = Field(None, description="Description of the project in detail")
    list_highlights:str | None = Field(None, description="Top highlights of this project")

class Roles(BaseModel):
    dateTime_startDate:datetime|None = Field(None, description="Start date of the role")
    dateTime_endDate:datetime|str|None = Field(None, description="End date, it can include `Present`")
    str_title:str|None = Field(None, description="Title of the role or designation")
    str_place:str|None = Field(None, description="Place")
    list_projects:list[Project] =  Field(None, description="List of the projects handled")
    list_achievements:list[str|None]  = Field([], description="List of achivements in this role")
    list_skills : list[str|None] = Field([], description="List of skills")

class WorkExperience(BaseModel):
    str_companyName:str
    list_roles:list[Roles]

class Education(BaseModel):
    str_institutionName:str|None = Field(None, description="Name of the Institution")
    str_degree:str|None = Field(None, description="Name of the degree")
    datetime_startDate:datetime|None = Field(None, description="Start date of the education")
    datetime_endDate:datetime|None = Field(None, description="End date of the degree")
    str_grade:str|None = Field(None, description="Grade Obtained")
    str_place:str|None = Field(None, description="Name of the place, where you obtained the degree")
    list_projects:list[Project|None] = Field(None, description="List of the projects")

class Certification(BaseModel):
    str_name:str|None = Field(None, description="Certification Name")
    str_issuingAuthority:str|None = Field(None, description="Name of the issuing Authority")
    datetime_issueDate:datetime|None = Field(None, description="Date of issuing")

class Papers(BaseModel):
    str_paperTile:str|None = Field(None, description="Title of the paper")
    str_abstract:str|None = Field(None, description="Abstract of the paper")
    str_publisherDetails:str|None = Field(None, description="Publisher details")
    str_hyperLink:str|None = Field(None, description="Link for publication")
    datetime_publicationDate:str|None = Field(None,description="Date of Publication")

class Patents(BaseModel):
    str_patentTitle:str|None = Field(None, description="Title of the patent")
    str_abstract:str|None = Field(None, description="Abstract of the paper")
    str_patentOffice:str|None = Field(None, description="Patent office name")
    datetime_publicationDate:str|None = Field(None, description="Datetime of the publication")

class Talks(BaseModel):
    str_title:str|None = Field(None, description="Title of the talk")
    str_abstract:str|None = Field(None, description="Abstract of the talk")
    str_place:str|None = Field(None, description="Place/Event of the talk")
    datetime_date:str|None = Field(None, description="Date of the talk")


class JobApplications(BaseModel):
    str_jobDescriptions:str|None = Field(None, description="Job Description")
    dict_jsonResume:dict|None = Field({}, description="Generated Resume")


class Profile(BaseModel):
    obj_profileInfo : SerializeAsAny[ProfileInformation]
    list_workExperience: SerializeAsAny[list[WorkExperience]] = []
    list_education:SerializeAsAny[list[Education]] = []
    list_certifcations:SerializeAsAny[list[Certification]] = []
    list_papers:SerializeAsAny[list[Papers]] = []
    list_patents:SerializeAsAny[list[Patents]] = []
    list_talks:SerializeAsAny[list[Talks]] = []
    list_jobApps:SerializeAsAny[list[JobApplications]] = []

class EntryMissingError(Exception):
    ...
    
class ProfileDataBase:

    def __init__(self):
        local_obj_mongoDB = MongoClient("mongodb://localhost:27017/")
        local_obj_db = local_obj_mongoDB["resume_builder"]
        self._obj_profileCollection = local_obj_db["profiles"]
    
    def read(self, param_str_profileName:str):
        local_obj_cursor = self._obj_profileCollection.find({"str_profileName" : param_str_profileName})
        local_list_findings = local_obj_cursor.to_list()
        if len(local_list_findings) != 1:
            raise EntryMissingError("The required profile is not available")

        else:
            local_dict_profile:dict = local_list_findings[0]
            local_dict_profile.pop('str_profileName')
            local_obj_profile = Profile(**local_dict_profile)
            return local_obj_profile 
    
    def create(self, param_str_profileName:str):
        
        local_obj_cursor = self._obj_profileCollection.find({"str_profileName" : param_str_profileName})
        local_list_findings = local_obj_cursor.to_list()
        if len(local_list_findings) != 0:
            raise Exception()
    
    def update(self, param_str_profileName:str, param_obj_profile:Profile):
        ...
    
    def delete(self, param_str_profileName:str):
        ...

    def read_all_profiles(self)->list[str]:
        ...