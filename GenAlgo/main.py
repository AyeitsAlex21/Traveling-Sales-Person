"""
Source Code for main used in the Genetic Algorithm, CIS422 FA21
Author(s): Eric Stoltz, Sarah Kitten, Alex Summers
Last Edited: 10/28/21
Sources:
    Base version of the code:
    https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
"""

from change import *
from initialize import *
import matplotlib.pyplot as plt

def parse_input(input):
    """
    ([[int]], [str]) -> [City]
    Convert input from maps API into list of city objects
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

    #dist_mtx, name_list = genMatrix(newAddresses)

    population = parse_input((dist_mtx, name_list))
    popSize = 100
    eliteSize = 50
    mutationRate = 0.05
    generations = 8
    geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)


if __name__ == "__main__":
    test()
