"""
Source Code for classes used in the Genetic Algorithm, CIS422 FA21
Author(s): Sarah Kitten, Eric Stoltz, Alex Summers
Group Name: NASAK
Last Edited: 10/28/21
Sources:
    Base version of the code:
    https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
"""

class City():
    """
    City class, used to store a location and its distances from other locations.
    Accepts name (str), num (int), and distances (list of floats) as input.
    """
    def __init__(self, name, num, distances):
        self.name = name # city name
        self.num = num # the number that the city was received
        self.distances = distances  # adj list containing list of distances to other city's

    def __str__(self):
        return self.name # displays name of the city

    def __repr__(self):
        return self.name # displays name of the city

    def distance(self, other):
        """
        (City) -> (float)

        returns the distance from the self city to the other city
        """
        return self.distances[other.num]  # returns distance from current city to the other city


class Route():
    """
    Route class, used for calculating the distance and fitness of a list of Cities.
    Accepts route (list of Cities) as input.
    """
    def __init__(self, route):
        self.route = route # list containing different city's representing a route
        self.distance = 0  # distance of the route
        self.fitness = 0   # this says how good each route is

    def __str__(self):
        return str(self.route) # print out list of city's representing the route

    def route_distance(self):
        """
        ()->(float)

        calculates the distance of route updating the distance variable
        also returns the distance
        """
        # if the route distance has not been evaluated yet evaluate it
        if self.distance == 0:
            # temp variable containing the distance of the route
            pathDistance = 0
            # loop through each city in the route
            for i in range(0, len(self.route)):
                fromCity = self.route[i]  # saving the from city
                toCity = None  # initializing the to city to None
                # if not end of the route list set toCity to the next city in route
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                # at last iteration of loop set toCity first city of the route
                else:
                    toCity = self.route[0]
                # add the distance from fromCity to toCity to the temp var
                pathDistance += fromCity.distance(toCity)
            # once route has been calculated assign the temp variable to the class distance variable
            self.distance = pathDistance
        return self.distance # return the distance of the route

    def routeFitness(self):
        """
        () -> float

        Calls route distance so it can determine fitness
        """
        if self.fitness == 0: # if the fitness has not been evaluated execute
            # fitness is the inverse of the distance
            self.fitness = 1 / float(self.route_distance())
        return self.fitness # return the route fitness
