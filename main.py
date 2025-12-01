# main.py
# Entry point for LifeNav demo

from agents.orchestrator import OrchestratorAgent

def run_demo():
    errands = [
        "Costco grocery trip",
        "Walgreens pharmacy pickup",
        "Home Depot pickup",
        "UPS dropoff"
    ]

    orchestrator = OrchestratorAgent()
    result = orchestrator.run(errands)

    print("\n=== LIFE NAV PLAN ===")
    print(result)

if __name__ == "__main__":
    run_demo()
