from string import Template
from textwrap import dedent
import json
import subprocess

class ResumeTemplate(Template):
    delimiter = "$*"

class LatexResumeBuilder:

    def __init__(self):
        ...
    
    def generate(self, param_dict_components:dict, )->None:

        local_str_latex = self._build(param_dict_components)
        with open('resume.tex', 'w') as local_obj_file:
            local_obj_file.write(local_str_latex)
        
        # delete the file
        local_obj_process = subprocess.Popen(["pdflatex","resume.tex"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = local_obj_process.communicate()

        print(stdout.decode())
        if stderr:
            print(f"Error : {stderr.decode()}")

    
    def _build(self, param_dict_resumeComponents:dict)->str:
        
        local_str_resume = self._add_pre_processors()
        local_str_resume += r"\begin{document}"
        local_str_resume += self._add_header(param_dict_resumeComponents['header'])
        local_str_resume += self._add_work_experience(param_dict_resumeComponents['work_experience'])
        local_str_resume += self._add_skills(param_dict_resumeComponents['skills'])
        local_str_resume += self._add_education(param_dict_resumeComponents['education'])
        local_str_resume += self._add_achievements(param_dict_resumeComponents['achievements'])
        local_str_resume += r"\end{document}"
        return local_str_resume


    def _add_pre_processors(self)->str:
        return dedent(r"""
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
        \item\small{
            {#1 \vspace{-3pt}}
        }
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

    def _add_header(self, param_dict_header:dict=None)->str:
        local_str_header = ResumeTemplate(dedent(r"""
        \begin{center}
            % NAME
            {\Huge\scshape $*name} 
            % SUBHEADING
            \\ \small
            % Phone
            \href{tel:$*phone}{\raisebox{-0.2\height}\faPhone\  \underline{$*phone}} ~
            % EMAIL
            \href{mailto:$*email}{\raisebox{-0.2\height}\faEnvelope\  \underline{$*email}} ~ 
            % LINKEDIN
            \href{$*linkedIn}{\raisebox{-0.2\height}\faLinkedin\ \underline{LinkedIn}}  ~
            % GITHUB
            \href{https://$*github}{\raisebox{-0.2\height}\faGithub\ \underline{github}}
        \end{center}
        """))

        local_str_substitutedString = local_str_header.substitute(param_dict_header)

        return local_str_substitutedString

    def _add_education(self, param_list_education:dict=None)->str:
        local_str_education = dedent(r"""
        \section{Education}
        \vspace{-0.1cm}
        """)

        for local_dict_education in param_list_education:
            local_str_template = ResumeTemplate(dedent(r"""
              \resumeSubHeadingListStart
                % MAIN INFORMATION
                \resumeSubheading
                {$*nameOfInstitution}{$*tenure}
                {$*degree}{$*place} \newline
                {\small GPA: $*GPA }
            \resumeSubHeadingListEnd
            \vspace{-0.5cm}                                           
            """))
            local_str_education += local_str_template.substitute(local_dict_education)
            
        
        return local_str_education
    
    def _add_work_experience(self, param_list_experience:list)->str:
        local_str_experTotal= ""
        
        for local_dict_experience in param_list_experience:
            local_str_experString = ""
            for local_str_projectName in local_dict_experience['description']:
                local_str_experString += f"\n\\textit {{\small {local_str_projectName}}}\n\\vspace{{-0.3cm}}"
                local_str_experString += r"\resumeItemListStart"+"\n"
                for local_str_points in local_dict_experience['description'][local_str_projectName]:
                    local_str_experString += r"\resumeItem{" + local_str_points+"}\n"

                local_str_experString += r"\resumeItemListEnd" + "\n"

            local_str_templatedExperienceHeading = ResumeTemplate(dedent(r"""
            
            \resumeSubheading
            {$*company}{$*tenure}
            {$*position}{$*place}
            """))
            local_str_headerString = local_str_templatedExperienceHeading.substitute(local_dict_experience)
            local_str_experString = local_str_headerString+local_str_experString
            local_str_experString = f"\\resumeSubHeadingListStart \n{local_str_experString}\n \\resumeSubHeadingListEnd\n\\vspace{{-0.3cm}}"
            local_str_experTotal += local_str_experString
        return r"\section{Work Experience}"+"\n"+local_str_experTotal

    def _add_skills(self, param_dict_skills:dict)->str:
        
        local_str_skills = dedent(r"""
        \section{Technical Skills}
        \begin{itemize}
        [leftmargin=0.15in, label={}]\small{\item{
        """)

        for local_str_key in param_dict_skills:
            local_str_skills+=f"\n\\textbf{{{local_str_key}:}} {{{",".join(param_dict_skills[local_str_key])}}};"
        
        local_str_skills += "\n}}\\end{itemize}"

        return local_str_skills
    
    def _add_achievements(self, param_list_achievements:list)->str:
        local_str_sectionAchievments = r"""
        \section{Achievements}
        \vspace{-0.1cm}
        \resumeItemListStart
        \resumeItem{Filed \href{https://www.linkedin.com/in/sharath-b-s-196522141/details/patents/}{\underline{8 patents}} on application of AI and ML algorithms for Automotive domain.}
        \vspace{-0.2cm}
        \resumeItem{Published \href{https://www.linkedin.com/in/sharath-b-s-196522141/details/publications/}{\underline{papers}} during university coursework on robotics and automation.}
        \vspace{-0.2cm}
        """
        for local_str_achievment in param_list_achievements:
            local_str_sectionAchievments += f"\\resumeItem{{{local_str_achievment}}}\n\\vspace{{-0.2cm}}"
        return local_str_sectionAchievments+"\n\\resumeItemListEnd"

