import streamlit as st

# Configure Streamlit app
st.set_page_config(page_title="Leuser Ecosystem Dashboard", layout="wide")

# Define pages
pg = st.navigation([
    st.Page("pages/forest_loss_predictions.py", title="Forest Loss Predictions"),
    st.Page("pages/data_explanation.py", title="Data Explanation")
])

# Run the selected page
pg.run()