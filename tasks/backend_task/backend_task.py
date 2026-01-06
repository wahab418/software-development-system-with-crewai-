from crewai import Task
from agents.backend_agent.backend_agent import backend_agent

backend_task = Task(
    description=(
        "Project Description:\n{project_description}\n\n"
        "Base Path (existing folder):\n{base_path}\n\n"
        "MANDATORY STEPS:\n"
        "1. Create ONE backend project folder inside base_path.\n"
        "2. Automatically decide backend language and framework.\n"
        "3. Create ALL required backend files (server, routes, config, etc.).\n"
        "4. Use FileWriterTool for EACH file with these arguments:\n"
        "   - filename: name of the file (e.g., 'server.js')\n"
        "   - content: the actual code content\n"
        "   - directory: FULL path to folder (e.g., '{base_path}/my-backend-app')\n\n"
        "EXAMPLE FileWriterTool call:\n"
        "FileWriterTool(filename='server.js', content='const express = require...', directory='{base_path}/weather-backend')\n\n"
        "FAILURE CONDITIONS:\n"
        "- No backend folder created → FAILED\n"
        "- No backend server file → FAILED\n"
        "- FileWriterTool not used → FAILED\n\n"
        "FINAL OUTPUT:\n"
        "- Mention the FULL backend folder path created."
        """YOU MUST START by creating the backend folder using FileWriterTool.
           YOU MUST THEN create server file using FileWriterTool.
           DO NOT EXPLAIN. ONLY USE FileWriterTool."""
    ),
    expected_output=(
        "Backend files created on disk using FileWriterTool with filename, content, and directory arguments. Final folder path returned."
    ),
    agent=backend_agent,
)

print("backend task initialized successfully")