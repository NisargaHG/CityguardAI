import streamlit as st
import pandas as pd
from utils.uds import calculate_uds

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)


# Load Dataset
df = pd.read_csv("data/events.csv")

# Metrics
total_incidents = len(df)

planned_events = len(df[df["event_type"] == "planned"])

unplanned_events = len(df[df["event_type"] == "unplanned"])

active_incidents = len(df[df["status"] == "active"])

# Title
st.title("CITYGUARD AI")
st.subheader("Intelligent Urban Disruption Management System")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Incidents", total_incidents)

col2.metric("Planned Events", planned_events)

col3.metric("Unplanned Events", unplanned_events)

col4.metric("Active Incidents", active_incidents)

st.divider()


df["UDS"] = df.apply(
    lambda row: calculate_uds(
        row["priority"],
        row["requires_road_closure"],
        row["event_type"]
    ),
    axis=1
)

st.write("### Top Incident Types")

event_counts = df["event_cause"].value_counts()

st.bar_chart(event_counts)

st.write("### Top Risk Zones")

zone_counts = df["zone"].fillna("Unknown").value_counts()

st.bar_chart(zone_counts.head(10))

st.write("### Urban Disruption Score Statistics")

col1,col2,col3 = st.columns(3)

col1.metric(
    "Average UDS",
    round(df["UDS"].mean(),2)
)

col2.metric(
    "Maximum UDS",
    int(df["UDS"].max())
)

col3.metric(
    "Critical Incidents",
    len(df[df["UDS"] >= 90])
)

st.write("### Zone Vulnerability Ranking")

zone_risk = (
    df.groupby("zone")["UDS"]
    .mean()
    .sort_values(ascending=False)
)

st.dataframe(zone_risk.head(10))