import asyncio
from fastmcp import FastMCP

MCP_PORT = 8080

# Create the MCP server
mcp = FastMCP("OmegaServer")

# Static data simulating a database or knowledge base
import json
import os

data_file_path = os.path.join(os.path.dirname(__file__), "data.json")
try:
    with open(data_file_path, "r", encoding="utf-8") as f:
        STATIC_INFO = json.load(f)
except Exception as e:
    print(f"Error loading {data_file_path}: {e}")
    STATIC_INFO = []
SEGMENT_INDEX = {
    int(record["segment_id"]): record
    for record in STATIC_INFO
    if "segment_id" in record
}

LINE_INDEX = {}
for record in STATIC_INFO:
    l_id = record.get("line_id", record.get("Linea"))
    if l_id:
        if l_id not in LINE_INDEX:
            LINE_INDEX[l_id] = []
        LINE_INDEX[l_id].append(record)


@mcp.tool()
def get_segment_by_id(id: int) -> dict:
    """
    Get a specific segment by id.
    """
    print(f"[get_segment_by_id] id: {id}")
    record = SEGMENT_INDEX.get(int(id))
    if record:
        return record

    return f"Segment with id '{id}' not found."


@mcp.tool()
def get_line_by_id(line_id: str) -> list[dict]:
    """
    Get a specific line by id.
    """
    print(f"[get_line_by_id] line_id: {line_id}")
    records = LINE_INDEX.get(line_id)
    if records:
        return records

    return f"Line with id '{line_id}' not found."


@mcp.tool()
def get_all_segments() -> list[dict]:
    """
    Retrieve all available segments.
    """
    return STATIC_INFO


if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    asyncio.run(
        mcp.run_async(
            transport="streamable-http",
            host="0.0.0.0",
            port=MCP_PORT,
        )
    )
