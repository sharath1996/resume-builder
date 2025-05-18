
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
    str_highlights:str | None = Field(None, description="Top highlights of this project")

class Roles(BaseModel):
    dateTime_startDate:str|None = Field(None, description="Start date of the role")
    dateTime_endDate:str|str|None = Field(None, description="End date, it can include `Present`")
    str_title:str|None = Field(None, description="Title of the role or designation")
    str_place:str|None = Field(None, description="Place")
    str_description:str|None = Field(None, description="Description of roles and responsibilities of this Role")
    list_achievements:list[str|None]  = Field([], description="List of achivements in this role")
    list_skills : list[str|None] = Field([], description="List of skills")

class WorkExperience(BaseModel):
    str_companyName:str|None = Field(None, description="Name of the company")
    list_roles:list[Roles] = Field(default_factory=list[Roles], description="List of roles")

class Education(BaseModel):
    str_institutionName:str|None = Field(None, description="Name of the Institution")
    str_degree:str|None = Field(None, description="Name of the degree")
    datetime_startDate:str|None = Field(None, description="Start date of the education")
    datetime_endDate:str|None = Field(None, description="End date of the degree")
    str_grade:str|None = Field(None, description="Grade Obtained")
    str_place:str|None = Field(None, description="Name of the place, where you obtained the degree")
    str_description:str|None = Field(None, description="Description of your courses and top achivements!")

class Certification(BaseModel):
    str_name:str|None = Field(None, description="Certification Name")
    str_issuingAuthority:str|None = Field(None, description="Name of the issuing Authority")
    datetime_issueDate:str|None = Field(None, description="Date of issuing")

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
    obj_profileInfo : SerializeAsAny[ProfileInformation] = ProfileInformation()
    list_workExperience: SerializeAsAny[list[WorkExperience | None] ] = []
    list_education:SerializeAsAny[list[Education | None]] = []
    list_certifcations:SerializeAsAny[list[Certification | None]] = []
    list_papers:SerializeAsAny[list[Papers | None]] = []
    list_patents:SerializeAsAny[list[Patents | None]] = []
    list_talks:SerializeAsAny[list[Talks | None]] = []
    list_jobApps:SerializeAsAny[list[JobApplications | None]] = []

class EntryMissingError(Exception):
    """Custom exception raised when a requested profile entry is missing in the database."""
    def __init__(self, param_str_message="The required profile is not available"):
        self._str_message = param_str_message
        super().__init__(self._str_message)
    
class ProfileDataBase:

    def __init__(self):
        local_obj_mongoDB = MongoClient("mongodb://localhost:27017/")
        local_obj_db = local_obj_mongoDB["resume_builder"]
        self._obj_profileCollection = local_obj_db["profiles"]

    def read(self, param_str_profileName: str) -> Profile:
        local_obj_cursor = self._obj_profileCollection.find_one({"str_profileName": param_str_profileName})
        if not local_obj_cursor:
            raise EntryMissingError("The required profile is not available")

        local_obj_cursor.pop('_id', None)  # Removing MongoDB's default ID field
        local_obj_cursor.pop('str_profileName', None)
        return Profile(**local_obj_cursor)

    def create(self, param_str_profileName: str, param_obj_profile: Profile):
        if self._obj_profileCollection.find_one({"str_profileName": param_str_profileName}):
            raise Exception("Profile already exists")

        local_dict_profileData = param_obj_profile.model_dump()
        local_dict_profileData["str_profileName"] = param_str_profileName
        self._obj_profileCollection.insert_one(local_dict_profileData)

    def update(self, param_str_profileName: str, param_obj_profile: Profile):
        local_obj_result = self._obj_profileCollection.update_one(
            {"str_profileName": param_str_profileName},
            {"$set": param_obj_profile.model_dump()}
        )
        if local_obj_result.matched_count == 0:
            raise EntryMissingError("Profile not found")

    def delete(self, param_str_profileName: str):
        local_obj_result = self._obj_profileCollection.delete_one({"str_profileName": param_str_profileName})
        if local_obj_result.deleted_count == 0:
            raise EntryMissingError("Profile not found")

    def read_all_profiles(self) -> list[str]:
        local_list_profiles = self._obj_profileCollection.find({}, {"str_profileName": 1})
        return [local_dict_profile["str_profileName"] for local_dict_profile in local_list_profiles]