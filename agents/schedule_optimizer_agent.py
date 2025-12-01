# agents/schedule_agent.py

class ScheduleAgent:
    def build_schedule(self, route):
        return {task: "10:00 AM" for task in route}
