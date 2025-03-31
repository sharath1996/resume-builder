# My work description

## AI Agents for SW Testing.

This project is created in the intention to test the AI agents which can help the SW test engineers to effectively test the SW.

This project includes the following:

#### Generic AI agents framework

###### Capabilities

- Human In Loop capability.
- Loading of conversations from the database.
- Interface to database such as MongoDB and LanceDB(Vector Database)
- Interface to Generic UI block.
- Logging of the status. 
- Interactions with other agents.
- Interactions to external tools such as Jama Connect, Jira, github, Confluence and PDF parsers.

#### Agent - For knowledge base creation

###### Capabilities

- From the given sources, the agent will create knowledge base and store it in the vector database.
- It provides an interface to ask questions from the knowledge Base, this is simple RAG based solution.
- It encapsulates as independent agent.


#### Agent - For Requirement analysis

###### Capabilities

- For the given requirement, the agent will create reference document, which acts as a single point of reference for multiple other agents.
- This will be created by allowing the agent to ask questions from the requirement and test criteria,
- This process will be repeated until the agent has no more questions.
- Once the agents gets answers to all the questions, it will then preapare the test document.
- These documents can be enhanced by users either by modifying the document, or by providing the feedback to agents.

#### Agent - For Test Case creation

###### Capabilities

- For the given requirement, the agent will create multiple test cases with a pre-defined template.
- This template will be filled by the agent for the test-cases.
- These test-cases can then be exported as confluence pages or Jama test cases.

#### Agent - For Test Case execution

###### Capabilities

- For the given test-case, agent will execute the tests.
- In case of a failed test, agent will check if the failure is due to a setup issues or software bugs. 
- Agent will create Jira tickets, with detailed scenarios on how to replicate the issue.

## SW News

