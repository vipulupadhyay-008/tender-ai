from google.adk import Workflow
from src.agents.tender_analyzer import TenderAnalyzer
from src.agents.proposal_writer import ProposalWriter

def create_tender_workflow() -> Workflow:
    """Creates and returns the tender analysis and proposal drafting workflow."""
    analyzer = TenderAnalyzer()
    writer = ProposalWriter()
    
    workflow = Workflow(
        name="tender_workflow",
        edges=[
            ("START", analyzer),
            (analyzer, writer)
        ]
    )
    return workflow
