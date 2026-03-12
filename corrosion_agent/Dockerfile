FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY . /app

# Enable experimental A2A protocol or other features by syncing dependencies
RUN uv sync --frozen

# Assuming agent 2 handles A2A API over port 8002
ENV PORT=8002
EXPOSE 8002

# The API Server from ADK
CMD ["uv", "run", "adk", "api_server", "agent.py", "--port", "8002", "--host", "0.0.0.0"]
