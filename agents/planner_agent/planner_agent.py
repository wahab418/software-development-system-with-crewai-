from crewai import Agent
from crewai.llm import LLM

# llm = LLM(
#     model="ollama/llama3.2",
#     temperature=0.3,
# )

planner_agent = Agent(
    role="Planner Agent",
    goal="Analyze requirements and create a step-by-step development plan.",
    backstory="Senior software architect who breaks ideas into execution plans.",
    llm=LLM(model="ollama/gpt-oss:120b-cloud", base_url="http://localhost:11434"),
    verbose=True
)

print("planner.........")