# agents/errand_intake_agent.py

class ErrandIntakeAgent:
    def process(self, errands):
        return [{"task": e, "location": "unknown"} for e in errands]
