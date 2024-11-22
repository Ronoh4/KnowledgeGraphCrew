from crewai.project import CrewBase, agent, crew, task
from crewai import Agent, Crew, Process, Task
from .tools.custom_tools import KnowledgeGraphTool, OrganicSearchTool
from dotenv import load_dotenv
from crewai_tools import ScrapeWebsiteTool
import os

load_dotenv()
serper_api_key = os.getenv('SERPER_API_KEY')

scrape_tool = ScrapeWebsiteTool()

@CrewBase
class KnowledgeGraphCrew:
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[KnowledgeGraphTool(), OrganicSearchTool(), scrape_tool],
            verbose=True,
            llm="openai/gpt-4o"
        )

    @agent
    def reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['reporter'],
            verbose=True,
            llm="openai/gpt-4o-mini"
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], 
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Define the order in which tasks will run
            verbose=True,
        )
