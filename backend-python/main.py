from flask import Flask, jsonify, request
from flask_cors import CORS , cross_origin
import sqlite3
dbname = "Tuugii.db"
app = Flask(__name__)

@app.route('/api/posts')
@cross_origin()
def getPosts():
    conn = sqlite3.connect(dbname)
    data = conn.execute("SELECT * FROM posts").fetchall()
    conn.commit()
    print(data)
    return data

@app.route("/api/upload", methods=['POST'])
@cross_origin()
def upload():
    data = request.json
    data1 = data.get('data1')
    data2 = data.get('data2')
    conn = sqlite3.connect(dbname)
    conn.execute("INSERT INTO posts (title, body) VALUES (?,?)",(data1,data2))
    conn.commit()
    return 'succesfully added'

@app.route('/api/delete/<id>',methods=['DELETE'])
@cross_origin()
def removePost(id):
    pID = id
    conn = sqlite3.connect(dbname)
    print(id)
    conn.execute("DELETE FROM posts WHERE id = ?", (pID))
    conn.commit()
    return 'succesfully deleted'

@app.route('/api/post/<id>',methods=['GET'])
@cross_origin()
def getPostinfo(id):
    pID = id
    conn = sqlite3.connect(dbname)
    data = conn.execute("SELECT * FROM posts WHERE id = ?", (pID)).fetchall()
    conn.commit()
    print(data)
    return data

@app.route('/api/update/<int:id>', methods=['PATCH'])
@cross_origin()
def updatePost(id):
    pID = id
    data = request.json
    data1 = data.get('title')
    data2 = data.get('body')
    print('name is ',data1 , data2)
    conn = sqlite3.connect(dbname)
    conn.execute("UPDATE posts SET title = ?, body = ? WHERE id = ?", (data1, data2, pID))
    conn.commit()
    return 'updatede'
    
if __name__ == '__main__':
    app.run(debug=True)