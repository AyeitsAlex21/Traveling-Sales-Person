from change import *
from initialize import *
import matplotlib.pyplot as plt
from mapsAPI import *

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
    bestSoFar = Route(pop[rankRoutes(pop)[0][0]])
    print("Initial distance: " + str(bestSoFar.route_distance()))

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


def geneticAlgorithmPlot(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    progress = []
    progress.append(1 / rankRoutes(pop)[0][1])

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()

def test():
    dist_mtx = [
        [0, 2.8, 3],
        [2.8,0,3.6],
        [2.4, 3.5,0]
    ]
    name_list = ["Zero", "One", "Two"]

    newAddresses = ["13th & Olive, 1180 Willamette St, Eugene, OR 97401", "Chase Village Student Housing, 375 Marche Chase Dr, Eugene, OR 97401",
                    "Valley River Inn, 1000 Valley River Way, Eugene, OR 97401"]
    dist_mtx, name_list = genMatrix(newAddresses)

    population = parse_input((dist_mtx, name_list))
    popSize = 100
    eliteSize = 50
    mutationRate = 0.05
    generations = 8
    geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)


if __name__ == "__main__":
    test()
