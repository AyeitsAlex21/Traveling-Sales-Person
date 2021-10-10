
class City():
    def __init__(self):
        self.name
        self.num = -1

    def distance(self, other):
        """
        (City) -> (float)

        returns the distance from the self city to the other city

        TODO
        NEED ADJ MATRIX TO GET DISTANCES
        """
        return 1


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
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness