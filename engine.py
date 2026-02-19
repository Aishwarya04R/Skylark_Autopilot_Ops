import pandas as pd

def check_compatibility(mission, pilot, drone):
    """
    The Core Brain: Detects all technical, financial, and logistical conflicts.
    """
    conflicts = []
    
    # 1. Weather Logic (IP43 Requirement)
    if mission['weather_forecast'] == 'Rainy' and 'IP43' not in str(drone['weather_resistance']):
        conflicts.append("⚠️ Weather Risk: Drone is not IP43 rated for rain.")

    # 2. Budget Logic
    duration = (pd.to_datetime(mission['end_date']) - pd.to_datetime(mission['start_date'])).days + 1
    total_cost = duration * pilot['daily_rate_inr']
    if total_cost > mission['mission_budget_inr']:
        conflicts.append(f"💰 Budget Overrun: Cost (₹{total_cost}) exceeds budget (₹{mission['mission_budget_inr']}).")

    # 3. Certification Logic (Matching Pilot to Mission Requirements)
    req_certs = [c.strip() for c in mission['required_certs'].split(',')]
    pilot_certs = [c.strip() for c in pilot['certifications'].split(',')]
    for cert in req_certs:
        if cert not in pilot_certs:
            conflicts.append(f"📜 Cert Gap: Pilot lacks required '{cert}' certification.")

    # 4. Equipment-Pilot Location Mismatch
    if pilot['location'] != drone['location']:
        conflicts.append(f"📍 Logistics Alert: Pilot is in {pilot['location']} but Drone is in {drone['location']}.")

    # 5. Status & Maintenance Checks
    if pilot['status'] != 'Available':
        conflicts.append(f"❌ Pilot Unavailable: Status is '{pilot['status']}'.")
    
    if drone['status'] == 'Maintenance':
        conflicts.append(f"🔧 Maintenance Alert: Drone {drone['drone_id']} is grounded.")

    return conflicts if conflicts else ["✅ Mission Ready: No conflicts detected."]

def suggest_urgent_reassignment(urgent_mission, all_pilots):
    """
    Heuristic for Urgent Reassignment: Finds pilots with matching skills 
    currently on lower-priority assignments.
    """
    # Look for pilots who are 'Assigned' but have the right skills
    potential = all_pilots[
        (all_pilots['status'] == 'Assigned') & 
        (all_pilots['skills'].str.contains(urgent_mission['required_skills']))
    ]
    
    if not potential.empty:
        candidate = potential.iloc[0]
        return f"💡 **AI Strategy:** Reassign **{candidate['name']}** from current assignment '{candidate['current_assignment']}'. They meet the requirements for this Urgent mission."
    
    return "❌ Critical: No eligible pilots found for reassignment."