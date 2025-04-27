# Agents for Software Engineers

A comprehensive initiative aimed at developing advanced AI-driven agents to significantly enhance the productivity of software engineers across all phases of the software development lifecycle.

## Overview

The project addresses critical inefficiencies faced by software engineers, particularly in ancillary tasks such as requirement analysis, software planning, detailed design documentation, code annotation, and creation of test cases. By leveraging AI-driven automation, the project streamlines these repetitive yet essential tasks, empowering engineers to focus on high-value coding activities.  

- **Project Scope:**  
  Design and implement AI-based agents to automate routine software engineering activities, optimize workflows, and integrate seamlessly into the engineering ecosystem.

- **Core Objectives:**  
  - Establish a centralized, scalable knowledge base for storing and processing critical engineering artifacts, including requirements, design specifications, and coding guidelines.
  - Develop sophisticated algorithms to analyze requirements and generate high-level architectural designs and detailed plans.
  - Automate the generation of comprehensive design documentation with iterative feedback mechanisms for engineering teams.
  - Create reusable, standards-compliant code templates to expedite development efforts.
  - Implement robust mechanisms for auto-generating detailed code documentation.
  - Automate the creation and execution of test plans and test cases, ensuring high-quality validation of software products.
  - Deliver concise, aggregated notifications summarizing updates from multiple tools, eliminating notification fatigue and redundant information.

## Technical Highlights

- **Knowledge Graphs:**  
  Developed and deployed knowledge graphs as the core data structure for managing interconnected, heterogeneous datasets. This enables efficient storage, retrieval, and querying of engineering-related information.
  
- **Advanced Graph Algorithms:**  
  Utilized graph algorithms for dimensionality reduction and the creation of concise, actionable notifications by aggregating relevant updates.

- **API Integration Framework:**  
  Engineered harmonized APIs for seamless integration with widely used development tools such as Jira, Confluence, Jama Connect, GitHub, and Bitbucket. RESTful APIs ensure robust and secure communication across platforms.

- **Custom AI Agent Framework:**  
  Built a proprietary agent framework capable of interfacing with decentralized databases (e.g., MongoDB) and external tools to perform tasks such as software diagram generation, code synthesis, and test plan creation.

- **Code and Design Automation:**  
  - Auto-generated detailed software diagrams adhering to predefined templates set by engineering teams.  
  - Implemented code generation mechanisms enforcing compliance with custom coding standards, exceeding current state-of-the-art capabilities.  

- **Scalable Architecture:**  
  Designed a decentralized database architecture for handling large-scale data with load balancing, ensuring high availability and reliability.  
  Teams are provided dedicated access to Azure OpenAI services, reducing contention and maintaining performance scalability.  

- **Asynchronous Processing:**  
  Enabled asynchronous operation for AI agents, allowing engineers to work uninterrupted while complex outputs are generated in the background.

- **Custom User Interfaces:**  
  - Developed a user-friendly interface using Streamlit to enhance accessibility for engineering tasks.  
  - Built a VS Code extension to act as a direct proxy for agent interactions, streamlining workflows.

- **Deployment**

  - The LLM are hosted on Azure AI foundry and respective actions are taken for observability and data monitoring scripts.
  - Deployments are made through creating containers and are deployed on Openshift.
  - Created CI/CD pipelines using GitHub Actions and Jenkins.
  - Automated Unit tests to ensure the compabilities.
  - As we have created a distributed system (Each team having their own instance of Database and API keys), these deployments are helpful.

## Achievements

- Demonstrated superior quality in auto-generated documentation and test cases, surpassing manually curated outputs.
- Achieved a 20x reduction in task completion time, optimizing the efficiency of engineering teams.
- Minimized cognitive overhead and distraction by consolidating information and reducing tool-switching during development workflows.
- Successfully integrated with key engineering tools (Jira, Confluence, Jama Connect, GitHub, Bitbucket) for seamless information retrieval and aggregation.

## Key Performance Indicators (KPIs)

- **Scalability Metrics:**  
  - Handled exponential growth in data volumes using decentralized databases.  
  - Orchestrated workloads across team-specific environments while ensuring data security and compliance.

- **Efficiency Metrics:**  
  - Time savings per task, estimated at 20x compared to manual effort.  
  - Reduction in redundant notifications by 90%, aggregating updates into actionable summaries.

- **Accuracy and Adoption Metrics:**  
  - Generated outputs with compliance exceeding 95% against engineering team standards.  
  - Adoption rate tracked across engineering teams, showing consistent engagement and satisfaction.  

## Impact

- Delivered a unified interface consolidating information from multiple tools, enabling engineers to focus on core development activities.
- Streamlined workflows enhanced productivity and contributed to higher-quality product outcomes.
- The project set a benchmark for engineering efficiency through AI-driven automation.

## Tools and Technologies

- **Programming Languages:** Python, TypeScript  
- **Development Tools:** Visual Studio Code, Ollama, Azure OpenAI Services, Neo4j, ChromaDB, MongoDB, OpenShift, GitHub, Bitbucket  
- **Libraries/Frameworks:** PyTorch, OpenAI APIs, VS Code APIs, NetworkX