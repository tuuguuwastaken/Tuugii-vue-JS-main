import sqlite3

conn = sqlite3.connect("D:\Github\Tuugii-vue-JS-main\Tuugii.db")

conn.execute("""
            CREATE TABLE posts (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                body TEXT NOT NULL)""")

conn.commit()
conn.close()