import os
from dotenv import load_dotenv
from src.workflows.tender_workflow import create_tender_workflow
from google.adk.runners import InMemoryRunner

# Load environment variables from .env file
load_dotenv()

def main():
    print("Initializing Tender AI Multi-Agent Workflow...")
    
    # 1. Create the workflow
    workflow = create_tender_workflow()
    
    # 2. Setup the runner
    runner = InMemoryRunner(agent=workflow)
    
    # 3. Check for API key
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key or gemini_key == "your_gemini_api_key_here":
        print("\n[WARNING] GEMINI_API_KEY is not set or is using the placeholder value in your .env file.")
        print("Please configure GEMINI_API_KEY in the '.env' file with a valid Google Gemini API key to run live inference.")
        print("\nScaffolding is complete! Project structure is fully set up and ready.")
        return

    # Sample tender input
    sample_tender = (
        "We are looking for a software development vendor to build a custom CRM system. "
        "The project must be completed within 6 months. "
        "Key deliverables: User authentication, customer contact management, pipeline tracking, and API integration. "
        "Eligibility: Vendors must have at least 3 years of experience in Python and React."
    )
    
    print("\nRunning workflow on sample tender:")
    print("-" * 50)
    print(sample_tender)
    print("-" * 50)
    
    try:
        # Run workflow
        print("Invoking agents...")
        response = runner.run(input=sample_tender)
        print("\n--- Workflow Execution Result ---")
        print(response)
    except Exception as e:
        print(f"\n[ERROR] Failed to execute workflow: {e}")
        print("Please ensure your GEMINI_API_KEY is valid and has sufficient quota/permissions.")

if __name__ == "__main__":
    main()
