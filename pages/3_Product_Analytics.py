import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/complex_sales_data.csv")

st.title("📦 Product Analytics")

product = st.selectbox("Select Product", df["Product"].unique())
product_data = df[df["Product"] == product]

st.write(f"Total Revenue for {product}: ${product_data['Total'].sum():,.2f}")

fig = px.line(product_data, x="Date", y="Total", title=f"{product} Sales Over Time")
st.plotly_chart(fig)

st.dataframe(product_data.head())
