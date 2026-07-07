from google.adk import Agent

def TenderAnalyzer() -> Agent:
    """Creates a Tender Analyzer agent that reviews tender descriptions and extracts key details."""
    return Agent(
        name="tender_analyzer",
        instruction=(
            "You are an expert Tender Analyst. Your job is to analyze the provided tender details "
            "and extract: 1. Main Objectives, 2. Key Deliverables, 3. Eligibility Criteria, "
            "and 4. Deadlines or timelines if mentioned. Present your analysis in a clear, "
            "structured markdown report."
        )
    )
