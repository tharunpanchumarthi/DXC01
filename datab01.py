import sqlite3
con = sqlite3.connect('DetailsStud02.db')
cur = con.cursor()
cur.execute(""" CREATE TABLE DetailsStud02 (RollNo int, StudName VARCHAR(30), MathMarks int, PhyMarks int, CheMarks int);""")
con.commit()
con.close()
