# Verizon 4 SQL AutoBI Tool

## Oveview
The SQL Query Generator is an app designed to create SQL queries based on natural language prompts. It uses:

- Google Gemini API for generating SQL queries.
- Flask as the backend framework.
- Flet as the frontend framework for building a GUI.

## Getting Started

First set up a virtual environment in the repo directory. Then, run the makefile to start the frontend and backend:
```
make start
```
- If you get an error saying port 5011 is already in use, kill the tasks running on that port (or just change the number in backend/app.py and frontend/fletty.py)
