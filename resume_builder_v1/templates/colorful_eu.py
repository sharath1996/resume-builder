from .base import BaseResume, CandidateResume
from textwrap import dedent

class ColorfulEU(BaseResume):

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
        local_str_latex += self._add_achievements(param_obj_input)
        local_str_latex += self._add_projects(param_obj_input)

        local_str_latex += "\n\\end{document}\n"

        # local_str_latex = local_str_latex.replace("#", "\#")

        return local_str_latex

    def _add_header(self) -> str:
        """
        Add the header for the resume.
        """
        return dedent(r"""
        \documentclass[10pt, letterpaper]{article}

        % Packages:
        \usepackage[
            ignoreheadfoot, % set margins without considering header and footer
            top=2 cm, % seperation between body and page edge from the top
            bottom=2 cm, % seperation between body and page edge from the bottom
            left=2 cm, % seperation between body and page edge from the left
            right=2 cm, % seperation between body and page edge from the right
            footskip=1.0 cm, % seperation between body and footer
            % showframe % for debugging 
        ]{geometry} % for adjusting page geometry
        \usepackage[explicit]{titlesec} % for customizing section titles
        \usepackage{tabularx} % for making tables with fixed width columns
        \usepackage{array} % tabularx requires this
        \usepackage[dvipsnames]{xcolor} % for coloring text
        \definecolor{primaryColor}{RGB}{0, 79, 144} % define primary color
        \usepackage{enumitem} % for customizing lists
        \usepackage{fontawesome5} % for using icons
        \usepackage{amsmath} % for math
        \usepackage[
            pdftitle={John Doe's CV},
            pdfauthor={John Doe},
            pdfcreator={LaTeX with RenderCV},
            colorlinks=true,
            urlcolor=primaryColor
        ]{hyperref} % for links, metadata and bookmarks
        \usepackage[pscoord]{eso-pic} % for floating text on the page
        \usepackage{calc} % for calculating lengths
        \usepackage{bookmark} % for bookmarks
        \usepackage{lastpage} % for getting the total number of pages
        \usepackage{changepage} % for one column entries (adjustwidth environment)
        \usepackage{paracol} % for two and three column entries
        \usepackage{ifthen} % for conditional statements
        \usepackage{needspace} % for avoiding page brake right after the section title
        \usepackage{iftex} % check if engine is pdflatex, xetex or luatex

        % Ensure that generate pdf is machine readable/ATS parsable:
        \ifPDFTeX
            \input{glyphtounicode}
            \pdfgentounicode=1
            \usepackage[T1]{fontenc}
            \usepackage[utf8]{inputenc}
            \usepackage{lmodern}
        \fi

        \usepackage[default, type1]{sourcesanspro} 

        % Some settings:
        \AtBeginEnvironment{adjustwidth}{\partopsep0pt} % remove space before adjustwidth environment
        \pagestyle{empty} % no header or footer
        \setcounter{secnumdepth}{0} % no section numbering
        \setlength{\parindent}{0pt} % no indentation
        \setlength{\topskip}{0pt} % no top skip
        \setlength{\columnsep}{0.15cm} % set column seperation
        \makeatletter
        \let\ps@customFooterStyle\ps@plain % Copy the plain style to customFooterStyle
        \patchcmd{\ps@customFooterStyle}{\thepage}{
            \color{gray}\textit{\small John Doe - Page \thepage{} of \pageref*{LastPage}}
        }{}{} % replace number by desired string
        \makeatother
        \pagestyle{customFooterStyle}

        \titleformat{\section}{
            % avoid page braking right after the section title
            \needspace{4\baselineskip}
            % make the font size of the section title large and color it with the primary color
            \Large\color{primaryColor}
        }{
        }{
        }{
            % print bold title, give 0.15 cm space and draw a line of 0.8 pt thickness
            % from the end of the title to the end of the body
            \textbf{#1}\hspace{0.15cm}\titlerule[0.8pt]\hspace{-0.1cm}
        }[] % section title formatting

        \titlespacing{\section}{
            % left space:
            -1pt
        }{
            % top space:
            0.3 cm
        }{
            % bottom space:
            0.2 cm
        } % section title spacing

        % \renewcommand\labelitemi{$\vcenter{\hbox{\small$\bullet$}}$} % custom bullet points
        \newenvironment{highlights}{
            \begin{itemize}[
                topsep=0.10 cm,
                parsep=0.10 cm,
                partopsep=0pt,
                itemsep=0pt,
                leftmargin=0.4 cm + 10pt
            ]
        }{
            \end{itemize}
        } % new environment for highlights

        \newenvironment{highlightsforbulletentries}{
            \begin{itemize}[
                topsep=0.10 cm,
                parsep=0.10 cm,
                partopsep=0pt,
                itemsep=0pt,
                leftmargin=10pt
            ]
        }{
            \end{itemize}
        } % new environment for highlights for bullet entries


        \newenvironment{onecolentry}{
            \begin{adjustwidth}{
                0.2 cm + 0.00001 cm
            }{
                0.2 cm + 0.00001 cm
            }
        }{
            \end{adjustwidth}
        } % new environment for one column entries

        \newenvironment{twocolentry}[2][]{
            \onecolentry
            \def\secondColumn{#2}
            \setcolumnwidth{\fill, 4.5 cm}
            \begin{paracol}{2}
        }{
            \switchcolumn \raggedleft \secondColumn
            \end{paracol}
            \endonecolentry
        } % new environment for two column entries

        \newenvironment{threecolentry}[3][]{
            \onecolentry
            \def\thirdColumn{#3}
            \setcolumnwidth{1 cm, \fill, 4.5 cm}
            \begin{paracol}{3}
            {\raggedright #2} \switchcolumn
        }{
            \switchcolumn \raggedleft \thirdColumn
            \end{paracol}
            \endonecolentry
        } % new environment for three column entries

        \newenvironment{header}{
            \setlength{\topsep}{0pt}\par\kern\topsep\centering\color{primaryColor}\linespread{1.5}
        }{
            \par\kern\topsep
        } % new environment for the header

        \newcommand{\placelastupdatedtext}{% \placetextbox{<horizontal pos>}{<vertical pos>}{<stuff>}
        \AddToShipoutPictureFG*{% Add <stuff> to current page foreground
            \put(
                \LenToUnit{\paperwidth-2 cm-0.2 cm+0.05cm},
                \LenToUnit{\paperheight-1.0 cm}
            ){\vtop{{\null}\makebox[0pt][c]{
                \small\color{gray}\textit{Last updated in September 2024}\hspace{\widthof{Last updated in September 2024}}
            }}}%
        }%
        }%

        % save the original href command in a new command:
        \let\hrefWithoutArrow\href

        % new command for external links:
        \renewcommand{\href}[2]{\hrefWithoutArrow{#1}{\ifthenelse{\equal{#2}{}}{ }{#2 }\raisebox{.15ex}{\footnotesize \faExternalLink*}}}
                            """)
    
    def _add_candidate_details(self, param_obj_input: CandidateResume) -> str:
        """
        Add the candidate's details to the resume.
        """
        # Render the header block as in template/resume.tex, but with colorful styling if needed
        return dedent(rf'''
        \begin{{header}}
        \fontsize{{30 pt}}{{30 pt}}
        \textbf{{{param_obj_input.str_fullName}}}

        \vspace{{0.3 cm}}

        \normalsize
        \mbox{{{{\footnotesize\faMapMarker*}}\hspace*{{0.13cm}}{param_obj_input.str_currentResidence}}}%
        \kern 0.25 cm%
        \AND%
        \kern 0.25 cm%
        \mbox{{\hrefWithoutArrow{{mailto:{param_obj_input.str_linkedInProfile or param_obj_input.str_customProfile or ''}}}{{{{\footnotesize\faEnvelope[regular]}}\hspace*{{0.13cm}}{param_obj_input.str_linkedInProfile or param_obj_input.str_customProfile or ''}}}}}%
        \kern 0.25 cm%
        \AND%
        \kern 0.25 cm%
        \mbox{{\hrefWithoutArrow{{tel:{param_obj_input.str_contactNumber}}}{{{{\footnotesize\faPhone*}}\hspace*{{0.13cm}}{param_obj_input.str_contactNumber}}}}}%
        \kern 0.25 cm%
        \AND%
        \kern 0.25 cm%
        \mbox{{\hrefWithoutArrow{{{param_obj_input.str_customProfile or ''}}}{{{{\footnotesize\faLink}}\hspace*{{0.13cm}}{param_obj_input.str_customProfile or ''}}}}}%
        \kern 0.25 cm%
        \AND%
        \kern 0.25 cm%
        \mbox{{\hrefWithoutArrow{{{param_obj_input.str_linkedInProfile or ''}}}{{{{\footnotesize\faLinkedinIn}}\hspace*{{0.13cm}}{param_obj_input.str_linkedInProfile or ''}}}}}%
        \kern 0.25 cm%
        \AND%
        \kern 0.25 cm%
        \mbox{{\hrefWithoutArrow{{{param_obj_input.str_githubProfile or ''}}}{{{{\footnotesize\faGithub}}\hspace*{{0.13cm}}{param_obj_input.str_githubProfile or ''}}}}}%
    \end{{header}}
    \vspace{{0.3 cm - 0.3 cm}}
''')
    
    def _add_summary(self, param_obj_input: CandidateResume) -> str:
        """
        Add the summary section to the resume.
        """
        return dedent(f"""
        \\section{{Summary}}
        \\begin{{onecolentry}}
            {param_obj_input.str_aboutCandidate}
        \\end{{onecolentry}}
        """)
    
    def _add_skills(self, param_obj_input: CandidateResume) -> str:
        """
        Add the skills section to the resume.
        """
        local_str = "\n\\section{Technologies}\n"
        for skill in param_obj_input.list_skills:
            local_str += f"\\begin{{onecolentry}}\n  \\textbf{{{skill.str_sectionTitle}}}: {', '.join(skill.list_skills)}\n\\end{{onecolentry}}\n"
        return local_str

    def _add_work_experience(self, param_obj_input: CandidateResume) -> str:
        """
        Add the work experience section to the resume.
        """
        local_str = "\n\\section{Experience}\n"
        for exp in param_obj_input.list_workExperience:
            local_str += f"\\begin{{twocolentry}}{{{exp.str_location or ''}\\n\\\n{exp.str_startDate} -- {exp.str_endDate or 'Present'}}}\n  \\textbf{{{exp.str_companyName}}}, {exp.str_designation}\n  \\begin{{highlights}}\n"
            for resp in exp.list_rolesAndResponsibilities:
                local_str += f"    \\item {resp}\n"
            local_str += "  \\end{highlights}\n\\end{twocolentry}\n\\vspace{0.2 cm}\n"
        return local_str

    def _add_education(self, param_obj_input: CandidateResume) -> str:
        """
        Add the education section to the resume.
        """
        local_str = "\n\\section{Education}\n"
        for edu in param_obj_input.list_education:
            local_str += f"\\begin{{threecolentry}}{{\\textbf{{{edu.str_degree}}}}}{{{edu.str_startDate} -- {edu.str_endDate or ''}}}\n  \\textbf{{{edu.str_institutionName}}}, {edu.str_degree}\n  \\begin{{highlights}}\n"
            if edu.str_grade:
                local_str += f"    \\item GPA: {edu.str_grade}\n"
            if edu.str_description:
                local_str += f"    \\item \\textbf{{Coursework:}} {edu.str_description}\n"
            local_str += "  \\end{highlights}\n\\end{threecolentry}\n"
        return local_str

    def _add_achievements(self, param_obj_input: CandidateResume) -> str:
        """
        Add the achievements section to the resume.
        """
        local_str = "\n\\section{Certifications \\& Awards}\n\\begin{onecolentry}\n  \\begin{highlightsforbulletentries}\n"
        for ach in param_obj_input.list_achievements:
            local_str += f"    \\item {ach}\n"
        local_str += "  \\end{highlightsforbulletentries}\n\\end{onecolentry}\n"
        return local_str

    def _add_projects(self, param_obj_input: CandidateResume) -> str:
        """
        Add the projects section to the resume.
        """
        local_str = "\n\\section{Projects}\n"
        for proj in param_obj_input.list_projects:
            local_str += f"\\begin{{twocolentry}}{{{proj.str_projectTitle}}}\n  \\textbf{{{proj.str_projectTitle}}}\n  \\begin{{highlights}}\n"
            if proj.list_projectContents:
                for desc in proj.list_projectContents:
                    local_str += f"    \\item {desc}\n"
            local_str += "  \\end{highlights}\n\\end{twocolentry}\n\\vspace{0.2 cm}\n"
        return local_str


