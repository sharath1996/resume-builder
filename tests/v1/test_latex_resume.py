from resume_builder_v1.templates import ResumeTemplates
from resume_builder_v1.builder.builder import CandidateResume, Skill, Experience, Education, Project

def get_sample_candidate_resume() -> CandidateResume:
    """
    Returns a sample CandidateResume object populated with example data.
    """
    return CandidateResume(
        str_fullName="Jane Doe",
        str_currentResidence="San Francisco, CA",
        str_contactNumber="+1-555-123-4567",
        str_linkedInProfile="https://www.linkedin.com/in/janedoe",
        str_githubProfile="https://github.com/janedoe",
        str_customProfile="https://janedoe.dev",
        str_aboutCandidate=(
            "Senior Software Engineer with 7+ years of experience in full-stack development, "
            "leading teams, and delivering scalable analytics platforms. Passionate about building "
            "robust, user-centric applications and mentoring engineers."
        ),
        list_skills=[
            Skill(
                str_sectionTitle="Programming Languages",
                list_skills=["Python", "Java", "C#", "TypeScript", "SQL"]
            ),
            Skill(
                str_sectionTitle="Frameworks & Tools",
                list_skills=["React", "Redux", "Spring Boot", ".NET", "Hibernate", "Jenkins", "Git"]
            ),
            Skill(
                str_sectionTitle="Cloud & DevOps",
                list_skills=["AWS", "Cloud Foundry", "Docker", "CI/CD"]
            ),
        ],
        list_workExperience=[
            Experience(
                str_companyName="FinTech Solutions",
                str_designation="Senior Software Engineer",
                str_startDate="2020-01",
                str_endDate="Present",
                str_location="San Francisco, CA",
                list_rolesAndResponsibilities=[
                    "Led the design and implementation of scalable analytics modules using React and Spring Boot.",
                    "Mentored a team of 5 junior engineers, improving code quality and delivery speed.",
                    "Collaborated with Product Managers and UX Designers to deliver customer-centric features.",
                    "Implemented CI/CD pipelines with Jenkins and Docker, reducing deployment time by 30%."
                ]
            ),
            Experience(
                str_companyName="Data Insights Inc.",
                str_designation="Software Engineer",
                str_startDate="2017-06",
                str_endDate="2019-12",
                str_location="Remote",
                list_rolesAndResponsibilities=[
                    "Developed RESTful APIs and data models for analytics products.",
                    "Worked with SQL Server and Hibernate for high-performance data access.",
                    "Contributed to cloud migration using AWS and Cloud Foundry."
                ]
            ),
        ],
        list_education=[
            Education(
                str_institutionName="Stanford University",
                str_degree="M.S. Computer Science",
                str_startDate="2015-09",
                str_endDate="2017-06",
                str_grade="3.9/4.0",
                str_location="Stanford, CA",
                str_description="Specialized in distributed systems and data analytics."
            ),
            Education(
                str_institutionName="University of California, Berkeley",
                str_degree="B.S. Computer Science",
                str_startDate="2011-09",
                str_endDate="2015-06",
                str_grade="3.8/4.0",
                str_location="Berkeley, CA",
                str_description="Graduated with Honors."
            ),
        ],
        list_projects=[
            Project(
                str_projectTitle="Real-Time Fraud Detection Platform",
                list_projectContents=[
                    "Designed and implemented a real-time fraud detection system using Spring Boot, Kafka, and React."
                    "Reduced fraud incidents by 40% and improved detection latency."
                ]
            ),
            Project(
                str_projectTitle="Cloud-Native Analytics Dashboard",
                list_projectContents=[
                    "Built a cloud-native dashboard for financial analytics using AWS, React, and REST APIs. "
                    "Enabled customers to visualize and export large datasets efficiently."
                ]
            ),
        ],
        list_achievements=[
            "AWS Certified Solutions Architect -- Associate",
            "Speaker at FinTech DevCon 2023: 'Scaling Analytics in the Cloud'",
            "Published paper: 'Optimizing Data Pipelines for Real-Time Analytics' (IEEE Big Data 2022)"
        ]
    )

def test_simple_template():
    
    local_obj_candidateResume = get_sample_candidate_resume()
    local_obj_resumeBuilder = ResumeTemplates().get_template("simple")
    local_str_resume = local_obj_resumeBuilder.build(local_obj_candidateResume)
    with open('resume.tex', "w") as local_file_resumeFile:
        local_file_resumeFile.write(local_str_resume)

