from change import *

"""
NOTE FOR GROUPMATES:
Not sure when the population gets cut down to be honest.
Did not import the files to one another.
Did not test anything yet.
In change.py the function selection prob need import pandas as pd
"""

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
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


def test():
    population = [City(0), City(1), City(2), City(3), City(4)]
    popSize = 10
    eliteSize = 5
    mutationRate = 0.5
    generations = 30
    geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)


def main():
    return 0


if __name__ == "__main__":
    test()