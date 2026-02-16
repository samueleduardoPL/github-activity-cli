# github-activity-cli

A layered command-line application that fetches and formats a user's public GitHub activity using the GitHub REST API.

This project was built following a layered architecture approach:

UI Layer → Handles CLI interaction

Domain Layer → Contains business logic

Data Layer → Communicates with the GitHub API

# 📦 Project Structure
githubactivity/
│
├── main.py
├── ui/
│   └── cli.py
├── domain/
│   └── services.py
└── data/
    └── repository.py

# 🚀 How to Run
From the src directory:
    python -m githubactivity.main <username>

# 🧠 What It Does

Calls the GitHub API endpoint:
/users/{username}/events

Groups events by type
Counts how many times each event occurred per repository
Prints a formatted, human-readable summary
    
# ⚠️ Possible Errors Handled

404 → User not found
403 → API rate limit exceeded
Network errors → Connection issues

# 🏗 Architecture

This project follows a Layered Architecture pattern:
    Clear separation of concerns
    Business logic isolated from UI
    External API access isolated from domain logic
    This improves maintainability, readability, and scalability.

# 🔧 Technologies Used

-Python 3.12
-argparse
-urllib
-GitHub REST API




