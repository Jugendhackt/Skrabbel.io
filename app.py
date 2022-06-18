import json
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def rpe():
    con = sqlite3.connect("example.db")
    cur = con.cursor()
    result= cur.execute('SELECT * FROM Insects').fetchall()
    con.close()
    return jsonify(result)


  
# main driver function
if __name__ == '__main__':
    app.run()
    
