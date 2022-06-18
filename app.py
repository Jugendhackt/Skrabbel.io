import json
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def rpe():
    con = sqlite3.connect("example.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Insects(InsectID, InsectName, Farbe, Verbreitung, Lebensraum, Nahrung)")
    cur.execute("INSERT INTO Insects VALUES(2, 'Bettwanze','Rot-Schwarz', 'Weltweit', 'Tropen', 'Blut')")
    con.commit()
    result= cur.execute('SELECT * FROM Insects')
    return jsonify(json.dumps(cur.fetchall()))

  
# main driver function
if __name__ == '__main__':
    app.run()
    
con.close()