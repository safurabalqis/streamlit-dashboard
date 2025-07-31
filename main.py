import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Dashboard Home", layout="wide")
st.title("📊 Dashboard from API")

# Call FastAPI backend
response = requests.get("http://127.0.0.1:8000/sales")

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df.head())
else:
    st.error("Failed to fetch data from the API")
