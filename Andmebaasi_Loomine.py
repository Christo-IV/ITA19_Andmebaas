import sqlite3

ühendus = sqlite3.connect("andmebaas.db")
c = ühendus.cursor()

c.execute("CREATE TABLE õppijad (eesnimi text, perenimi text)")

c.execute("INSERT INTO õppijad VALUES ('Andres', 'Kivi')")
c.execute("INSERT INTO õppijad VALUES ('Priit', 'Murakas')")
c.execute("INSERT INTO õppijad VALUES ('Indrek', 'Kivi')")
c.execute("INSERT INTO õppijad VALUES ('Siim', 'Kivi')")

ühendus.commit()

ühendus.close()