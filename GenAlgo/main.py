from change import *
from initialize import *

"""
TODO:

Experiment with values for popSize, eliteSize, mutationRate, generations
Make an option to force routes to return to the start (each route will begin and end with the "first" city)
"""


def parse_input(input):
    """
    ([[int]], [str]) -> [City]
    Convert input from maps API into list of city objects
    TODO more input checking?
    """
    dist_mtx, name_list = input
    cities = []
    for i in range(len(name_list)):
        cities.append(City(name_list[i], i, dist_mtx[i]))
    return cities


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    """
    :param population: List of citys in chronological order.
    :param popSize: Max size the population can be.
    :param eliteSize: Min size the population can be.
    :param mutationRate: Chance an individual can mutate.
    :param generations: How many times will GA run.
    :return: Route with the shortest approximate distance.

    This function runs the whole Genetic Algorithm.
    Returns list of location names (str)
    """
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(int(1 / rankRoutes(pop)[0][1])))
    bestSoFar = Route(pop[rankRoutes(pop)[0][0]])

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        ranked = rankRoutes(pop)
        intermedDist = 1 / ranked[0][1]
        if intermedDist < bestSoFar.route_distance():
            bestSoFar = Route(pop[ranked[0][0]])

    print("Final distance: " + str(bestSoFar.route_distance()))
    retval = []
    for city in bestSoFar.route:
        retval.append(city.name)
    print(retval)
    return retval


def test():
    dist_mtx = [
        [0, 5, 8, 5, 12, 20, 30, 40],
        [5, 0, 1, 3, 13, 30, 20, 40],
        [8, 1, 0, 2, 10, 20, 40, 30],
        [6, 5, 2, 0, 7, 10, 40, 20],
        [13, 13, 10, 14, 0, 30, 10, 40],
        [20, 30, 20, 10, 15, 0, 3, 5],
        [30, 20, 40, 40, 30, 4, 0, 2],
        [40, 50, 40, 20, 40, 5, 2, 0]
    ]
    name_list = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    population = parse_input((dist_mtx, name_list))
    popSize = 20
    eliteSize = 5
    mutationRate = 0.5
    generations = 100
    geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)


def main():
    return 0


if __name__ == "__main__":
    test()