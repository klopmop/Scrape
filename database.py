import sqlite3
from joke_api import get_random_joke

DB_FILE = "funny.db"


def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS jokes(Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Joke_text TEXT, Data DATE DEFAULT (CURRENT_DATE))
        """)
        conn.commit()

def save_to_db(jokes):
    with sqlite3.connect(DB_FILE, timeout=5) as conn:
        c  = conn.cursor()
        c.execute("INSERT INTO jokes (Joke_text) VALUES (?)",(jokes,))
        conn.commit()

joke1 = get_random_joke()
save_to_db(joke1)