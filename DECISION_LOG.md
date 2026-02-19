# Decision Log: Skylark Autopilot Ops

**Project:** AI-Powered Drone Operations Coordinator  
**Candidate:** Aishwarya R.  
**Date:** February 19, 2026  

---

## 1. Interpretation of "Urgent Reassignments"
In drone operations, **"Urgent"** implies a mission with zero lead time and high stakes (e.g., emergency surveillance or time-sensitive delivery). My implementation views "Urgent" as a **priority override** rather than a standard booking.

* **The Heuristic:** I implemented a **Priority-Displacement Algorithm**. If a mission is tagged as "Urgent" and no matching pilots are currently "Available," the AI automatically scans the roster for pilots who possess the required skills but are currently assigned to "Standard" priority missions.
* **Actionable Intelligence:** The system doesn't just display an error; it identifies the specific pilot and the mission they would be "pulled" from. This allows the coordinator to make an informed executive decision to pivot resources to the highest-value task.

---

## 2. Key Assumptions Made
To build a robust logic engine, I established the following operational boundaries:

| Category | Assumption Made | Rational |
| :--- | :--- | :--- |
| **Weather Safety** | "Rainy" forecast requires a hard-coded IP43 rating. | To prevent hardware loss, I assumed a "Safety-First" approach where drones without water resistance are hard-blocked for rain. |
| **Financials** | Mission dates are **Inclusive**. | A mission from May 1st to May 2nd is calculated as 2 full days of pilot daily rates. |
| **Logistics** | Location Mismatch is a **Warning**, not a Block. | I assumed equipment or pilots can be transported if the budget allows; the system flags it as an alert rather than a critical failure. |
| **Certifications** | Certs are **Binary Constraints**. | Unlike skills, certifications are legal requirements. If a pilot lacks a required cert (e.g., "Night Flight"), they are disqualified. |

---

## 3. Technical Trade-offs Chosen & Why

### **A. Data Layer: Google Sheets API vs. SQL**
* **Decision:** Utilized Google Sheets as the primary database.
* **Why:** Operational staff often prefer a spreadsheet interface for manual updates. By using a 2-way sync, I ensured the "Source of Truth" remains accessible to non-developers.
* **Trade-off:** Sacrificed the query speed of an SQL database for the **collaborative accessibility** of a spreadsheet.

### **B. Frontend: Streamlit**
* **Decision:** Streamlit for the UI/UX.
* **Why:** Allowed for a **"Logic-First" development cycle**. I dedicated time to the `engine.py` logic and sync reliability rather than CSS boilerplate.
* **Trade-off:** Limited control over complex multi-page state management in exchange for **rapid deployment**.

---

## 4. Conflict Resolution Engine Logic
The "Brain" of the application (`engine.py`) uses a modular validation pattern. Assignments pass through four **"Sentinels"**:
1.  **The Weather Guard:** Cross-checks mission forecast against drone IP ratings.
2.  **The Budget Sentinel:** Compares calculated costs (Rate × Duration) against the mission budget.
3.  **The Compliance Officer:** Matches required certifications against the pilot's profile.
4.  **The Maintenance Monitor:** Grounds drones marked with "Maintenance" status.

---

## 5. What I’d Do Differently with More Time
* **Live Weather Integration:** Integrate the **OpenWeatherMap API** for real-time risk assessment based on coordinates.
* **Automated Notification Layer:** Implement **WhatsApp/Twilio API** to send "Deployment Orders" to pilots instantly.
* **Optimization Algorithm:** Upgrade reassignment logic to a **Cost-Optimization Algorithm** (finding the pilot with the lowest displacement "cost").
* **User Authentication:** Add a secure login layer to distinguish between "Coordinators" and "View-only" users.

---

## 6. Final Conclusion
**Skylark Autopilot Ops** successfully bridges the gap between static data and active operational coordination. By centralizing disparate data points into a single "Source of Truth," the system ensures that drone missions are planned with maximum safety and financial viability.
