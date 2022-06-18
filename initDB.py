#!/usr/bin/env python3

import sqlite3
con = sqlite3.connect("example.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Insects
(
    InsectID INTEGER NOT NULL, 
    InsectName VARCHAR(20),
    Lebensraum VARCHAR(30),
    Farbe VARCHAR(10),
    Nahrung VARCHAR(15),
    Verbreitung VARCHAR(20),
    Bedrohung VARCHAR(20),
    Bild VARCHAR(50)
);''')
cur.execute('''INSERT INTO Insects (InsectID, InsectName, Farbe, Verbreitung, Lebensraum, Nahrung, Bedrohung, Bild) VALUES
(1, 'Ameise', 'braun/schwarz/rot', 'Weltweit', 'Wald/Erde/Gaerten/Staedte', 'Insekten/Pflanzen/Lebensmittel', 'Abholzung', NULL),
(2, 'Bettwanze', 'Rot-Schwarz', 'Weltweit', 'Tropen', 'Blut', NULL, NULL),
(3, 'Eintagsfliege', 'braun/grau', 'Europa', 'Wassernähe', 'Algen', 'durch die Industrie verunreinigte Gewässer', NULL),
(4, 'Kakerlake', 'braun', 'Tropen/Subtropen', 'Waelder/Wiesen', 'Allesfresser', NULL, NULL),
(5, 'Schnecke', 'grau/braun/schwarz', 'Weltweit', 'Boden/Wiesen/Parks', 'Pflanzen', NULL, NULL),
(6, 'Zecke', 'Schwarz', 'Weltweit', 'Graeser/Buesche/Unterholz', 'Blut', NULL, NULL),
(7, 'Honigbiene', 'Schwarz/Gelb', 'Weltweit', 'Wiese/Wald', 'Nektar/Pollen', NULL, NULL),
(8, 'Wandelndes Blatt', 'Gruen', 'Weltweit', 'Tropen/Subtropen', 'Blaetter/Pflanzen/Fruechte', NULL, NULL),
(9, 'Marienkaefer', 'Rot/Schwarz', 'Weltweit', 'Gaerten/Heiden/Waelder', 'Blattläuse', NULL, NULL),
(10, 'Wespe', 'Gelb/Schwarz', 'Weltweit', 'Waelder/Wiesen', 'Nektar', 'Pestizide', NULL);''')
con.commit()
con.close()