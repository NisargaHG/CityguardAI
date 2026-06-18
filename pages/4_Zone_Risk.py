import streamlit as st
import pandas as pd

st.title("📍 Zone Intelligence")

df = pd.read_csv("data/events.csv")

zone_stats = (
    df.groupby("zone")
      .size()
      .reset_index(name="Incidents")
      .sort_values(
          "Incidents",
          ascending=False
      )
)

st.dataframe(zone_stats)

st.bar_chart(
    zone_stats.set_index("zone")
)