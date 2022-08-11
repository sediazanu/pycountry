import sqlite3
import sys ##allows for system specific parameters and functions to be used

db = sqlite3.connect('database/mydb') ##creates or opens a file called mydb with a SQLite3 DB

def get_posts():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Package")##selects everything from the package
    print(cursor.fetchall())##prints everything that was selected including ids

def edittable():
    cursor = db.cursor()
    editinput = input("Which record in the table would you like to edit")
    City2 = input("What would you like the new city to be named?")
    Package2 = input("What would you want the new package to be named?")
    Hotel2 = input("What would you want the new hotel to be named?")
    cursor.execute("""UPDATE Package SET City = ?, Package=?, Hotel=? WHERE PackageID = ?""", (City2, Package2, Hotel2, editinput))
    db.commit()


get_posts()
edittable()
get_posts()



