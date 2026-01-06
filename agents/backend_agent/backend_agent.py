from crewai import Agent
from crewai.llm import LLM
from crewai_tools import FileWriterTool

file_writer_tool = FileWriterTool()

backend_agent = Agent(
    role="Backend Developer",
    goal="Generate backend project files and write them to disk using FileWriterTool",
    backstory=(
        "You are a senior backend developer.\n"
        "You analyze the project topic and automatically choose the best backend language and framework.\n"
        "You MUST create backend files using FileWriterTool ONLY.\n"
        "FileWriterTool requires these arguments:\n"
        "  - filename: The name of the file (e.g., 'server.js')\n"
        "  - content: The actual code content\n"
        "  - directory: The FULL path to the folder\n"
        "You NEVER return code as plain text.\n"
        "Each backend file must be written using a separate FileWriterTool call.\n"
        "If files are not written, the task is FAILED."
        "You MUST call FileWriterTool.\n"
        "DO NOT describe.\n"
        "DO NOT explain.\n"
        "ONLY call FileWriterTool.\n"
        "If no tool call happens, you FAILED."
    ),
    tools=[file_writer_tool],
    llm=LLM(
        model="ollama/qwen3-coder:480b-cloud",
        base_url="http://localhost:11434"
    ),
    max_iter=15,
    verbose=True
)

print("backend agent initialized successfully")