"""display_menu is the interface for the database that allows the user to be able to access parts of the database.
get_menu allows for the user to gain access to a specific function by typing in one of the values. If the value isnt between what is allowed,
the user will be stuck in a loop until the variable "accepted" becomes true.

My plan is for the menu to have several functions: Creating a new table, adding new countries, editing countries, deleting countries and searching
for specific countries. This allows the user to make several adjustments to the table in case anything happens to go wrong.

the value {0} represents the name of the table itself which can be seen as when the code is played, instead of it saying {0}, it uses the table name
as the table_name variable appears as a result instead.



"""

# SQLITE is a c library that provides a lightweight disk-based datanase that doesnt require a seperate server process,
# and allows accessing the database using a non-standard variant of the SQL query language
#import allows for functions that are defined elsewhere to be used in this code.

import sqlite3
""" This function below is what creats the table by """

# What is this? What is a function?

#Custom functions

# def is used to...
def create_table(table_name,sql): #what are table_name and sql?
    with sqlite3.connect(DATABASE) as db: # this allows for the function to be stored in a variable so that it is easier to write for the user.
        print(table_name) #this prints the name of the database
        cursor = db.cursor() # this enables traversal over the records in a database.
        cursor.execute("select name from sqlite_master where name=?",(table_name,)) # This method executes the database, which the name is given by sqlite_master
        result = cursor.fetchall() #this method fetches all the rows of a query result and returns a list of tuples.
        keep_table = True
        if len(result) == 1: #If the length of the results ==1, it shows there is a database, which means that to create a new table the current one would have to be deleted
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == "y": #if the user enters y, then the original table is overwritten and a new one is made
                keep_table = False
                print("Value of...", keep_table)
                print("The {0} table will be recreated - all existing data will be lost".format(table_name)) # prints this to tell the user everything is being deleted.
                cursor.execute("drop table if exists {0}".format(table_name)) #drops the current table and replaces it with the new one.
                db.commit() #updaes all the records in the table.
            else:
                print("The existing table was kept") #prints this if the user enters anything except y.
        else:
            keep_table = False
            print(keep_table)
        if not keep_table: #Do not understand that this does.
            cursor.execute(sql)
            db.commit()


def query(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def display_menu():
    print("Package Holiday Database")
    print()
    print("1. (Re)Create Tables", "\n", "2. Add new city")
    print("2. Add new city")
    print("3. Edit existing city")
    print("4. Delete existing city")
    print("5. Search for cities")
    print("6. Display the entire database")
    print("0. Exit")
    print()



"""This option allows for the user to select a menu choice ranging from 0 to 5. 1 goes to the function that allows for the user to recreate the table
2 Allows for the user to add a new record to the table. 3 Allows the user to edit an existing records fields, 4 allows for a record to be deleted
from the table and 5 allows for a record to be searched."""
def get_menu_choice():
    accepted = False
    while not accepted:
     choice = input("Please select an option:")
     if "0" == choice or "1" == choice or "2" == choice or "3" == choice or "4" == choice or "5" == choice or "6" == choice:
       accepted = True
     else:
      print("Pleae enter a valid value")
    return choice

def insert_data(values):
    sql = "insert into City (City,Country,TimeZone,Population,Nationallanguage,currency) values(?,?,?,?,?,?)"
    query(sql,values)

def query_with_results(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        if data == None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,data)
        results = cursor.fetchall()
        return results

def query_with_single_result(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        result = cursor.fetchone()
        return result

""" This function is used to display the results of the search from the person using the database. Current issue is that due to the amount of
fields the function is not displaying due to a "tuple index out of range" error appearing

The print function is not printing all the column headings due to there being a tuple index out of range error, however the
results are printing.

https://stackoverflow.com/questions/20296188/indexerror-tuple-index-out-of-range-python
one of the indexes may be incorrect.

https://pypi.python.org/pypi/PTable/0.9.0

Deleted one of the sql variables as it was not needed and a shortened table causes less problems.
"""

#added CountryID to sql variable
def update_country(data):
    sql = "update Country set Country=?, Capital=?, TimeZone=?, Population=?, Nationallanguage=?, Currency=? where CountryID=?"
    print(sql)
    query(sql,data)

def display_select_results(results):
    if results[0] != None:
        print()
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15} {5:<15} {6:<15}".format("Country ID","Country Name","Capital", "TimeZone", "Population","National Language","Currency"))
        for result in results:
            print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15} {5:<15} {6:<15}".format(result[0],result[1],result[2],result[3],result[4],result[5],result[6]))
        print()
    else:
        print("The query returned no results")

