import os
import sqlite3

DATABASE_PATH = os.environ.get("DATABASE_PATH", "energy_watch.db")  

CREATE_COMPONENTS_TABLE = """
CREATE TABLE IF NOT EXISTS components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    type TEXT NOT NULL,
    last_updated TEXT NOT NULL
);
"""

def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_connection()
    try:    
        connection.execute(CREATE_COMPONENTS_TABLE)
        connection.commit()
    finally:
        connection.close()