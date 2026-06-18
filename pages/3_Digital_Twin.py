import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Digital Twin Simulator",
    layout="wide"
)

st.title("🚦 Cityguard AI - Digital Twin Simulator")

# Load Dataset
df = pd.read_csv("data/events.csv")

# Sidebar
st.sidebar.header("Simulation Inputs")

event_type = st.sidebar.selectbox(
    "Event Type",
    sorted(
        df["event_type"]
        .dropna()
        .unique()
    )
)

incident = st.sidebar.selectbox(
    "Incident Type",
    sorted(df["event_cause"].dropna().unique())
)

priority = st.sidebar.selectbox(
    "Priority",
    ["Low", "Medium", "High"]
)

road_closure = st.sidebar.selectbox(
    "Road Closure Required",
    ["No", "Yes"]
)

if event_type == "planned":

    st.success(
        "📅 Planned Event Scenario"
    )

else:

    st.warning(
        "⚡ Unplanned Event Scenario"
    )
# ------------------------------------
# REAL UDS CALCULATION
# ------------------------------------

base_risk = 20

event_type_count = len(
    df[
        df["event_type"] == event_type
    ]
)

max_event_type = (
    df["event_type"]
    .value_counts()
    .max()
)

event_type_score = (
    event_type_count /
    max_event_type
) * 20

base_risk += event_type_score

# Priority Score
if priority == "Medium":
    base_risk += 20

elif priority == "High":
    base_risk += 40

# Road Closure Score
if road_closure == "Yes":
    base_risk += 25

# Historical Incident Frequency
incident_count = len(
    df[df["event_cause"] == incident]
)

max_count = df["event_cause"].value_counts().max()

frequency_score = (
    incident_count / max_count
) * 35

base_risk += frequency_score

base_risk = min(round(base_risk), 100)

# ------------------------------------
# CURRENT STATE
# ------------------------------------

st.subheader("Current Situation")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Incident Type",
    incident
)

col2.metric(
    "Historical Incidents",
    incident_count
)

col3.metric(
    "Urban Disruption Score",
    base_risk
)

col4.metric(
    "Event Type",
    event_type
)

# ------------------------------------
# INTERVENTIONS
# ------------------------------------

st.subheader("Apply Interventions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    officers = st.checkbox(
        "Deploy Officers"
    )

with col2:
    towtruck = st.checkbox(
        "Tow Truck"
    )

with col3:
    diversion = st.checkbox(
        "Diversion Route"
    )

with col4:
    barricades = st.checkbox(
        "Barricades"
    )

# ------------------------------------
# SIMULATION ENGINE
# ------------------------------------

new_risk = base_risk

if officers:
    new_risk -= 15

if towtruck:
    new_risk -= 20

if diversion:
    new_risk -= 15

if barricades:
    new_risk -= 10

new_risk = max(new_risk, 0)

# ------------------------------------
# RESULTS
# ------------------------------------

st.subheader("Simulation Result")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Current Risk",
        base_risk
    )

with col2:

    st.metric(
        "Risk After Intervention",
        new_risk,
        delta=base_risk-new_risk
    )

# ------------------------------------
# RISK STATUS
# ------------------------------------

if new_risk >= 75:

    st.error(
        "🔴 Critical Risk"
    )

elif new_risk >= 50:

    st.warning(
        "🟠 High Risk"
    )

elif new_risk >= 25:

    st.info(
        "🟡 Moderate Risk"
    )

else:

    st.success(
        "🟢 Low Risk"
    )

# ------------------------------------
# COMPARISON CHART
# ------------------------------------

fig = go.Figure()

fig.add_bar(
    x=["Before"],
    y=[base_risk],
    name="Current Risk"
)

fig.add_bar(
    x=["After"],
    y=[new_risk],
    name="Post Intervention"
)

fig.update_layout(
    title="Risk Reduction Analysis",
    yaxis_title="Urban Disruption Score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ------------------------------------
# AI INSIGHT
# ------------------------------------

st.subheader("🤖 AI Insight")

reduction = base_risk - new_risk

if reduction > 40:

    st.success(
        f"""
        Excellent response plan.

        Risk reduced by {reduction} points.

        Recommended deployment is sufficient
        to avoid severe congestion.
        """
    )

elif reduction > 20:

    st.info(
        f"""
        Moderate improvement.

        Risk reduced by {reduction} points.

        Consider additional officers or
        diversion routes.
        """
    )

else:

    st.warning(
        f"""
        Only {reduction} points reduction.

        Current intervention may not be enough.

        Additional resources are recommended.
        """
    )