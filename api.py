from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd

app = FastAPI()

# Enable CORS (important for Streamlit to call FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route to get all sales data
@app.get("/sales")
def get_sales_data():
    conn = sqlite3.connect("sales_data.db")
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df.to_dict(orient="records")
