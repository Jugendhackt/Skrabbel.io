import time
zeitanfang = time.perf_counter()
spieler = input()
insect = "test"
eingabe = ""
dauer = 30
insect = insect.lower()
while not eingabe == insect:
    eingabe = input()
    eingabe = eingabe.lower()
    print(spieler + ": " + eingabe)
  #  if  zeitanfang > dauer:
        #Fakt anzeigen
       # print("test erfogreich")
      #  dauer = dauer * 2
zeitende = time.perf_counter()
print("Das Insekt wurde in " + str(round(zeitende - zeitanfang, 0)) + " Sekunden erraten.")
    #Bild und Fakten anzeigen