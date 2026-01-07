from crewai import Task
from agents.frontend_agent.frontend_agent import frontend_agent
from tasks.planning_task.planning_task import planning_task


frontend_task = Task(
    description=(               
        "Project Description:\n{project_description}\n\n"
        "Base Path (existing folder):\n{base_path}\n\n"
        "MANDATORY STEPS:\n"
        "1. Create ONE frontend project folder inside base_path.\n"
        "2. Decide frontend stack automatically.\n"
        "3. Create ALL required frontend files (HTML, CSS, JS, etc.).\n"
        "4. Use FileWriterTool for EACH file with:\n"
        "   - filename\n"
        "   - content\n"
        "   - directory (FULL path)\n\n"
        "EXAMPLE:\n"
        "FileWriterTool(filename='index.html', content='<!DOCTYPE html>...', directory='{base_path}/frontend-app')\n\n"
        "FAILURE CONDITIONS:\n"
        "- No frontend folder created → FAILED\n"
        "- No index.html created → FAILED\n"
        "- FileWriterTool not used → FAILED\n\n"
        "FINAL OUTPUT:\n"
        "- Mention FULL frontend folder path created.\n"
        "YOU MUST START by creating the frontend folder using FileWriterTool.\n"
        "DO NOT EXPLAIN. ONLY USE FileWriterTool."
    ),
    expected_output=(
        "Frontend files created on disk using FileWriterTool."
    ),
    agent=frontend_agent,
    context=[planning_task],  # Added - receives planner's output
)

print("frontend task initialized successfully")