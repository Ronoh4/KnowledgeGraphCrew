Knowledge Graph & General Google Search Agent System
This project leverages crewAI to build an intelligent agent system that prioritizes information from Google's Knowledge Graph for reliability. If no relevant data is found, it reverts to a General Google Search to scrape the top two URLs from the organic results, ensuring accurate and comprehensive information retrieval about entities, organizations, or individuals.

Key Features:
Knowledge Graph Tool: Extracts structured data from Google's Knowledge Graph, offering reliable, curated information.
Organic Search Tool: If no Knowledge Graph data is available, it performs a Google search and scrapes the top 2 URLs from organic search results.
Web Scraping Tool: Built using crewAI's ScrapeWebsiteTool, this tool extracts content from the selected top URLs for deeper insights.
The system integrates two custom tools—KnowledgeGraphTool and OrganicSearchTool—to gather and process the data, and a crewAI built-in tool, ScrapeWebsiteTool, to scrape web pages.

Customization:

Clone the repository:
To modify the system for your own use, clone the repository:

bash

git clone git@github.com:Ronoh4/KnowledgeGraphCrew.git
cd your-repository
Modify agents.yaml:
Define the behavior and configuration of your agents.

Modify tasks.yaml:
Adjust tasks and objectives that agents will perform.

Extend with Custom Tools:
Customize custom_tools.py to add new tools or modify existing ones to better suit your needs.

Running the Project:
To run the system and begin agent collaboration:

bash
crewai run
This command will initialize the agents, allowing them to gather and analyze data automatically, based on the configuration you've set.