FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY . /app

# Enable experimental A2A protocol or other features by syncing dependencies
RUN uv sync --frozen

# Assuming agent 1 handles A2A API over a specific port
ENV PORT=8001
EXPOSE 8001

# The API Server from ADK
CMD ["uv", "run", "adk", "api_server", "agent.py", "--port", "8001", "--host", "0.0.0.0"]
