![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
# Skylark Autopilot Ops: The Intelligent Resource Orchestrator

**🌐 [View Live Prototype](https://skylarkautopilotops-xv3tbvardbacuvdov4gzpg.streamlit.app/)**

Skylark Autopilot Ops is an intelligent orchestration platform designed for drone operations coordinators. It automates the complex task of matching pilots, drones, and missions while proactively mitigating risks through a custom constraint-satisfaction engine.

## Key Features
- **Intelligent Conflict Detection:** Real-time validation of weather resistance (IP43), pilot certifications, and budget margins.
- **Urgent Reassignment Protocol:** A priority-aware heuristic that identifies reassignment candidates when high-priority missions face resource shortages.
- **Bi-Directional Cloud Sync:** 2-way integration with Google Sheets, acting as a live distributed database for operational staff.
- **Logistics Alerting:** Automated warnings for pilot-equipment location mismatches.

## Tech Stack
- **Interface:** Streamlit (Custom CSS-enhanced Dashboard)
- **Engine:** Python / Pandas
- **Database:** Google Sheets API v4
- **Security:** Service Account OAuth2 Authentication

## Project Structure
- `app.py`: The professional dashboard and user interface.
- `engine.py`: The "Brain" containing all validation and reassignment logic.
- `database.py`: The data abstraction layer for Google Sheets communication.
- `credentials.json`: API authentication (Required for setup).

## Setup Instructions
1. Install dependencies: `pip install streamlit gspread oauth2client pandas`
2. Ensure `credentials.json` is in the root directory.
3. Share your Google Sheet with the Service Account email.

4. Run the app: `python -m streamlit run app.py`

