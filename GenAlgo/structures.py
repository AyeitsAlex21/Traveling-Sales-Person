dist_mtx = [
    [0, 5, 8, 5, 12],
    [5, 0, 1, 3, 13],
    [8, 1, 0, 2, 10],
    [6, 5, 2, 0, 7],
    [13, 13, 10, 14, 0]
]
"""
Sample matrix for testing:
5 cities (named 0-4) with distances to all others.
Distance from city 0 to city 4 = dist_mtx[0][4]
"""

class City():
    # changed this to accept name as input
    def __init__(self, name):
        self.name = name
        self.num = -1

    def distance(self, other):
        """
        (City) -> (float)

        returns the distance from the self city to the other city

        TODO
        NEED ADJ MATRIX TO GET DISTANCES
        """
        return dist_mtx[self.name][other.name]


class Route():
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0

    def route_distance(self):
        """
        ()->(float)

        calculates the distance of route updating the distance variable
        also returns the distance
        """
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        """
        () -> float

        Calls route distance so it can determine fitness

        TODO
        PROBABLY TAKE OUT THE IF SO WE CAN CHANGE THE ROUTE DISTANCE AND
        FITNESS MORE OFTEN.
        """
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness