from crewai import Crew
from crewai.llm import LLM

# ---------------- Planner Agent ----------------
# from agents.planner_agent.planner_agent import planner_agent
# from tasks.planning_task.planning_task import planning_task

# ---------------- Frontend Agent ----------------
# from agents.frontend_agent.frontend_agent import frontend_agent
# from tasks.frontend_task.frontend_task import frontend_task

# ---------------- Backend Agent ----------------
from agents.backend_agent.backend_agent import backend_agent
from tasks.backend_task.backend_task import backend_task

# ---------------- Code Enhancer Agent ----------------
# from agents.code_enhancer_agent.code_enhancer_agent import code_enhancer_agent
# from tasks.code_enhancer_task.code_enhancer_task import code_enhancer_task

# ---------------- LLM Setup ----------------
llm = LLM(
    model="ollama/qwen3-coder:480b-cloud",
    temperature=0.3,
    base_url="http://localhost:11434",
)

# ---------------- Crew Setup ----------------
crew = Crew(
    agents=[
        backend_agent
    ],
    tasks=[
        backend_task
    ],
    planning=True,
    planning_llm=llm,
    verbose=True
)

# ---------------- Kickoff ----------------
crew.kickoff(
    inputs={
        "project_description": "weather app",
        "base_path": "E:/autonomous_software_dev_crewai/output",
        "folder_path": "E:/autonomous_software_dev_crewai/output"  # for code enhancer
    }
)
