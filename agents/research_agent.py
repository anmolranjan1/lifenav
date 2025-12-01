# agents/research_agent.py

class ResearchAgent:
    def lookup(self, structured_errands):
        # Would call search tools here
        return [{"task": e["task"], "hours": "9am–9pm"} for e in structured_errands]
