# Decision Log: Drone Operations AI Coordinator

**Author:** Aishwarya R.  
**Date:** February 2026  

## 1. Interpretation of "Urgent Reassignments"
My implementation views "Urgent" as a priority override. In a standard system, an "Assigned" pilot is a closed door. In this system, the AI identifies that human capital is fluid. If a mission is marked **Urgent**, the engine scans for pilots who possess the required skills but are currently tied to **Standard** priority projects. This "Displacement Logic" provides the coordinator with actionable intelligence to pivot resources instantly.

## 2. Technical Assumptions
- **Weather Safety:** I assumed that "IP43" is the minimum viable rating for any mission forecast labeled "Rainy." Any drone without this specific metadata is hard-blocked to prevent hardware loss.
- **Cost Inclusivity:** I assumed mission dates are inclusive. For a mission from the 6th to the 8th, the engine calculates 3 full days of pilot fees.
- **Location Logistics:** I assumed that while a location mismatch is a conflict, it is a solvable logistical challenge. Thus, it is presented as a "Warning" rather than a "Critical Block."

## 3. Chosen Trade-offs
- **Google Sheets vs. SQL:** For a high-context coordination role, a spreadsheet is often the "natural" tool for staff. By using Google Sheets as the backend, I ensured that data entry remains easy for non-developers while maintaining programmatic control via the API.
- **Modular Architecture:** I chose to separate the logic engine from the UI. While it would have been faster to write everything in one file, modularity ensures that the validation rules can be unit-tested independently in a production environment.

## 4. Future Improvements
Given more time, I would integrate:
- **Real-time Weather API:** Fetching live data instead of relying on static CSV forecasts.
- **Geofencing:** Using Google Maps API to calculate the exact shipping time for drones between locations.
- **Auth Layer:** A login system to distinguish between Coordinator and Pilot views.