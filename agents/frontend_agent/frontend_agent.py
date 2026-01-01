from crewai import Agent
from crewai.llm import LLM
from crewai_tools import FileWriterTool 

# Initialize the FileWriterTool
file_writer_tool = FileWriterTool()

# Define the Frontend Agent
frontend_agent = Agent(
    role="Frontend Developer",
    goal="Generate frontend project structure and write clean frontend code",
    backstory=(
        "You are a senior frontend developer. "
        "You must create all files using the FileWriterTool. "
        "Do NOT return code as plain text. "
        "Return structured actions for each file: filename, directory, overwrite=True, content. "
        "After writing files, return final output showing content of all files."
    ),
    tools=[file_writer_tool],  
    llm=LLM(model="ollama/gpt-oss:120b-cloud", base_url="http://localhost:11434"),
    verbose=True
)

print("frontend agent initialized successfully")
