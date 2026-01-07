from crewai import Agent
from crewai.llm import LLM
from crewai_tools import FileWriterTool, FileReadTool

# Initialize tools
file_writer_tool = FileWriterTool()
file_read_tool = FileReadTool()

frontend_agent = Agent(
    role="Frontend Developer",
    goal="Generate frontend project files and write them to disk using FileWriterTool",
    backstory=(
        "You are a senior frontend developer.\n"
        "You analyze the project description and choose the best frontend stack.\n"
        "You can read existing files using FileReadTool.\n"
        "You MUST create frontend files using FileWriterTool.\n"
        "FileWriterTool requires:\n"
        "  - filename\n"
        "  - content\n"
        "  - directory (FULL path)\n"
        "You NEVER return code as plain text.\n"
        "Each file must be written using a SEPARATE FileWriterTool call.\n"
        "DO NOT explain. ONLY call tools."
    ),
    allow_delegation=True,
    tools=[file_writer_tool, file_read_tool],  # Both tools added
    llm=LLM(
        model="ollama/qwen3-coder:480b-cloud",
        base_url="http://localhost:11434"
    ),
    max_iter=15,
    verbose=True
)

print("frontend agent initialized successfully")