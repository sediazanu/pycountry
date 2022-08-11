##To help me with this project, I used a website called pythoncentral.io which gave me some information on how to use SQLite in python
##The link to the section of the website I used is https://www.pythoncentral.io/introduction-to-sqlite-in-python/

import sqlite3
import sys ##allows for system specific parameters and functions to be used

db = sqlite3.connect('database/mydb') ##creates or opens a file called mydb with a SQLite3 DB

def get_posts():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Package")##selects everything from the package
    print(cursor.fetchall())##prints everything that was selected including ids


def newtable():
    askinput = (input("Do you want to create/update the package table? (yes or no)")).lower()

    if askinput == "yes":
        print("yes")
        cursor = db.cursor() ##cursor is an object that allows for the statement to be executed
        cursor.execute("""CREATE TABLE if not exists Package(PackageID integer, City text,
                              Package text,
                              Hotel text,
                              primary key(PackageID))""")
        db.commit() ##updates the record in the database
        City1 = input("Enter the name of the city")
        Package1 = input("Enter the name of the type of package being offered")
        Hotel1 = input("Enter the name of the hotel")
        cursor.execute("""INSERT INTO Package(City, Package, Hotel) Values(?,?,?)""", (City1, Package1, Hotel1))
        db.commit()
    elif askinput == "no":
        print("no")
        sys.exit()
    else:
        print("Please enter yes or no")
        newtable()
get_posts()
newtable()


