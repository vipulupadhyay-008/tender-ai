# Tender AI Multi-Agent System

A multi-agent system built using the Google Agent Development Kit (ADK) to analyze tenders, proposals, and draft professional business responses.

## System Architecture

Below is the flowchart representing the Tender AI multi-agent workflow, demonstrating how documents are ingested, drafts are generated using reference data, and compliance checks are enforced with a human-in-the-loop review.

```mermaid
flowchart TD
    %% Styling Class Definitions
    classDef userStyle fill:#E1F5FE,stroke:#0288D1,stroke-width:2px,color:#01579B;
    classDef agentStyle fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#311B92;
    classDef dbStyle fill:#EFEBE9,stroke:#5D4037,stroke-width:2px,color:#3E2723;
    classDef actionStyle fill:#FFF3E0,stroke:#F57C00,stroke-width:2px,color:#E65100;
    classDef decisionStyle fill:#FFEBEE,stroke:#C62828,stroke-width:2px,color:#B71C1C;
    classDef successStyle fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20;

    %% Nodes & Shapes
    UserNode["👤 User"]:::userStyle
    UploadDoc["📄 Uploads Document"]:::actionStyle
    
    subgraph IntakePhase["1. Intake & Analysis Phase"]
        IntakeAgent["🤖 Intake Agent (Tender Analyzer)"]:::agentStyle
        ExtractRequirements["📋 Extract Key Requirements"]:::actionStyle
    end
    
    subgraph WritingPhase["2. Response Generation Phase"]
        WriterAgent["🤖 Writer Agent (Proposal Writer)"]:::agentStyle
        MockDB[("🗄️ Mock Database (Reference Context)")]:::dbStyle
        DraftResponse["📝 Draft Response Proposal"]:::actionStyle
    end
    
    subgraph CompliancePhase["3. Risk & Compliance Phase"]
        ComplianceAgent["🤖 Compliance Agent"]:::agentStyle
        RiskReport["⚠️ Risk Analysis & Verification"]:::actionStyle
        HITL["💻 Human-in-the-Loop (Terminal Prompt)"]:::userStyle
    end
    
    DecisionNode{"Approved by Human?"}:::decisionStyle
    FinalOutput["🚀 Final Approved Response"]:::successStyle
    Revisions["🔄 Revisions Needed"]:::actionStyle

    %% Flow Connections
    UserNode --> UploadDoc
    UploadDoc --> IntakeAgent
    IntakeAgent --> ExtractRequirements
    ExtractRequirements --> WriterAgent
    
    WriterAgent <-->|Queries Templates / History| MockDB
    WriterAgent --> DraftResponse
    DraftResponse --> ComplianceAgent
    
    ComplianceAgent --> RiskReport
    RiskReport --> HITL
    HITL --> DecisionNode
    
    DecisionNode -->|Yes| FinalOutput
    DecisionNode -->|No| Revisions
    Revisions --> WriterAgent
```

## Setup Instructions

1. **Prerequisites**:
   - Python 3.10 or higher
   - API access to Google Gemini models (set `GEMINI_API_KEY`)

2. **Virtual Environment**:
   Ensure the virtual environment is set up and active:
   ```bash
   # Windows PowerShell
   .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Copy `.env` and set your Google Gemini API Key:
   ```bash
   # Add your key to .env
   GEMINI_API_KEY=your-api-key-here
   ```

## Running the Application

To run the default workflow:
```bash
python main.py
```

## Project Structure

- `src/` - Application source code
  - `agents/` - Custom ADK Agents (e.g. `TenderAnalyzer`, `ProposalWriter`)
  - `workflows/` - Orchestration logic connecting agents
  - `tools/` - Reusable functions and tools utilized by agents
- `main.py` - Main runner script
