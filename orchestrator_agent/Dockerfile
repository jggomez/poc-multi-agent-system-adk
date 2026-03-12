FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY . /app

# Sync dependencies
RUN uv sync --frozen

# Assuming Orchestrator handles requests directly on 8000 (standard web port)
# wait, fastmcp is already on 8000. Let's use 8004
ENV PORT=8004
EXPOSE 8004

# The API Server from ADK
CMD ["uv", "run", "adk", "api_server", "agent.py", "--port", "8004", "--host", "0.0.0.0"]
