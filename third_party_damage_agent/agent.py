import os
import yaml
from pathlib import Path
from google.adk.agents import Agent, SequentialAgent
from pydantic import BaseModel, Field
from typing import Union
from google.genai import types as genai_types

from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.skills import load_skill_from_dir
from google.adk.tools.skill_toolset import SkillToolset
from dotenv import load_dotenv

load_dotenv()

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://0.0.0.0:8080/mcp")

yaml_path = Path(__file__).parent / "instructions" / "agent.yaml"
with open(yaml_path, "r", encoding="utf-8") as f:
    agent_config = yaml.safe_load(f)

evaluate_activity_level_skill = load_skill_from_dir(
    Path(__file__).parent / "skills" / "evaluate-activity-level"
)

evaluate_min_cover_depth_skill = load_skill_from_dir(
    Path(__file__).parent / "skills" / "evaluate-min-cover-depth"
)


probability_variables_orchestrator_skill = load_skill_from_dir(
    Path(__file__).parent / "skills" / "probability-variables-orchestrator"
)

my_skill_toolset = SkillToolset(
    [
        evaluate_activity_level_skill,
        evaluate_min_cover_depth_skill,
        probability_variables_orchestrator_skill,
    ]
)


class VariableEvaluation(BaseModel):
    name: str = Field(description="The name of the evaluated variable.")
    value: Union[float, str] = Field(
        description="The evaluated value of the variable (e.g., 1.2, 'medium', 'concrete')."
    )
    points: float = Field(description="The points assigned to this variable.")
    technical_insight: str = Field(
        description="A technical sentence explaining the score."
    )


class AnalyzerOutput(BaseModel):
    agent_id: str = Field(description="The ID of the agent, e.g., 'prob_damage'.")
    score_total: float = Field(description="The total calculated score.")
    confidence_level: float = Field(
        description="The confidence level of the analysis, between 0.0 and 1.0."
    )
    variables_evaluated: list[VariableEvaluation] = Field(
        description="A list of evaluated variables."
    )
    global_summary: str = Field(description="A global summary of the risk or analysis.")
    manual_reference: str = Field(
        description="A reference to the manual or regulations used."
    )


data_gathering_agent = Agent(
    name=agent_config.get("name"),
    model=agent_config.get("model"),
    instruction=agent_config.get("instruction"),
    description=agent_config.get("description"),
    generate_content_config=genai_types.GenerateContentConfig(
        max_output_tokens=800,
        temperature=0.1,
    ),
    tools=[
        my_skill_toolset,
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=MCP_SERVER_URL,
            ),
        ),
    ],
    output_key="gathered_data",
    include_contents="none",
)

formatting_agent = Agent(
    name="formatting_agent",
    model=agent_config.get("model", "gemini-3-flash-preview"),
    instruction=(
        "You are an expert formatting agent. Take the unstructured gathered data "
        "provided below and structure it strictly into the requested JSON schema.\n"
        "Data:\n{gathered_data}"
    ),
    description="Formats unstructured analysis into structured JSON.",
    generate_content_config=genai_types.GenerateContentConfig(
        max_output_tokens=800,
        temperature=0.1,
    ),
    output_schema=AnalyzerOutput,
    include_contents="none",
)

root_agent = SequentialAgent(
    name="third_party_damage_pipeline_agent",
    sub_agents=[data_gathering_agent, formatting_agent],
)

a2a_app = to_a2a(root_agent, port=8081)
