import streamlit as st
import pandas as pd
import folium
import time

from streamlit_folium import st_folium

st.title("CityGuard AI Risk Heatmap")

loading_text = st.empty()

loading_text.info(
    " Loading Geospatial Traffic Layer..."
)

time.sleep(2)

df = pd.read_csv("data/events.csv")

loading_text.empty()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Incidents",
        len(df)
    )

with col2:
    st.metric(
        "High Risk Incidents",
        len(
            df[
                df["priority"]
                .astype(str)
                .str.lower() == "high"
            ]
        )
    )

with col3:
    st.metric(
        "Zones Covered",
        df["zone"].nunique()
    )

m = folium.Map(
    location=[12.97, 77.59],
    zoom_start=11
)

for _, row in df.iterrows():

    color = "green"

    priority = str(row["priority"]).lower()

    if priority == "high":
        color = "red"

    elif priority == "medium":
        color = "orange"

    popup_text = f"""
    Event Cause: {row['event_cause']}
    
    Priority: {row['priority']}
    
    Status: {row['status']}
    
    Zone: {row['zone']}
    """

    folium.CircleMarker(
        location=[
            row["latitude"],
            row["longitude"]
        ],
        radius=5,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=popup_text
    ).add_to(m)

st.markdown("""
### Risk Levels

🔴 High Risk
🟠 Medium Risk
🟢 Low Risk
""")

st_folium(
    m,
    width=1200,
    height=700
)