    ##Found help with this code section by using the link https://stackoverflow.com/questions/29481485/creating-a-distance-matrix


from math import sin, cos, sqrt, atan2, radians
def matrix():
    ##approx radius of earth in km
    radius = 6373.0
    cords = {}##This creats the dictonary to store the values
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
    for items in cords.items():
        print(str(items))


    for city1, cords1 in cords.items(): ##This finds any of the data values in the dictionary and iterates until all data values have been found
        Matrix[city1] = {} ##This creates the heading for the first city in the dictionary
        print(city1, cords1)
        for (city2, cords2) in cords.items(): ##This finds the second city to compare to the first city to.
            Matrix[city1][city2] = dist(cords1, cords2) ##This stores the distance between the two cities after the funciton is completed


    for city1, x in Matrix.items(): ##This finds each of the fields and all of the column values that follow them. x is the value of the second dictionary
                                     ##This is repeated until all the cities in the table have been found
        for city2, d in x.items():##This finds in the second dictionary the city and the value attached to that city, which was found with the dist() function
            print (city1, city2, d) ##This finds all of the values found and prints them.#

matrix()
