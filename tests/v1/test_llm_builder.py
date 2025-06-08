from resume_builder_v1.builder.builder import ResumeBuilderInput, ResumeBuilder
import json
from  textwrap import dedent

def test_llm_builder_with_real_profile():
    """
    Integration test for LLMBuilder with a real profile from the database (profile name: 'sharath').
    """

    builder = ResumeBuilder()
    input_obj = ResumeBuilderInput(
        str_jobDescription=dedent("""
        Minimum qualifications:

        Bachelor's degree or equivalent practical experience.
        5 years of experience with software development in one or more programming languages, and with data structures/algorithms.
        3 years of experience testing, maintaining, or launching software products, and 1 year of experience with software design and architecture.
        3 years of experience with state of the art GenAI techniques (e.g., LLMs, Multi-Modal, Large Vision Models) or with GenAI-related concepts (language modeling, computer vision).
        3 years of experience with ML infrastructure (e.g., model deployment, model evaluation, optimization, data processing, debugging).

        Preferred qualifications:

        Master's degree or PhD in Computer Science or related technical field.
        1 year of experience in a technical leadership role.
        Experience developing accessible technologies.
        """),
        str_additionalInstructionsAndNotes="Highlight leadership and cloud experience.",
        str_profileName="Sharath"
    )
    candidate_resume = builder.build(input_obj)
    with open("tests/v1/test_llm_builder_output.json", "w") as f:
        json.dump(candidate_resume.model_dump(), f, indent=4)