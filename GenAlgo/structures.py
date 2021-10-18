class City():
    """
    City class, used to store a location and its distances from other locations.
    Accepts name (str), num (int), and distances (list of floats) as input.
    """
    def __init__(self, name, num, distances):
        self.name = name
        self.num = num
        self.distances = distances

    def __str__(self):
        return "City:" + self.name

    def __repr__(self):
        return "City:" + self.name

    def distance(self, other):
        """
        (City) -> (float)

        returns the distance from the self city to the other city
        """
        return self.distances[other.num]


class Route():
    """
    Route class, used for calculating the distance and fitness of a list of Cities.
    Accepts route (list of Cities) as input.
    """
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
        """
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness