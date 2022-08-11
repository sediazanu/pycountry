
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

def finddistance():
    cursor.execute("""SELECT City, Latitude, Longitude FROM Location """)
    matrixlist = list(cursor.fetchall())
    print(matrixlist)


finddistance()

def dist(coor1, coor2): ##This function I found in javascript and modififed it to allow it to work in python
        R= 6373.0
        m = [coor1[0] - coor2[0], coor1[1] - coor2[1]] ##This finds out the x distance and the y distance between the two points
        c = sin(m[0]/2)**2 + cos(coor1[0])*cos(coor2[0])* sin(m[1]/2)**2 ##This is the haversine formula that is used to find the great-circle distance between two points on
        p = 2* atan2(sqrt(c), sqrt(1-c))                                 ##a sphere given their longitudes and latititudes.
        distance = p*radius
        return distance


Matrix = {} ##This creates the dictionary for the matrix
'''for items in cords.items():
        print(str(items))'''


for city1, cords1 in cords.items(): ##This finds any of the data values in the dictionary and iterates until all data values have been found
        Matrix[city1] = {} ##This creates the heading for the first city in the dictionary
##        print(city1, cords1)
        for (city2, cords2) in cords.items(): ##This finds the second city to compare to the first city to.
            Matrix[city1][city2] = dist(cords1, cords2) ##This stores the distance between the two cities after the funciton is completed
