import sqlite3

def get_db_connection():
    conn = sqlite3.connect("sales_data.db")
    conn.row_factory = sqlite3.Row  # for dict-like row access
    return conn
