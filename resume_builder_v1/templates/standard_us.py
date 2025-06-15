from .base import BaseResume, CandidateResume
from textwrap import dedent

class StandardUS(BaseResume):
    def __init__(self):
        pass

    def build(self, param_obj_input: CandidateResume) -> str:
        local_str_latex = self._add_header()
        local_str_latex += "\n\\begin{document}\n"
        local_str_latex += self._add_candidate_details(param_obj_input)
        local_str_latex += self._add_skills(param_obj_input)
        local_str_latex += self._add_experience(param_obj_input)
        local_str_latex += self._add_education(param_obj_input)
        local_str_latex += self._add_achievements(param_obj_input)
        local_str_latex += self._add_projects(param_obj_input)
        
        local_str_latex += "\n\\end{document}\n"
        return local_str_latex

    def _add_header(self):
        return dedent(r"""
        %-------------------------
        % Resume in Latex
        % Author : Gabriel Sison
        % Based off of: https://github.com/sb2nov/resume
        % License : MIT
        %------------------------
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%  Random Stuff %%%%%%%%%%%%%%%%%%%%%%%%%%%%
        \documentclass[letterpaper,10pt]{article}
        \usepackage{latexsym}
        \usepackage[empty]{fullpage}
        \usepackage{titlesec}
        \usepackage{marvosym}
        \usepackage[usenames,dvipsnames]{color}
        \usepackage{verbatim}
        \usepackage{enumitem}
        \usepackage[hidelinks]{hyperref}
        \usepackage{fancyhdr}
        \usepackage[english]{babel}
        \usepackage{tabularx}
        \usepackage{fontawesome5}
        \usepackage{multicol}
        \setlength{\multicolsep}{-3.0pt}
        \setlength{\columnsep}{-1pt}
        \input{glyphtounicode}
        \pagestyle{fancy}
        \fancyhf{} % clear all header and footer fields
        \fancyfoot{}
        \renewcommand{\headrulewidth}{0pt}
        \renewcommand{\footrulewidth}{0pt}
        % Adjust margins
        \addtolength{\oddsidemargin}{-0.6in}
        \addtolength{\evensidemargin}{-0.5in}
        \addtolength{\textwidth}{1.19in}
        \addtolength{\topmargin}{-.7in}
        \addtolength{\textheight}{1.4in}
        \urlstyle{same}
        \raggedbottom
        \raggedright
        \setlength{\tabcolsep}{0in}
        % Sections formatting
        \titleformat{\section}{
          \vspace{-7pt}\scshape\raggedright\large\bfseries
        }{}{0em}{}[\color{black}\titlerule \vspace{0pt}]
        % Ensure that generate pdf is machine readable/ATS parsable
        \pdfgentounicode=1
        \usepackage{xcolor} 
        \usepackage{hyperref}
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%  Commands  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
        \newcommand{\resumeItem}[1]{
          \item\small{{#1 \vspace{-3pt}}}
        }
        \newcommand{\resumeSubheading}[4]{
          \vspace{-3pt}\item
            \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
              \textbf{#1} & \textbf{\small #2} \\
              \textit{\small#3} & \textit{\small #4} \\
            \end{tabular*}\vspace{-7pt}
        }
        \newcommand{\resumeSubheadingContinue}[2]{
          \vspace{-3pt}
            \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
              \textit{\small#1} & \textit{\small #2} \\
            \end{tabular*}\vspace{-7pt}
        }
        \newcommand{\resumeProjectHeading}[2]{
          \vspace{-3pt}\item
            \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
              \textbf{#1} & \textbf{\small #2} \\
            \end{tabular*}\vspace{-7pt}
        }
        \newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{0pt}}
        \renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
        \renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}
        \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
        \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
        \newcommand{\resumeItemListStart}{\begin{itemize}}
        \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{0pt}}
        """)

    def _add_candidate_details(self, param_obj_input: CandidateResume):
        # ...implement similar to simple.py, using the varsha_resume.tex header layout...
        return dedent(rf"""
        
        \begin{{center}}
            {{\Huge\scshape {param_obj_input.str_fullName}}} \\
            \small
            \href{{tel:{param_obj_input.str_contactNumber}}}{{\raisebox{{-0.2\height}}\faPhone\  \underline{{{param_obj_input.str_contactNumber}}}}} ~
            \href{{mailto:{param_obj_input.str_linkedInProfile}}}{{\raisebox{{-0.2\height}}\faEnvelope\  \underline{{{param_obj_input.str_linkedInProfile}}}}} ~
            \href{{{param_obj_input.str_githubProfile}}}{{\raisebox{{-0.2\height}}\faGithub\  \underline{{{param_obj_input.str_githubProfile}}}}}
        \end{{center}}
        """)

    def _add_education(self, param_obj_input: CandidateResume):
        # ...implement using resumeSubheading and resumeSubHeadingListStart/End...
        local_str = "\n\\section{Education}\n"
        local_str += "\\vspace{-0.1cm}\n\\resumeSubHeadingListStart\n"
        for edu in param_obj_input.list_education:
            local_str += f"\\resumeSubheading{{{edu.str_institutionName}}}{{{edu.str_startDate} - {edu.str_endDate or ''}}}{{{edu.str_degree}}}{{{edu.str_location}}} \\newline\n"
            if edu.str_grade:
                local_str += f"{{\\small GPA: {edu.str_grade} }}\n"
            if edu.str_description:
                local_str += f"\\newline\textit{{Relevant Coursework :}} {edu.str_description}\n"
        local_str += "\\resumeSubHeadingListEnd\n"
        return local_str

    def _add_experience(self, param_obj_input: CandidateResume):
        local_str = "\n\\section{Experience}\n\\resumeSubHeadingListStart\n"
        for exp in param_obj_input.list_workExperience:
            local_str += f"\\resumeSubheading{{{exp.str_companyName}}}{{{exp.str_startDate} - {exp.str_endDate or ''}}}{{{exp.str_designation}}}{{{exp.str_location}}}\n"
            local_str += "\\resumeItemListStart\n"
            for resp in exp.list_rolesAndResponsibilities:
                local_str += f"\\resumeItem{{{resp}}}\n"
            local_str += "\\resumeItemListEnd\n"
        local_str += "\\resumeSubHeadingListEnd\n"
        return local_str

    def _add_projects(self, param_obj_input: CandidateResume):
        local_str = "\n\\section{Projects}\n    \\resumeSubHeadingListStart\n"
        for proj in param_obj_input.list_projects:
            local_str += f"\\resumeProjectHeading{{{proj.str_projectTitle}}}{{}}\n"
            local_str += "\\resumeItemListStart\n"
            if proj.list_projectContents:
                for desc in proj.list_projectContents:
                    local_str += f"\\resumeItem{{{desc}}}\n"
            local_str += "\\resumeItemListEnd\n"
        local_str += "\\resumeSubHeadingListEnd\n"
        return local_str

    def _add_skills(self, param_obj_input: CandidateResume):
        local_str = "\n\\section{Technical Skills}\n    \\vspace{-0.3cm}\n    \\begin{itemize}\n    [leftmargin=0.15in, label={}]\\small{\\item{\n        "
        for skill in param_obj_input.list_skills:
            local_str += f"\\textbf{{{skill.str_sectionTitle}}}{{: {', '.join(skill.list_skills)}}} \\textbf{{;}} "
        local_str += "}}\\end{itemize}\n"
        return local_str

    def _add_achievements(self, param_obj_input: CandidateResume):
        local_str = "\n\\section{Honors \\& Awards}\n  \\vspace{-0.3cm}\n    \\resumeItemListStart[itemsep=0pt]\n"
        for ach in param_obj_input.list_achievements:
            local_str += f"\\resumeItem{{{ach}}}\n"
        local_str += "\\resumeItemListEnd\n"
        return local_str
