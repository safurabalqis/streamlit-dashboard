import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/complex_sales_data.csv")

st.title("🌍 Regional Insights")

region = st.selectbox("Select Region", df["Region"].unique())

filtered = df[df["Region"] == region]
st.write(f"Total Revenue in {region}: ${filtered['Total'].sum():,.2f}")

fig = px.bar(filtered, x="Product", y="Total", color="Product", title=f"Sales by Product in {region}")
st.plotly_chart(fig)
