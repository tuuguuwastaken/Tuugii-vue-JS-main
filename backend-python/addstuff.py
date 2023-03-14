import json
import sqlite3

conn = sqlite3.connect('D:\Github\Tuugii-vue-JS-main\Tuugii.db')

with open("json.json",'r') as f:
    data = json.load(f)
    
    
for i in data:
    conn.execute("INSERT INTO posts (title , body) VALUES ( ?, ? )", (i['title'],i['body']))
    conn.commit()

conn.close()