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
(1, 'Ameise', 'braun/schwarz/rot', 'Weltweit', 'Wald/Erde/Gaerten/Staedte', 'Insekten/Pflanzen/Lebensmittel', 'Abholzung', 'pexels-egor-kamelev-1104974.jpg'),
(2, 'Bettwanze', 'Rot-Schwarz', 'Weltweit', 'Tropen', 'Blut', NULL, 'pexels-pixabay-35804.jpg',
(3, 'Eintagsfliege', 'braun/grau', 'Europa', 'Wassernähe', 'Algen', 'durch die Industrie verunreinigte Gewässer', 'pexels-petr-ganaj-4121192.jpg'),
(4, 'Kakerlake', 'braun', 'Tropen/Subtropen', 'Waelder/Wiesen', 'Allesfresser', NULL, 'erik-karits-iZR2SI7tcQw-unsplash(2).jpg'),
(5, 'Schnecke', 'grau/braun/schwarz', 'Weltweit', 'Boden/Wiesen/Parks', 'Pflanzen', "Mensch: Flächenbebauung", 'marian-beck-xlcj7KLs2FQ-unsplash.jpg'),
(6, 'Zecke', 'Schwarz', 'Weltweit', 'Graeser/Buesche/Unterholz', 'Blut', NULL, 'rotes-schabe-makro-isoliert-auf-weiß-seitenansicht-eines-lebenden-erwachsenen-roten-makros-weißem-hintergrund-eine-schwangere-161177088.jpg'),
(7, 'Honigbiene', 'Schwarz/Gelb', 'Weltweit', 'Wiese/Wald', 'Nektar/Pollen', 'Pestizide/Überdüngung/Flächenbebauung', 'pexels-pixabay-460961.jpg'),
(8, 'Wandelndes Blatt', 'Gruen', 'Weltweit', 'Tropen/Subtropen', 'Blaetter/Pflanzen/Fruechte', NULL, 'istockphoto-120251734-170667a.jpg'),
(9, 'Marienkaefer', 'Rot/Schwarz', 'Weltweit', 'Gaerten/Heiden/Waelder', 'Blattläuse', NULL, 'pexels-michael-willinger-3482947.jpg'),
(10, 'Wespe', 'Gelb/Schwarz', 'Weltweit', 'Waelder/Wiesen', 'Nektar', 'Pestizide/Überdüngung', 'pexels-david-hablützel-928968.jpg');''')
con.commit()
con.close()