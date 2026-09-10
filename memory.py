import sqlite3

connection = sqlite3.connect("data/memory.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIME
    )
""")

def save_memory(content):
    cursor.execute("""
        INSERT INTO memories (content)
        VALUES (?)
    """, (content, )
    )

    connection.commit()

def get_memory():
    cursor.execute("""
    SELECT *
    FROM memories
    """)

    return cursor.fetchall()
