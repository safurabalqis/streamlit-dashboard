import sqlite3
import pandas as pd

# Load your CSV
df = pd.read_csv("data/complex_sales_data.csv")

# Connect to (or create) database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    OrderID TEXT,
    OrderDate TEXT,
    CustomerName TEXT,
    Product TEXT,
    Region TEXT,
    Quantity INTEGER,
    UnitPrice REAL,
    Total REAL
)
""")

# Insert data
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("✅ Database created and data inserted!")
