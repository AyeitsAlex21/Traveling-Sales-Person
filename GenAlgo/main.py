from change import *
from initialize import *

"""
TODO:
Replace the mutation and breeding algorithms with the superior ones
Force the first city to be the first city for all routes
    Need changes to createRoute (DONE MAYBE), breed, and mutate
    
Eventually:
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

    This function runs the whole Genitic Algorithm.
    """
    pop = initialPopulation(popSize, population)
    print(rankRoutes(pop))
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestSoFar = Route(pop[rankRoutes(pop)[0][0]])

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        intermedDist = 1 / rankRoutes(pop)[0][1]
        # if intermedDist < bestSoFar:
        #     bestSoFar = intermedDist
        #print("best so far: " + str(bestSoFar))

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    print(bestRoute)
    return bestRoute


def test():
    dist_mtx = [
        [0, 5, 8, 5, 12],
        [5, 0, 1, 3, 13],
        [8, 1, 0, 2, 10],
        [6, 5, 2, 0, 7],
        [13, 13, 10, 14, 0]
    ]
    name_list = ["Zero", "One", "Two", "Three", "Four"]
    population = parse_input((dist_mtx, name_list))
    popSize = 10
    eliteSize = 5
    mutationRate = 0.5
    generations = 30
    geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)


def main():
    return 0


if __name__ == "__main__":
    test()