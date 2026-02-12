import sqlite3

def login(user, pwd):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
    return conn.execute(query).fetchone()
