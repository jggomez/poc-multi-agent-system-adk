import os
import yaml
import json
from pathlib import Path
from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import ToolContext, FunctionTool
from google.genai import types as genai_types
from dotenv import load_dotenv

load_dotenv()

yaml_path = Path(__file__).parent / "instructions" / "agent.yaml"
with open(yaml_path, "r", encoding="utf-8") as f:
    agent_config = yaml.safe_load(f)


def create_save_output_callback(key: str):
    """Creates a callback to save the agent's final response to session state."""

    def callback(callback_context: CallbackContext, **kwargs) -> None:
        ctx = callback_context
        for event in reversed(ctx.session.events):
            if event.author == ctx.agent_name and event.content and event.content.parts:
                text = event.content.parts[0].text
                if text:
                    if text.strip().startswith("{"):
                        try:
                            ctx.state[key] = json.loads(text)
                        except json.JSONDecodeError:
                            ctx.state[key] = text
                    else:
                        ctx.state[key] = text
                    print(f"[{ctx.agent_name}] Saved output to state['{key}']")
                    return

    return callback


third_party_agent_url = os.environ.get(
    "THIRD_PARTY_AGENT_CARD_URL",
    "http://localhost:8081/.well-known/agent-card.json",
)

third_party_agent = RemoteA2aAgent(
    name="third_party_agent",
    agent_card=third_party_agent_url,
    description="Gathers information using Google Search.",
    after_agent_callback=create_save_output_callback("third_party_findings"),
)

corrosion_agent_url = os.environ.get(
    "CORROSION_AGENT_CARD_URL",
    "http://localhost:8082/.well-known/agent-card.json",
)

corrosion_agent = RemoteA2aAgent(
    name="corrosion_agent",
    agent_card=corrosion_agent_url,
    description="Analyzes corrosion risk.",
    after_agent_callback=create_save_output_callback("corrosion_findings"),
)

consolidator_agent_url = os.environ.get(
    "CONSOLIDATOR_AGENT_CARD_URL",
    "http://localhost:8083/.well-known/agent-card.json",
)

consolidator_agent = RemoteA2aAgent(
    name="consolidator_agent",
    agent_card=consolidator_agent_url,
    description="Consolidates analysis results.",
)


def generate_compact_summary(segment_id: str, tool_context: ToolContext) -> str:
    """Generates a compact summary of the findings to be sent to the consolidator.
    Call this tool after the specialists have finished, and pass its exact output to the consolidator_agent.
    """
    state = tool_context.state
    tp = state.get("third_party_findings", {})
    corr = state.get("corrosion_findings", {})

    tp_score = tp.get("score_total", "N/A") if isinstance(tp, dict) else "N/A"
    tp_summary = tp.get("global_summary", "N/A") if isinstance(tp, dict) else "N/A"

    corr_score = corr.get("score_total", "N/A") if isinstance(corr, dict) else "N/A"
    corr_summary = (
        corr.get("global_summary", "N/A") if isinstance(corr, dict) else "N/A"
    )

    return f"Segment: {segment_id}\\nThird-Party Damage: {tp_score} pts. {tp_summary}\\nCorrosion: {corr_score} pts. {corr_summary}"


root_agent = Agent(
    name=agent_config.get("name"),
    model=agent_config.get("model"),
    instruction=agent_config.get("instruction"),
    description=agent_config.get("description"),
    generate_content_config=genai_types.GenerateContentConfig(
        max_output_tokens=800,
        temperature=0.1,
    ),
    tools=[
        AgentTool(third_party_agent),
        AgentTool(corrosion_agent),
        FunctionTool(generate_compact_summary),
        AgentTool(consolidator_agent),
    ],
)
