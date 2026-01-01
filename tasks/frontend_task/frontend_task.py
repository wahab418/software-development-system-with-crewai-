from crewai import Task
from agents.frontend_agent.frontend_agent import frontend_agent

frontend_task = Task(
    description=(
    "You will receive:\n"
    "1. project_description\n"
    "2. base_path (this is an existing folder on the local PC)\n\n"
    "Your task:\n"
    "- Create a project folder INSIDE base_path\n"
    "- The folder name should be derived from the project description\n"
    "- Inside the folder, create:\n"
    "  - index.html\n"
    "  - style.css\n"
    "  - script.js\n"
    "- Write clean frontend code\n"
    "- Use ONLY the FileWriterTool\n"
    "- At the end, mention the full folder path where files were saved"
    ),
    expected_output=(
    "Frontend files created on disk inside the provided base_path. "
    "The output includes the full folder path."
),
    agent=frontend_agent
)
print("frontend task initialized successfully")