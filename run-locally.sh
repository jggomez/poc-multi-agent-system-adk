#!/bin/bash

# Kill any existing processes on these ports
echo "Stopping any existing processes on ports 8081-8084..."
lsof -ti:8081,8082,8083,8084 | xargs kill -9 2>/dev/null

# Set common environment variables for local development
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
export GOOGLE_CLOUD_LOCATION="us-central1"
export GOOGLE_GENAI_USE_VERTEXAI="False" # Use Gemini API locally
export GOOGLE_API_KEY="" # Put your google api key here

echo "Starting mcp server"
pushd mcp-server
uv sync
uv run python app.py &
MCP_SERVER_PID=$!
popd

sleep 2

echo "Starting third_party_damage_agent on port 8081..."
pushd third_party_damage_agent
uv sync
uv run python -m uvicorn agent:a2a_app --port 8081 &
THIRD_PARTY_DAMAGE_AGENT_PID=$!
popd

sleep 3

echo "Starting corrosion_agent on port 8082..."
pushd corrosion_agent
uv sync
uv run python -m uvicorn agent:a2a_app --port 8082 &
CORROSION_AGENT_PID=$!
popd

sleep 3

echo "Starting consolidator_agent on port 8083..."
pushd consolidator_agent
uv sync
uv run python -m uvicorn agent:a2a_app --port 8083 &
CONSOLIDATOR_AGENT_PID=$!
popd

sleep 3

export THIRD_PARTY_AGENT_CARD_URL=http://localhost:8081/.well-known/agent-card.json
export CORROSION_AGENT_CARD_URL=http://localhost:8082/.well-known/agent-card.json
export CONSOLIDATOR_AGENT_CARD_URL=http://localhost:8083/.well-known/agent-card.json

echo "Installing orchestrator_agent..."
pushd orchestrator_agent
uv sync
popd

echo "Starting orchestrator_agent on port 8004..."
uv run adk web --reload_agents
ORCHESTRATOR_PID=$!

# Wait a bit for them to start up
sleep 5


echo "All agents started!"
echo "Third Party Damage Agent: http://localhost:8081"
echo "Corrosion Agent: http://localhost:8082"
echo "Consolidator Agent: http://localhost:8083"
echo "Orchestrator Agent: http://127.0.0.1:8000"
echo ""
echo "Press Ctrl+C to stop all agents."

# Wait for all processes
trap "kill $MCP_SERVER_PID $THIRD_PARTY_DAMAGE_AGENT_PID $CORROSION_AGENT_PID $CONSOLIDATOR_AGENT_PID $ORCHESTRATOR_PID; exit" INT
wait
