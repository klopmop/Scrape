import sqlite3
import pathlib
from joke_api import get_random_joke


def does_it_exists():
    file = pathlib.Path("funny.db")
    if not file.exists():
        init_db()
    else:
        save_to_db(joke)


def init_db():
    conn = sqlite3.connect("funny.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS jokes(Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Joke_text TEXT, Data DATE DEFAULT (CURRENT_DATE))
    """)
    conn.commit()
    conn.close()

def save_to_db(joke):
    conn = sqlite3.connect("funny.db", timeout=5)
    c  = conn.cursor()
    c.execute("INSERT INTO jokes (Joke_text) VALUES (?)",(joke,))
    conn.commit()
    conn.close()

joke = get_random_joke()
does_it_exists()