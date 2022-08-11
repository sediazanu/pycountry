
import sqlite3
db = sqlite3.connect('database/mydb') ##creates or opens a file called mydb with a SQLite3 DB
cursor = db.cursor()
from math import sin, cos, sqrt, atan2, radians

def add_latandlong():
    for package in cursor.execute("SELECT * FROM Location"): ##selects everything from the package
        print(package) ##prints everything that was selected including ids
    city = input("Enter the name of the city")
    Latitude = input("Enter Latitude of the city")
    Latitude = radians(float(Latitude))
    Longitude = input("Enter the Longitude of the city")
    Longitude = radians(float(Longitude))
    cursor.execute("""INSERT INTO Location(City, Latitude, Longitude) Values(?,?,?)""", (city, Latitude, Longitude))
    db.commit()




add_latandlong()