# PoC AI Agents: Pipeline Integrity Multi-Agent System (PoC)

## 📌 Project Overview
**PoC AI Agents** is an advanced Proof of Concept (PoC) focused on revolutionizing risk assessment and pipeline integrity in the oil and gas industry. The system utilizes an Orchestrator-Specialist architecture powered by the **Google Agent Development Kit (ADK)** and Gemini-Flash.

The primary goal of this system is to analyze massive volumes of static operational parameters (pressure, depth, historical corrosion, etc.) and generate structured diagnoses in near real-time through Multiple Artificial Intelligence Agents collaborating simultaneously.

## 🎯 General Objective
To provide the maintenance and reliability engineering team with a unified interface (via A2A/Streaming) that processes the context of pipeline segments, assigns specific risk scores by threat, and consolidates an executive report on the integrity level and recommended actions (Mitigation Mechanisms), emulating the technical reasoning of an interdisciplinary panel of experts.

---

## 🤖 Multi-Agent System (MAS) Architecture

The OMEGA AI ecosystem is composed of asynchronous interaction led by a central node and satellite nodes:

### 1. Master Orchestrator (`orchestrator_agent`)
*   **Role:** The directive brain.
*   **Function:** Receives the natural language "query" from the user (e.g., *"What is the risk diagnosis of segment 1?"*). Its task is **Smart Routing**: through semantic reasoning (LLM), it analyzes what information is missing, invokes the database server (MCP) to extract the raw records of the segment, and **prepares and delegates in parallel** the respective information to the specialist agents, making runtime decisions to save unnecessary calls (costs/time).

### 2. Corrosion Specialist Agent (`corrosion_agent`)
*   **Role:** Chemical and Materials Expert.
*   **Function:** Takes environmental and metallurgical parameters (e.g., CO2, O2, Bacteria, Temperature) and injects reasoning based on standards (API Mechanisms, NACE) to determine the probabilistic severity of internal or external metal degradation. Returns the structured analysis explicitly as a JSON model.

### 3. Third-Party Damage Specialist Agent - DxT (`third_party_damage_agent`)
*   **Role:** Geomechanical and Prevention Expert.
*   **Function:** Analyzes the level of urban/rural anthropic activity around the pipeline versus the installed mitigation measures (e.g., Minimum Trench Depth, Signage, Concrete) to assess the probability of external machinery puncturing the pipeline. Returns a calculation and reasoning in JSON.

### 4. Consolidator Agent (`consolidator_agent`)
*   **Role:** The Consulting Engineer / Presenter.
*   **Function:** At the end of the orchestration (Fan-In), it takes the key alerts from all specialists issued on the fly by the orchestrator (`generate_compact_summary`) and produces a coherent technical and narrative verdict for the human eye. Avoids raw database jargon and prioritizes executive readability.

---

## 🛠️ Underlying Infrastructure and Components

### The Model Context Protocol (MCP) Server
*   Location: `mcp-server/app.py`
*   **The Secure Database:** The LLMs never have direct or hallucinatory contact with the SQL database. We built a local server compatible with the open **MCP** standard.
*   **Exposed Tools (`@mcp.tool`):** 
    *   `get_segment_by_id`: Fast $O(1)$ extraction of the required "piece of pipe" by unique identifier.
    *   `get_line_by_id`: Dynamic $O(1)$ grouper of all underlying segments of an operational master line.
    *   `get_all_segments`: Information dump for global analytical reports.
*   **Technology:** Powered by FastMCP, delivers isolated bi-directional connectivity using in-memory Hash tables for extreme low latency $O(1)$.

### Use of "Skills" (Modular Toolboxes)
The *Specialist* agents are not just giant prompts; they are programmed to use **Dynamic Skills** (ADK Skills) that can be loaded and combined depending on the diagnosis they must perform.
Some of the skills hosted in the `skills/` directories:
*   `evaluate-fluid-composition`: Analysis of the mixture index of the transported crude oil.
*   `evaluate-internal-inspection-tool-ili`: Analysis of calipers and thicknesses obtained in Intelligent PIG runs.
*   `evaluate-min-cover_depth-skill` and `evaluate-activity-level-skill`: Specific hard-coded functions (to standardize deterministic calculations) encapsulated as tools for the LLM model.

## 🚀 Deployment and Testing

### Running locally
This project uses several agents and an MCP server. To run the system locally, you need to configure your environment and start the development server.

**Step 1. Configure the Environment Variables**
The system requires a Google API key from AI Studio to function. You can find example environment files in the root folder and inside each agent's folder.
1. Copy the `.env.example` file to create your own `.env` file at the root of the project:
   ```bash
   cp .env.example .env
   ```
2. Open the newly created `.env` file and replace `"your-gemini-api-key-here"` with your actual API key. Keep `GOOGLE_GENAI_USE_VERTEXAI="False"` to ensure it connects properly.

**Step 2. Setup your dependencies**
Ensure you have `uv` installed, as the project heavily relies on it to manage virtual environments. The `run-locally.sh` script handles dependency synchronization.

**Step 3. Run the complete pipeline**
Execute the provided shell script from the root directory to spin up all the agents and the MCP server simultaneously:
```bash
./run-locally.sh
```

**What happens next?**
The script will sequentially start:
1. The MCP Server (Port: 8080)
2. Third-Party Damage Agent (Port: 8081)
3. Corrosion Agent (Port: 8082)
4. Consolidator Agent (Port: 8083)
5. Master Orchestrator (Port: 8000)

Once terminal logs show `All agents started!`, the Orchestrator allows querying and coordinates the specialized agents correctly. Press `Ctrl+C` to cleanly shut down all processes running on the background.

---
**Next Stop: Staging on Cloud Run!**
