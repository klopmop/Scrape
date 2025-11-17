import sqlite3

def init_db():
    conn = sqlite3.connect("rand_jokes.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS jokes(Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Joke_text TEXT, Data DATE DEFAULT (CURRENT_DATE))
    """)
    conn.commit()
    conn.close()

def save_to_db(joke):
    conn = sqlite3.connect("rand_jokes.db", timeout=5)
    c  = conn.cursor()
    c.execute("INSERT INTO jokes (Joke_text) VALUES (?)",(joke,))
    conn.commit()
    conn.close()