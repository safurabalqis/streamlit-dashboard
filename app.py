import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Simple Sales Dashboard")

file = st.file_uploader("Upload a CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.write("Preview of Data:", df.head())

    if "Date" in df.columns and "Sales" in df.columns:
        fig = px.line(df, x="Date", y="Sales", title="Sales Over Time")
        st.plotly_chart(fig)
    else:
        st.warning("CSV must contain 'Date' and 'Sales' columns.")
