#!/usr/bin/env python
import sys
from .crew import KnowledgeGraphCrew

def run():
    """
    Run the crew.
    """
    print("Initializing Knowledge Graph Crew...")  
    crew = KnowledgeGraphCrew()

    inputs = {
        "topic": "CrewAI"  
    }

    response = crew.crew().kickoff(inputs=inputs)  
    return {"response": response}

if __name__ == "__main__":
    run()
