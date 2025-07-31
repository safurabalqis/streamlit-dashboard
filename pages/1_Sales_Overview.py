import streamlit as st
import pandas as pd

df = pd.read_csv("data/complex_sales_data.csv")

st.title("📈 Sales Overview")
st.write("Summary of all sales transactions.")

st.metric("Total Orders", df['OrderID'].nunique())
st.metric("Total Revenue", f"${df['Total'].sum():,.2f}")
st.metric("Total Units Sold", int(df['Quantity'].sum()))

st.subheader("Sales by Date")
st.line_chart(df.groupby("Date")["Total"].sum())
