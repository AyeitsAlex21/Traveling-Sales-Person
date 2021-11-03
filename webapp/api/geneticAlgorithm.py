from change import *
from initialize import *
import matplotlib.pyplot as plt
from mapsAPI import *


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
