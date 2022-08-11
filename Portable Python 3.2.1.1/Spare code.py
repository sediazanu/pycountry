#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      aazan
#
# Created:     16/01/2018
# Copyright:   (c) aazan 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()
CITY1 = "London"
CITY2 = 500
CITY3 = 400
CITY4 = 200
CITY5 = 900

cursor.execute("""INSERT INTO CITY1(CITY1, CITY2, CITY3, CITY4, CITY5) Values(?,?,?,?,?)""", (CITY1, CITY2, CITY3, CITY4, CITY5))
City1 = "London"
Package1 = "All-Inclusive"
Hotel1 = "Hilton"
##this inserts the informaiton into the table
cursor.execute("""INSERT INTO Package(City, Package, Hotel) Values(?,?,?)""", (City1, Package1, Hotel1))
City2 = "Malaga"
Package2 = "All-Inclusive"
Hotel2 = "Club la costa"
##this inserts the informaiton into the table
cursor.execute("""INSERT INTO Package(City, Package, Hotel) Values(?,?,?)""", (City1, Package1, Hotel1))
packageid1= 1
cursor.execute("""SELECT City, Package, Hotel FROM Package WHERE PackageID=?""",(packageid1,))
package = cursor.fetchone() ##This fetches the part of the table which was asked for.
print(package)##This prints out the selected code
def get_posts():
        cursor.execute("SELECT * FROM Package")##selects everything from the package
        print(cursor.fetchall())##prints everything that was selected including ids
        cursor.execute("SELECT * FROM CITY1")
        print(cursor.fetchall())

get_posts()

db.close()