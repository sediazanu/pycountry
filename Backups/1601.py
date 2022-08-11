##To help me with this project, I used a website called pythoncentral.io which gave me some information on how to use SQLite in python
##The link to the section of the website I used is https://www.pythoncentral.io/introduction-to-sqlite-in-python/

import sqlite3
import sys ##allows for system specific parameters and functions to be used

db = sqlite3.connect('database/mydb') ##creates or opens a file called mydb with a SQLite3 DB


def newtable():
 askinput = (input("Do you want to create a new table? (yes or no)")).lower


 while askinput !="yes" or askinput !="no":
    askinput = input("Only use yes or no please").lower
 if askinput == "yes":




  cursor = db.cursor() ##cursor is an object that allows for the statement to be executed
  cursor.execute("""CREATE TABLE IF NOT exists Package(PackageID integer, City text,
                          Package text,
                          Hotel text,
                          primary key(PackageID))""")
  db.commit() ##updates the record in the database
  cursor = db.cursor()
  cursor.execute("""CREATE TABLE IF NOT exists CITY1(CITY1 text, CITY2 text, CITY3 text, CITY4 text, CITY5 text, primary key(CITY1))""")
  db.commit()
 elif askinput.lower() == "no":
    sys.exit()

newtable()



