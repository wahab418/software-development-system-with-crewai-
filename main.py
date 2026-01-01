from crewai import Crew
from crewai.llm import LLM

# planner imports
from agents.planner_agent.planner_agent import planner_agent
from tasks.planning_task.planning_task import planning_task

# frontend imports
from agents.frontend_agent.frontend_agent import frontend_agent
from tasks.frontend_task.frontend_task import frontend_task


llm = LLM(
    model="ollama/gpt-oss:120b-cloud",
    temperature=0.3,
    base_url="http://localhost:11434" ,

)

# Crew definition (merged safely)
crew = Crew(
    agents=[
        planner_agent,
        frontend_agent  
    ],
    tasks=[
        planning_task,
        frontend_task   
    ],
    planning=True,
    planning_llm=llm,
    verbose=True
)

# Kickoff
crew.kickoff(
    inputs={
        "project_description": "Create a simple weather app using HTML, CSS, and JavaScript",
        "base_path": "E:\frontend-output"   
    }
)