"""This displays all the records that fall under the criteria of the requirements"""
def select_all_cities():
    sql = "select * from City"
    return query_with_results(sql,None)

"""the main function which gets called at the bottom. This allows people to be linked to the database as the functions given that can change the database can allow things to be edited
or changed to have new things."""
def main():
    finished = False
    while not finished:
        display_menu()
        choice = get_menu_choice()
        if choice == "1":
            choice2 = input("Select a number between 1-3 for the type of table to be created 1= City table. 2= Package type. 3= Matrix table")#This entire code allows for the database to have 1 of 3 tables added to it. One being the normal city table, another being the type of package for each of the cities and the third being a matrix looking at how far each of the cities are from each other.
            if choice2 == "1":
             sql = """create table City
             (CityID integer,
             City text,
             Country text,
             TimeZone text,
             Population text,
             Nationallanguage text,
             Currency text,
             primary key(CityID))"""
             create_table("City",sql)
            if choice2 == "2":
             sql = """create table Package
             (PackageID integer,
             Country text,
             primary key(PackageID))"""
             create_table("Package",sql)
            if choice2 == "3":
             sql = """create table Matrix
             (City text,
             London text,
             Paris text,
             Sydney text,
             Florida text,
             New York text,
             Malaga text,
             Dubai text,
             Berlin text,
             Cancun text,
             Accra, text
             primary key(City))"""
            create_table("Matrix",sql)
        elif choice == "2":
            city = input("Please enter name of new city: ")
            Country = (input("Please enter the country the city is in"))
            TimeZone = input("What is the timezone of the city")
            Population = input("What is the population of the city")
            Nationallanguage = input("What is the national language of the city")
            currency = input("What is the currency of the city")
            insert_data((city,Country,TimeZone,Population,Nationallanguage,currency))
        elif choice == "3":
            countries = select_all_countries()
            display_select_results(countries)
            CountryID = int(input("Please enter the id of the city to edit: "))
            country = input("Please enter new name for the City: ")
            Capital = (input("Please enter the Country the city is in: "))
            TimeZone = input("What is the timezone of the city")
            Population = input("What is the population of the city")
            Nationallanguage = input("What is the national language of the city")
            currency = input("What is the currency of the city")
            update_country((city,Country,TimeZone,Population,Nationallanguage,currency,CountryID))
        elif choice == "4":
            countries = select_all_countries()
            display_select_results(countries)
            CountryID = int(input("Please enter the id of the country to delete: "))
            Country = select_country(CountryID)
            delete_country((Country[1],))
        elif choice == "5":
            name = input("Please enter the name of the country to search for: ")
            country = select_country_with_name(name)
            display_select_results([country])
        elif choice == "6":
            cities = select_all_cities()
            display_select_results(cities)

        elif choice == "0":
            finished = True

def select_country_with_name(name):
    sql = "select * from Country where Country=?"
    return query_with_single_result(sql,(name,))

def select_country(id):
    sql = "select * from Country where CountryID=?"
    return query_with_single_result(sql,(id,))

def delete_country(data):
    sql = "delete from Country where Country=?"
    query(sql,data)

if __name__ == "__main__":
    DATABASE = "cities.db"
    main()
