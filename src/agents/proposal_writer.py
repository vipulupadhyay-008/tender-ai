from google.adk import Agent

def ProposalWriter() -> Agent:
    """Creates a Proposal Writer agent that drafts response proposals based on a tender analysis."""
    return Agent(
        name="proposal_writer",
        instruction=(
            "You are a professional Bid and Proposal Writer. Your job is to take a structured "
            "tender analysis report and draft a professional proposal response. The proposal should include: "
            "1. Executive Summary, 2. Proposed Solution Overview, 3. Methodology & Deliverables Alignment, "
            "and 4. Value Proposition. Write in an engaging, authoritative, and persuasive corporate tone."
        )
    )
