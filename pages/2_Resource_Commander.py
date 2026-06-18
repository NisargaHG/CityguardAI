import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Resource Commander", layout="wide")

st.title("🚔 AI Resource Commander")
st.subheader("Intelligent Resource Deployment Recommendation")

# Load dataset
df = pd.read_csv("data/events.csv")

# Get all event causes
event_list = sorted(df["event_cause"].dropna().unique())

# Inputs
col1, col2, col3 = st.columns(3)

with col1:
    event = st.selectbox(
        "Incident Type",
        event_list
    )

with col2:
    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High"]
    )

with col3:
    road_closure = st.selectbox(
        "Road Closure Required",
        ["No", "Yes"]
    )

# Base Resource Rules
RESOURCE_RULES = {

    "vehicle_breakdown": {
        "Officers": 2,
        "Tow Trucks": 1,
        "Barricades": 0,
        "Ambulances": 0
    },

    "water_logging": {
        "Officers": 4,
        "Tow Trucks": 0,
        "Barricades": 3,
        "Drainage Teams": 1
    },

    "tree_fall": {
        "Officers": 3,
        "Tow Trucks": 1,
        "Barricades": 2,
        "Forest Team": 1
    },

    "pot_holes": {
        "Officers": 2,
        "Road Maintenance Team": 1,
        "Barricades": 2
    },

    "accident": {
        "Officers": 5,
        "Tow Trucks": 1,
        "Ambulances": 1,
        "Barricades": 3
    },

    "construction": {
        "Officers": 4,
        "Barricades": 5,
        "Monitoring Cameras": 2
    }
}

# Default Rule
default_resources = {
    "Officers": 2,
    "Barricades": 1
}

# Fetch Resources
resources = RESOURCE_RULES.get(event, default_resources)

# Copy dictionary
resources = dict(resources)

# Priority adjustment
if priority == "Medium":

    for key in resources:

        if isinstance(resources[key], int):
            resources[key] += 1

elif priority == "High":

    for key in resources:

        if isinstance(resources[key], int):
            resources[key] += 2

# Road closure adjustment
if road_closure == "Yes":

    resources["Barricades"] = resources.get(
        "Barricades",
        0
    ) + 3

    resources["Traffic Diversion Team"] = 1

# Display
st.divider()

st.subheader("📋 Recommended Deployment")

for resource, value in resources.items():

    st.metric(resource, value)

# Risk Level
st.divider()

risk_score = 20

if priority == "Medium":
    risk_score += 20

if priority == "High":
    risk_score += 40

if road_closure == "Yes":
    risk_score += 20

if risk_score >= 70:
    st.error("🔴 CRITICAL RISK")

elif risk_score >= 40:
    st.warning("🟠 MODERATE RISK")

else:
    st.success("🟢 LOW RISK")

# Explanation
st.divider()

st.subheader("🤖 AI Recommendation")

recommendation = f"""
Incident Type: {event}

Priority: {priority}

Road Closure: {road_closure}

Recommended Action:
"""

if priority == "High":

    recommendation += """
• Deploy resources immediately.
• Activate diversion routes.
• Monitor traffic every 5 minutes.
"""

elif priority == "Medium":

    recommendation += """
• Deploy field officers.
• Monitor congestion buildup.
"""

else:

    recommendation += """
• Routine monitoring is sufficient.
"""

st.info(recommendation)