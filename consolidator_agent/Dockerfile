FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY . /app

# Enable experimental A2A protocol or other features by syncing dependencies
RUN uv sync --frozen

# Assuming Consolidator handles A2A API over port 8003
ENV PORT=8003
EXPOSE 8003

# The API Server from ADK
CMD ["uv", "run", "adk", "api_server", "agent.py", "--port", "8003", "--host", "0.0.0.0"]
