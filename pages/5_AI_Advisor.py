import streamlit as st

st.title("🤖 AI Traffic Advisor")

question = st.text_area(
    "Ask a traffic management question"
)

if st.button("Generate Advice"):

    q = question.lower()

    # Vehicle Breakdown
    if "breakdown" in q:

        st.success("""
🚗 Vehicle Breakdown Detected

Recommended Action:
• Deploy 2 Traffic Officers
• Send Tow Truck
• Activate Diversion Route
• Monitor Traffic for 20 minutes

Expected Risk Reduction: 35%
Expected Clearance Time: 20 minutes
""")

    # Water Logging
    elif "water" in q or "flood" in q:

        st.success("""
🌧 Water Logging Detected

Recommended Action:
• Deploy Drainage Team
• Install Barricades
• Divert Traffic
• Alert Nearby Zones

Expected Risk Reduction: 40%
Expected Clearance Time: 45 minutes
""")

    # Tree Fall
    elif "tree" in q:

        st.success("""
🌳 Tree Fall Detected

Recommended Action:
• Notify Forest Department
• Deploy 3 Officers
• Block Affected Lane
• Arrange Removal Vehicle

Expected Clearance Time: 30 minutes
""")

    # Potholes
    elif "pothole" in q:

        st.success("""
🛣 Pothole Hazard Detected

Recommended Action:
• Deploy Road Maintenance Team
• Install Warning Signboards
• Reduce Speed Limit
• Temporary Lane Restriction

Expected Clearance Time: 2 Hours
""")

    # Accident
    elif "accident" in q or "crash" in q:

        st.success("""
🚑 Road Accident Detected

Recommended Action:
• Deploy Ambulance
• Send 4 Traffic Officers
• Activate Diversion Route
• Inform Nearby Hospitals

Expected Risk Reduction: 50%
""")

    # Construction
    elif "construction" in q or "road work" in q:

        st.success("""
🚧 Construction Activity Detected

Recommended Action:
• Install Barricades
• Deploy 3 Officers
• Activate Alternate Routes
• Display Public Advisory

Expected Congestion Reduction: 30%
""")

    # Protest / Rally
    elif "protest" in q or "rally" in q:

        st.success("""
📢 Protest / Rally Detected

Recommended Action:
• Deploy Additional Officers
• Create Traffic Diversions
• Coordinate with Event Organizers
• Increase CCTV Monitoring

Expected Impact: High
""")

    # Festival
    elif "festival" in q:

        st.success("""
🎉 Festival Traffic Management

Recommended Action:
• Deploy Crowd Management Teams
• Increase Barricades
• Enable Temporary Parking Zones
• Extend Signal Timings

Expected Crowd Load: Very High
""")

    # Signal Failure
    elif "signal" in q:

        st.success("""
🚦 Traffic Signal Failure

Recommended Action:
• Deploy Traffic Officers Immediately
• Notify Signal Maintenance Team
• Activate Manual Traffic Control

Expected Clearance Time: 15 Minutes
""")

    # Illegal Parking
    elif "parking" in q:

        st.success("""
🅿 Illegal Parking Hotspot

Recommended Action:
• Dispatch Enforcement Team
• Issue E-Challans
• Deploy Tow Trucks
• Increase CCTV Monitoring

Expected Congestion Reduction: 25%
""")

    # Event
    elif "event" in q or "concert" in q or "match" in q:

        st.success("""
🏟 Major Event Detected

Recommended Action:
• Deploy Traffic Officers
• Create Diversion Routes
• Reserve Emergency Corridor
• Increase Public Transport Frequency

Expected Traffic Increase: 150-300%
""")

    else:

        st.info("""
🤖 General Recommendation

• Monitor Incident Closely
• Assess Severity Level
• Deploy Officers Based on Risk
• Activate Diversions if Congestion Increases
• Continuously Monitor Urban Disruption Score (UDS)

Recommended Monitoring Interval: 15 Minutes
""")