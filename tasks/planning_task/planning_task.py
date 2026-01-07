from crewai import Task
from agents.planner_agent.planner_agent import planner_agent
# Planner Task

planning_task = Task(
    description=
        "Create a detailed development plan for an Autonomous Software "
        "Development System using CrewAI. "
        "The plan should include system architecture, agent responsibilities, "
        "development phases, and key deliverables."
    ,
    expected_output=
        "A structured development plan with phases, agent roles, "
        "and clear implementation steps."
    ,
    agent=planner_agent
)

print("task..............")