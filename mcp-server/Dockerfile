FROM python:3.12-slim

WORKDIR /app

# Install uv for dependency management
RUN pip install uv

# Copy the pyproject.toml and source code
COPY . /app

# Install dependencies using uv
RUN uv sync --frozen

# Expose port (if needed, though standard MCP often uses stdio)
# For testing with A2A or network, FastMCP can run over SSE.
# Since ADK relies on stdio for local MCPs, or SSE for remote.
# Let's assume this might run over SSE on port 8000 when deployed to Cloud Run.
ENV PORT=8000
EXPOSE 8000

# Run the FastMCP server via the uv environment
# To use SSE we need to start it properly, but for now we run the script.
# FastMCP uses `mcp run app.py` or just `python app.py`
CMD ["uv", "run", "fastmcp", "run", "app.py", "--transport", "sse", "--port", "8000", "--host", "0.0.0.0"]
