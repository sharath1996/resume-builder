from pydantic import BaseModel, Field

class Skill(BaseModel):
    """
    Base class for skills.
    This class is used to define the structure of skills data.
    """
    str_sectionTitle:str = Field(None, description="Title of the skills section")
    list_skills: list[str] = Field([], description="List of skills")

class Experience(BaseModel):
    """
    Base class for work experience.
    This class is used to define the structure of work experience data.
    """
    str_companyName:str = Field(..., description="Name of the company")
    str_designation:str = Field(..., description="Designation or title of the role")
    str_startDate: str = Field(..., description="Start date of the role in Mmmm, YYYY format, example: 'January, 2020' or 'March, 2021")
    str_endDate: str | None = Field(None, description="End date of the role  Mmmm, YYYY formatt, example: 'January, 2020' or 'March, 2021")
    str_location: str | None = Field(None, description="Location of the company")
    list_rolesAndResponsibilities: list[str] = Field(..., description="List of roles and responsibilities in this role")

class Education(BaseModel):
    """
    Base class for education.
    This class is used to define the structure of education data.
    """
    str_institutionName: str = Field(..., description="Name of the institution")
    str_degree: str = Field(..., description="Name of the degree")
    str_startDate: str = Field(..., description="Start date of the education n Mmmm, YYYY format, example: 'January, 2020' or 'March, 2021")
    str_endDate: str | None = Field(None, description="End date of the degree n Mmmm, YYYY format, example: 'January, 2020' or 'March, 2021")
    str_grade: str | None = Field(None, description="Grade obtained")
    str_location: str | None = Field(None, description="Location of the institution")
    str_description: str | None = Field(None, description="Description of courses and top achievements")

class Project(BaseModel):
    """
    Base class for projects.
    This class is used to define the structure of project data.
    """
    str_projectTitle: str | None = Field(None, description="Title of the project")
    list_projectContents: list[str] | None = Field(None, description="Two to three lines describing the project and its relevance to the job application")

class CandidateDetails(BaseModel):

    str_fullName: str  = Field(..., description="Full Name of the candidate")
    str_currentResidence: str  = Field(..., description="Current residence of the candidate")
    str_contactNumber: str = Field(..., description="Contact number including the country code")
    str_email: str = Field(..., description="Email address of the candidate")
    str_linkedInProfile: str | None = Field(None, description="LinkedIn Profile URL")
    str_githubProfile: str | None = Field(None, description="Github profile link")
    str_customProfile: str | None = Field(None, description="Any other custom Profile Link")
    str_aboutCandidate: str = Field(..., description="About the candidate")

class Skills(BaseModel):
    list_skills: list[Skill] = Field(..., description="List of skills")

class WorkExperiences(BaseModel):
    list_workExperience: list[Experience] = Field(..., description="List of work experience")

class Educations(BaseModel):
    list_education: list[Education] = Field(..., description="List of education details")

class Projects(BaseModel):
    list_projects: list[Project] = Field(..., description="List of projects that are relevant to the job application")

class Achivements(BaseModel):
    list_achievements: list[str] = Field([], description="List of achievements including certifications, papers, patents, talks etc.")
class CandidateResume(CandidateDetails, Skills, WorkExperiences, Educations, Projects, Achivements):
    """
    Base class for resume input data.
    This class is used to define the structure of the resume input data.
    """
    ...
    
    
    
    
    