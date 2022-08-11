import sys
import sqlite3
from math import sin, cos, sqrt, atan2, radians

from functions import *

db = sqlite3.connect('database/mydb') ##creates or opens a file called mydb with a SQLite3 DB
cursor = db.cursor()
##cursor.execute("SELECT * FROM Package")##selects everything from the package
##print(cursor.fetchall()) ##prints everything that was selected including ids


def get_package(Matrix):
    package1 = input("Input the package type you want: ")
    print(package1) ##This prints out the package inputted so it is easier for the user to remember which package they input
    cursor.execute("""SELECT City FROM Package WHERE Package=?""",(package1,)) ##this takes the values where the cities match the package input
    packagelist = list(cursor.fetchall()) ##This stores the obtained cities into a list so that it is converted from sql into python
    print(packagelist)
    print(len(packagelist)) ##This prints out how long the list is
    array = [] ##this creates a new array
    for each in range(len(packagelist)):
        array.append(packagelist[each][0])##This inserts each of the cities into an array as the list is actually 2d, meaning that it cant only be used to take values
    print(array)
    n = input("Which city would you like to start from?: ").title() ##This is used to select the city that the user wants to compare to the rest in the database
    x = array.index(n) ##This stores the location of that city in the array
    array[x]=array[(len(packagelist)-1)] ##This changes the inputted city with the last city in the array
    array[(len(packagelist)-1)] = n ##This puts the city inputted in the last position in the array
    y=0
    base= []##This new array is created to store the cities and their location from the inputted city
    for each in range(len(packagelist)-1):
        base.append([]) ##This creates a new section in the array.
        base[y].append(array[y]) ##This adds the city and inputs it inside the first
        base[y].append(Matrix[array[len(packagelist)-1]][array[each]])
        print(base)
        y = y+1

    base = sorted(base, key=lambda x: x[1])##This sorts the array and changes the order to ascending order.
    print(base)
    z=0
    for each in range(len(packagelist)-1):
        print(base[z][0],"is",base[z][1],"from",n)
        z=z+1

def matrix():
    ##approx radius of earth in km
    radius = 6373.0
    cords = {} ##This creats the dictonary to store the values
    cords['Paris'] = (radians(48.864716), radians(2.349014))
    cords['London'] = (radians(51.509865), radians(-0.118092))
    cords['New York'] = (radians(40.730610), radians(-73.935242))
    cords["Malaga"] = (radians(36.721274), radians(-4.421399))
    cords["Brussels"] = (radians(50.8504500), radians(4.3487800))
    cords["Toronto"] = (radians(43.761539),radians(-79.411079))
    cords["Berlin"] = (radians(52.520008), radians(13.404954))
    cords["Sydney"] = (radians(-33.865143), radians(151.209900))
    cords["Dubai"] = (radians(25.276987), radians(55.296249))
    cords["Orlando"] = (radians(28.538336), radians(-81.379234))

    def dist(coor1, coor2): ##This function I found in javascript and modififed it to allow it to work in python
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



    '''for city1, x in Matrix.items(): ##This finds each of the fields and all of the column values that follow them. x is the value of the second dictionary
                                     ##This is repeated until all the cities in the table have been found
        for city2, d in x.items(): ##This finds in the second dictionary the city and the value attached to that city, which was found with the dist() function
            print (city1, city2, d) ##This finds all of the values found and prints them.#'''
    return Matrix

def display_menu():
    print()
    print("############################")
    print("Welcome to Sedinams Holdays!")
    print("############################")
    print()
    print("Main Menu - choose one of the following options:")
    print()
    print("1. Show all starting cities.")
    print("2. Choose a holiday package.")
    print("3. Add a new city to the database")
    print("4. Update a currently existing record.")
    print("0. Exit.")
    print()
    menu_choice = int(input("Enter number here: "))

    if menu_choice == 1:
        get_all()
        display_menu()
    elif menu_choice == 2:
        get_package(matrix())
    elif menu_choice == 3:
        add_city()
    elif menu_choice == 4:
        edit_table()
    elif menu_choice == 0:
        sys.exit()
    else:
        print("Incorrect number entered please enter another option.")
        display_menu()

display_menu()



