LifeNav — Autonomous Personal Errand Planner

A multi-agent system that plans, optimizes, and schedules your weekly errands using research tools, routing algorithms, memory, and automated validation.

⭐ Overview

LifeNav takes a list of errands (groceries, pharmacy, drop-off, etc.) and automatically produces:

An optimized route

Store hours validation

Time-blocked weekly schedule

A corrected plan through a validation loop

Fully autonomous multi-agent workflow

This project is built for the Kaggle 5-Day Agents Intensive Capstone.

🧠 Why LifeNav?

Most people lose 2–5 hours/week planning errands manually:

figuring out store hours

checking which stores are nearby

deciding the best order to visit them

fitting errands into a busy weekly schedule

LifeNav completely automates this with agents + tools.

🚏 Architecture
High-Level Pipeline

User provides errands

Errand Intake Agent → structuring tasks

Research Agent → store hours, distance lookups

Route Optimizer Agent → fastest route tool

Schedule Agent → generates time-blocked plan

Validator Loop Agent → fixes issues automatically

Orchestrator → coordinates workflow end-to-end

🧩 Agents
Agent	Role
Orchestrator	Manages full workflow
Errand Intake Agent	Parses user errands
Research Agent	Gathers store hours & constraints
Route Optimizer Agent	Computes optimal route
Schedule Agent	Builds schedule with travel times
Validator Agent (LoopAgent)	Ensures correctness
🔧 Tools
Custom Tools

route_optimizer.py

search_tool.py

Built-in / External

Google Search Tool

Geopy for distance

Session & memory utilities

🧰 Setup
git clone https://github.com/YOUR_USERNAME/lifenav
cd lifenav
pip install -r requirements.txt
python main.py

🧪 Demo (example run)

Input:

Groceries, UPS dropoff, Walgreens pharmacy pickup, Home Depot


Output (summary):

Optimized order

Travel durations

Store hours verified

Schedule:

10:00 Costco

11:00 Home Depot

11:20 Walgreens

11:45 UPS

Total time: ~2.5 hr

🏗️ Tech Used

Google Agent Development Kit (ADK)

Gemini

Python

Multi-Agent Workflows

Loop Agents

Custom Tools

Session + Memory Bank

Context Compaction

Observability hooks

📈 Future Enhancements

Send schedule to Google Calendar

Live traffic-based routing

UI with map visualization

Weather-aware routing

Budget-aware store optimization