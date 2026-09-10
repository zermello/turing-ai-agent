import sqlite3
import os

os.makedirs("data", exist_ok=True)

connection = sqlite3.connect("data/memory.db")
cursor = connection.cursor()

x=cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

connection.commit()