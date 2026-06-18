import streamlit as st

st.title("🔄 Post Event Learning Engine")

predicted = st.selectbox(
    "Predicted Outcome",
    ["Low","Medium","High"]
)

actual = st.selectbox(
    "Actual Outcome",
    ["Low","Medium","High"]
)

if st.button("Archive Incident"):

    if predicted == actual:

        st.success(
            "Prediction Correct. Model confidence increased."
        )

    else:

        st.warning(
            "Prediction Mismatch. Added to retraining dataset."
        )

    st.info("""
This incident will be used
for future model retraining.
""")