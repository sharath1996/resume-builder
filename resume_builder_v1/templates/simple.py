from .base import BaseResume, CandidateResume
from textwrap import dedent

class SimpleResume:

    def __init__(self):
        ...
    
    def build(self, param_obj_input: CandidateResume) -> str:
        """
        Build the resume in LaTeX format using the simple template.
        """
        local_str_latex = self._add_header()
        local_str_latex += "\n\\begin{document}\n"
        local_str_latex += self._add_candidate_details(param_obj_input)
        local_str_latex += self._add_summary(param_obj_input)
        local_str_latex += self._add_skills(param_obj_input)
        local_str_latex += self._add_work_experience(param_obj_input)
        local_str_latex += self._add_education(param_obj_input)
        local_str_latex += self._add_projects(param_obj_input)
        local_str_latex += self._add_achievements(param_obj_input)
        local_str_latex += "\n\\end{document}\n"

        # local_str_latex = local_str_latex.replace("#", "\#")

        return local_str_latex

    def _add_header(self):
        local_str_header = dedent(r"""
        %%%%
        % MTecknology's Resume
        %%%%
        % Author: Michael Lustfield
        % License: CC-BY-4
        % - https://creativecommons.org/licenses/by/4.0/legalcode.txt
        %%%%

        \documentclass[letterpaper,10pt]{article}
        %%%%%%%%%%%%%%%%%%%%%%%
        %% BEGIN_FILE: mteck.sty
        %% NOTE: Everything between here and END_FILE can
        %% be relocated to "mteck.sty" and then included with:
        %\usepackage{mteck}

        % Dependencies
        % NOTE: Some packages (lastpage, hyperref) require second build!
        \usepackage[empty]{fullpage}
        \usepackage{titlesec}
        \usepackage{enumitem}
        \usepackage[hidelinks]{hyperref}
        \usepackage{fancyhdr}
        \usepackage{fontawesome5}
        \usepackage{multicol}
        \usepackage{bookmark}
        \usepackage{lastpage}

        % Sans-Serif
        %\usepackage[sfdefault]{FiraSans}
        %\usepackage[sfdefault]{roboto}
        %\usepackage[sfdefault]{noto-sans}
        %\usepackage[default]{sourcesanspro}

        % Serif
        \usepackage{CormorantGaramond}
        \usepackage{charter}

        % Colors
        % Use with \color{Name}
        % Can wrap entire heading with {\color{accent} [...] }
        \usepackage{xcolor}
        \definecolor{accentTitle}{HTML}{0e6e55}
        \definecolor{accentText}{HTML}{0e6e55}
        \definecolor{accentLine}{HTML}{a16f0b}

        % Misc. Options
        \pagestyle{fancy}
        \fancyhf{}
        \fancyfoot{}
        \renewcommand{\headrulewidth}{0pt}
        \renewcommand{\footrulewidth}{0pt}
        \urlstyle{same}

        % Adjust Margins
        \addtolength{\oddsidemargin}{-0.7in}
        \addtolength{\evensidemargin}{-0.5in}
        \addtolength{\textwidth}{1.19in}
        \addtolength{\topmargin}{-0.7in}
        \addtolength{\textheight}{1.4in}

        \setlength{\multicolsep}{-3.0pt}
        \setlength{\columnsep}{-1pt}
        \setlength{\tabcolsep}{0pt}
        \setlength{\footskip}{3.7pt}
        \raggedbottom
        \raggedright

        % ATS Readability
        \input{glyphtounicode}
        \pdfgentounicode=1

        %-----------------%
        % Custom Commands %
        %-----------------%

        % Centered title along with subtitle between HR
        % Usage: \documentTitle{Name}{Details}
        \newcommand{\documentTitle}[2]{
        \begin{center}
            {\Huge\color{accentTitle} #1}
            \vspace{10pt}
            {\color{accentLine} \hrule}
            \vspace{2pt}
            %{\footnotesize\color{accentTitle} #2}
            \footnotesize{#2}
            \vspace{2pt}
            {\color{accentLine} \hrule}
        \end{center}
        }

        % Create a footer with correct padding
        % Usage: \documentFooter{\thepage of X}
        \newcommand{\documentFooter}[1]{
        \setlength{\footskip}{10.25pt}
        \fancyfoot[C]{\footnotesize #1}
        }

        % Simple wrapper to set up page numbering
        % Usage: \numberedPages
        % WARNING: Must run pdflatex twice!
        \newcommand{\numberedPages}{
        \documentFooter{\thepage/\pageref{LastPage}}
        }

        % Section heading with horizontal rule
        % Usage: \section{Title}
        \titleformat{\section}{
        \vspace{-5pt}
        \color{accentText}
        \raggedright\large\bfseries
        }{}{0em}{}[\color{accentLine}\titlerule]

        % Section heading with separator and content on same line
        % Usage: \tinysection{Title}
        \newcommand{\tinysection}[1]{
        \phantomsection
        \addcontentsline{toc}{section}{#1}
        {\large{\bfseries\color{accentText}#1} {\color{accentLine} |}}
        }

        % Indented line with arguments left/right aligned in document
        % Usage: \heading{Left}{Right}
        \newcommand{\heading}[2]{
        \hspace{10pt}#1\hfill#2\\
        }

        % Adds \textbf to \heading
        \newcommand{\headingBf}[2]{
        \heading{\textbf{#1}}{\textbf{#2}}
        }

        % Adds \textit to \heading
        \newcommand{\headingIt}[2]{
        \heading{\textit{#1}}{\textit{#2}}
        }

        % Template for itemized lists
        % Usage: \begin{resume_list} [items] \end{resume_list}
        \newenvironment{resume_list}{
        \vspace{-7pt}
        \begin{itemize}[itemsep=-2px, parsep=1pt, leftmargin=30pt]
        }{
        \end{itemize}
        %\vspace{-2pt}
        }

        % Formats an item to use as an itemized title
        % Usage: \itemTitle{Title}
        \newcommand{\itemTitle}[1]{
        \item[] \underline{#1}\vspace{4pt}
        }

        % Bullets used in itemized lists
        \renewcommand\labelitemi{--}

        %% END_FILE: mteck.sty
        %%%%%%%%%%%%%%%%%%%%%%
        """)

        return local_str_header
    
    def _add_candidate_details(self, param_obj_input: CandidateResume):
        # Compose the LaTeX for the candidate's name and contact info using \documentTitle
        local_list_details = []
        if param_obj_input.str_contactNumber:
            local_list_details.append(f"\\href{{tel:{param_obj_input.str_contactNumber}}}{{\\raisebox{{-0.05\\height}} \\faPhone\\ {param_obj_input.str_contactNumber}}}")
        if param_obj_input.str_linkedInProfile:
            local_list_details.append(f"\\href{{{param_obj_input.str_linkedInProfile}}}{{\\raisebox{{-0.15\\height}} \\faLinkedin\\ {param_obj_input.str_linkedInProfile}}}")
        if param_obj_input.str_githubProfile:
            local_list_details.append(f"\\href{{{param_obj_input.str_githubProfile}}}{{\\raisebox{{-0.15\\height}} \\faGithub\\ {param_obj_input.str_githubProfile}}}")
        if param_obj_input.str_customProfile:
            local_list_details.append(f"\\href{{{param_obj_input.str_customProfile}}}{{\\raisebox{{-0.15\\height}} \\faGlobe\\ {param_obj_input.str_customProfile}}}")
        local_str_details = " ~ | ~ ".join(local_list_details)
        
        return f"\\documentTitle{{{param_obj_input.str_fullName}}}{{{local_str_details}}}\n\n"

    def _add_summary(self, param_obj_input: CandidateResume):
        # Add a summary/about section
        
        if param_obj_input.str_aboutCandidate:
            return f"\\tinysection{{Summary}}\n{param_obj_input.str_aboutCandidate}\n\n"
        
        return ""

    def _add_skills(self, param_obj_input: CandidateResume):
        # Add a Skills section in two columns
        if not param_obj_input.list_skills:
            return ""
        latex = "\\section{Skills}\n\n\\begin{multicols}{2}\n  \\begin{itemize}[itemsep=-2px, parsep=1pt, leftmargin=75pt]\n"
        for local_obj_skill in param_obj_input.list_skills:
            if local_obj_skill.str_sectionTitle and local_obj_skill.list_skills:
                local_str_skills = ", ".join(local_obj_skill.list_skills)
                latex += f"\n\t\\item[\\textbf{{{local_obj_skill.str_sectionTitle}}}] {local_str_skills}"
        latex += "\n\\end{itemize}\n\\end{multicols}\n\n"
        return latex

    def _add_work_experience(self, param_obj_input: CandidateResume):
        # Add Experience section
        if not param_obj_input.list_workExperience:
            return ""
        latex = "\\section{Experience}\n\n"
        for exp in param_obj_input.list_workExperience:
            latex += f"\\headingBf{{{exp.str_companyName}}}{{{exp.str_startDate} -- {exp.str_endDate or 'Present'}}}\n"
            latex += f"\\headingIt{{{exp.str_designation}}}{{{exp.str_location or ''}}}\n"
            latex += "\\begin{resume_list}\n"
            for resp in exp.list_rolesAndResponsibilities:
                latex += f"  \\item {resp}\n"
            latex += "\\end{resume_list}\n\n"
        return latex

    def _add_education(self, param_obj_input: CandidateResume):
        # Add Education section
        if not param_obj_input.list_education:
            return ""
        latex = "\\section{Education}\n\n"
        for edu in param_obj_input.list_education:
            latex += f"\\headingBf{{{edu.str_institutionName}}}{{}}\n"
            latex += f"\\headingIt{{{edu.str_degree}}}{{{edu.str_location or ''}}}\n"
            if edu.str_description:
                latex += f"{edu.str_description}\n"
        latex += "\n"
        return latex

    def _add_projects(self, param_obj_input: CandidateResume):
        # Add Projects section if present
        if not hasattr(param_obj_input, 'list_projects') or not getattr(param_obj_input, 'list_projects', None):
            return ""
        local_str_latex = "\\section{Projects}\n\n"
        for local_obj_project in param_obj_input.list_projects:
            if local_obj_project.str_projectTitle:
                local_str_latex += f"\\headingBf{{{local_obj_project.str_projectTitle}}}{{}}\n"
            if local_obj_project.list_projectContents:
                local_str_latex += "\\begin{resume_list}\n"
                for item in local_obj_project.list_projectContents:
                    local_str_latex += f"  \\item {item}\n"
                local_str_latex += "\\end{resume_list}\n"
        local_str_latex += "\n"
        return local_str_latex

    def _add_achievements(self, param_obj_input: CandidateResume):
        # Add Achievements/Certifications section if present
        if not hasattr(param_obj_input, 'list_achievements') or not getattr(param_obj_input, 'list_achievements', None):
            return ""
        local_str_achievements = "\\section{Achievements}\n\n\\begin{resume_list}\n"
        for local_str_achievement in param_obj_input.list_achievements:
            local_str_achievements += f"  \\item {local_str_achievement}\n"
        local_str_achievements += "\\end{resume_list}\n\n"
        return local_str_achievements