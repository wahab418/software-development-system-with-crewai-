from crewai import Agent
from crewai.llm import LLM

planner_agent = Agent(
    role="Planner Agent",
    goal="Analyze requirements and create a step-by-step development plan.",
    backstory="Senior software architect who breaks ideas into execution plans.",
    allow_delegation=True,
    llm=LLM(model="ollama/qwen3-coder:480b-cloud", base_url="http://localhost:11434"),
    verbose=True
)

print("planner agent initialized successfully")