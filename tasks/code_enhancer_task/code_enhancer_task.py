# tasks/code_enhancer_task/code_enhancer_task.py

from crewai import Task
from agents.code_enhancer_agent.code_enhancer_agent import code_enhancer_agent
from crewai_tools import FileReadTool, FileWriterTool
import os

# Initialize tools to read and write files
file_reader = FileReadTool()
file_writer = FileWriterTool(result_as_answer=True)

def collect_code_files(base_path):
    """
    Recursively collect all code files in the base_path
    """
    code_files = []
    for root, _, files in os.walk(base_path):
        for f in files:
            if f.endswith((".js", ".ts", ".py", ".html", ".css")):  
                code_files.append(os.path.join(root, f))
    return code_files

def read_file_content(file_path):
    return file_reader(file_path=file_path)  

def write_enhanced_code(file_path, content):
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    return file_writer(filename=filename, content=content, directory=directory, overwrite=True)

# Define the task
code_enhancer_task = Task(
    description=(
        "Enhance and optimize all frontend and backend code in the project folder.\n"
        "You will read each file, send its content to the Code Enhancer Agent, and overwrite it with improved code.\n"
        "After enhancement, return the list of files updated."
    ),
    expected_output=(
        "All project code files enhanced and saved using FileWriterTool. "
        "Provide a confirmation message listing all enhanced files."
    ),
    agent=code_enhancer_agent
)

# Task execution logic
def run_code_enhancer_task(inputs):
    base_path = inputs.get("base_path")
    if not os.path.exists(base_path):
        return f"Error: Base path '{base_path}' does not exist."

    code_files = collect_code_files(base_path)
    enhanced_files = []

    for file_path in code_files:
        original_code = read_file_content(file_path=file_path)
        # Send code to enhancer agent
        enhanced_code = code_enhancer_agent.run({"code": original_code})  # returns enhanced code
        # Save enhanced code
        write_enhanced_code(file_path, enhanced_code)
        enhanced_files.append(file_path)

    return f"Enhanced {len(enhanced_files)} files:\n" + "\n".join(enhanced_files)
