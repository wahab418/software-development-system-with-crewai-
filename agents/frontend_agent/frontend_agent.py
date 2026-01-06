from crewai import Agent
from crewai.llm import LLM
from crewai_tools import FileWriterTool

file_writer_tool = FileWriterTool()

frontend_agent = Agent(
    role="Frontend Developer",
    goal="Generate frontend project files and write them to disk using FileWriterTool",
    backstory=(
        "You are a senior frontend developer.\n"
        "You analyze the project description and choose the best frontend stack.\n"
        "You MUST create frontend files using FileWriterTool ONLY.\n"
        "FileWriterTool requires:\n"
        "  - filename\n"
        "  - content\n"
        "  - directory (FULL path)\n"
        "You NEVER return code as plain text.\n"
        "Each file must be written using a SEPARATE FileWriterTool call.\n"
        "You MUST call FileWriterTool.\n"
        "DO NOT explain.\n"
        "DO NOT describe.\n"
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

print("frontend agent initialized successfully")
