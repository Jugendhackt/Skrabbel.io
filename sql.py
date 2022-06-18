import sqlite3
con = sqlite3.connect("example.db")
cur = con.cursor()
cur.execute("CREATE TABLE Insects(InsectID, InsectName, Farbe, Verbreitung, Lebensraum, Nahrung)")
cur.execute("INSERT INTO Insects VALUES(2, 'Bettwanze','Rot-Schwarz', 'Weltweit', 'Tropen', 'Blut')")
con.commit()

for row in cur.execute('SELECT * FROM Insects'):
    print(row)



con.close()