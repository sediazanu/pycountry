##To help me with this project, I used a website called pythoncentral.io which gave me some information on how to use SQLite in python
##The link to the section of the website I used is https://www.pythoncentral.io/introduction-to-sqlite-in-python/
import sqlite3
db = sqlite3.connect('database/mydb') ##creates or opens a file called mydb with a SQLite3 DB
cursor = db.cursor()

def new_table():
    askinput = (input("Do you want to create/update the package table? (yes or no)")).lower()

    if askinput == "yes":
        print("yes")
        cursor.execute("""CREATE TABLE if not exists Package(PackageID integer, City text,
                              Package text,
                              Hotel text,
                              primary key(PackageID))""")
        db.commit() ##updates the record in the database
    elif askinput == "no":
        print("no")
        sys.exit()
    else:
        print("Please enter yes or no")
        newtable()

# Update - moved add city into it's own function
def add_city():
    city = input("Enter the name of the city")
    package = input("Enter the name of the type of package being offered")
    hotel = input("Enter the name of the hotel")
    cursor.execute("""INSERT INTO Package(City, Package, Hotel) Values(?,?,?)""", (city, package, hotel))
    db.commit()

def edit_table():
    editinput = input("Which record in the table would you like to edit")
    city = input("What would you like the new city to be named?")
    package = input("What would you want the new package to be named?")
    hotel = input("What would you want the new hotel to be named?")
    cursor.execute("""UPDATE Package SET City = ?, Package=?, Hotel=? WHERE PackageID = ?""", (city, package, hotel, editinput))
    db.commit()

### Queries ###
def get_all():
    for package in cursor.execute("SELECT * FROM Package"): ##selects everything from the package
        print(package) ##prints everything that was selected including ids


