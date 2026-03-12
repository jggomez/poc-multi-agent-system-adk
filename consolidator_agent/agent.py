from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import Agent
from google.genai import types as genai_types
from pathlib import Path
import yaml
from dotenv import load_dotenv

load_dotenv()

yaml_path = Path(__file__).parent / "instructions" / "agent.yaml"
with open(yaml_path, "r", encoding="utf-8") as f:
    agent_config = yaml.safe_load(f)

root_agent = Agent(
    name=agent_config["name"],
    model=agent_config["model"],
    instruction=agent_config["instruction"],
    description=agent_config["description"],
    generate_content_config=genai_types.GenerateContentConfig(
        max_output_tokens=800,
        temperature=0.1,
    ),
    include_contents="none",
)

a2a_app = to_a2a(root_agent, port=8083)
