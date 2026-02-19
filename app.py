import streamlit as st
import pandas as pd
from database import get_data, update_pilot_status
from engine import check_compatibility, suggest_urgent_reassignment

# --- Advanced Page Configuration ---
st.set_page_config(
    page_title="Skylark Mission Control",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Advanced Page Configuration ---
st.set_page_config(
    page_title="Skylark Mission Control",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Updated Professional & Readable Styling ---
st.markdown("""
    <style>
    /* Main Background */
    .main { background-color: #f8f9fa; color: #212529; }
    
    /* Professional Light Cards for Mission Dispatch */
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        color: #343a40 !important; /* Forces dark text for visibility */
    }
    
    .metric-card b {
        color: #6c757d;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-card span {
        display: block;
        font-size: 1.1rem;
        font-weight: 600;
        color: #212529;
    }

    /* Keep the Urgent Alert Pulsing */
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(255, 75, 75, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0); }
    }
    .urgent-box {
        background-color: #fff5f5;
        border: 2px solid #ff4b4b;
        padding: 15px;
        border-radius: 10px;
        color: #212529;
        animation: pulse 2s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
col_h1, col_h2 = st.columns([4, 1])
with col_h1:
    st.title("🛸 Skylark Autopilot Ops: The Intelligent Resource Orchestrator")
    st.caption("AI-Powered Operations Coordination Systems v2.0")
with col_h2:
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

st.markdown("---")

# --- Step 1: Data Fetching ---
try:
    missions_df = get_data("missions")
    pilots_df = get_data("pilot_roster")
    drones_df = get_data("drone_fleet")
except Exception as e:
    st.error(f"📡 Connection Error: Ensure Google Sheet is shared and API is active. Details: {e}")
    st.stop()

# --- Sidebar: Operational Overview ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/drone.png", width=80)
    st.header("Fleet Intelligence")
    
    # Live Metrics
    active_missions = len(missions_df)
    avail_pilots = len(pilots_df[pilots_df['status'] == 'Available'])
    ready_drones = len(drones_df[drones_df['status'] == 'Available'])
    
    st.metric("Total Missions", active_missions)
    st.metric("Available Pilots", avail_pilots)
    st.metric("Flight-Ready Drones", ready_drones)
    
    st.markdown("---")
    st.subheader("⚠️ Urgent Action Required")
    urgent_items = missions_df[missions_df['priority'] == 'Urgent']
    for _, item in urgent_items.iterrows():
        st.error(f"**{item['project_id']}**: {item['location']}")

# --- Main Dashboard Tabs ---
tab1, tab2, tab3 = st.tabs(["🎯 Mission Assignment", "👥 Roster Management", "🚁 Drone Inventory"])

with tab1:
    # Mission Selection Row
    st.subheader("Mission Dispatcher")
    selected_id = st.selectbox("Search Project ID", missions_df['project_id'], label_visibility="collapsed")
    m_data = missions_df[missions_df['project_id'] == selected_id].iloc[0]

    # Info Cards with New Styling
    with st.container():
        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f"<div class='metric-card'><b>Priority</b><br><span style='color:#ff4b4b'>{m_data['priority']}</span></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='metric-card'><b>Forecast</b><br><span>{m_data['weather_forecast']}</span></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='metric-card'><b>Budget</b><br><span>₹{m_data['mission_budget_inr']}</span></div>", unsafe_allow_html=True)
        c4.markdown(f"<div class='metric-card'><b>Required Skill</b><br><span>{m_data['required_skills']}</span></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # Assignment Logic
    col_assign, col_conflicts = st.columns([1, 1.2])

    with col_assign:
        st.write("### 🛠️ Manual Configuration")
        with st.expander("Configure Crew & Equipment", expanded=True):
            p_id = st.selectbox("Select Pilot", pilots_df['pilot_id'] + " - " + pilots_df['name'])
            d_id = st.selectbox("Select Drone", drones_df['drone_id'] + " - " + drones_df['model'])
            
            p_row = pilots_df[pilots_df['pilot_id'] == p_id.split(" - ")[0]].iloc[0]
            d_row = drones_df[drones_df['drone_id'] == d_id.split(" - ")[0]].iloc[0]
            
            if st.button("🚀 Finalize & Sync Assignment"):
                with st.spinner("Writing to Secure Database..."):
                    res = update_pilot_status(p_row['pilot_id'], "Assigned")
                    st.success(res)
                    st.balloons()

    with col_conflicts:
        st.write("### 🤖 Coordinator AI Insights")
        
        # Conflict Logic Execution
        alerts = check_compatibility(m_data, p_row, d_row)
        
        for alert in alerts:
            if "✅" in alert:
                st.success(alert)
            else:
                st.error(alert)

        # Urgent Logic Display
        if m_data['priority'] == 'Urgent':
            st.markdown("<div class='urgent-box'>", unsafe_allow_html=True)
            st.write("**Urgent Reassignment Protocol:**")
            st.info(suggest_urgent_reassignment(m_data, pilots_df))
            st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Pilot Roster Database")
    st.dataframe(pilots_df, use_container_width=True)

with tab3:
    st.subheader("Drone Fleet Status")
    st.dataframe(drones_df, use_container_width=True)