"""
Source Code for main used in the Genetic Algorithm, CIS422 FA21
Author(s): Sarah Kitten, Eric Stoltz, Alex Summers
Group Name: NASAK
Last Edited: 10/28/21
Sources:
    Base version of the code:
    https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
"""

from change import *
from initialize import *
import matplotlib.pyplot as plt
from mapsAPI import *

def parse_input(input):
    """
    ([[int]], [str]) -> [City]
    Convert input from maps API into list of city objects
    """
    dist_mtx, name_list = input  # separate tuple from maps API into distance matrix and name list
    cities = []  # initialize list of cities
    for i in range(len(name_list)):
        # for each city in the name list, create a City object and add it to cities
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
    pop = initialPopulation(popSize, population)  # create initial population
    bestSoFar = pop[rankRoutes(pop)[0][0]]  # Store the shortest route from the initial population
    print("Initial distance: " + str(Route(bestSoFar).route_distance()))

    for i in range(0, generations):  # for each generation:
        pop = nextGeneration(pop, eliteSize, mutationRate)  # breed and mutate to form the next generation
        ranked = rankRoutes(pop)  # rank the routes of the new generation
        intermedDist = 1 / ranked[0][1]  # find the shortest route in this generation
        if intermedDist < Route(bestSoFar).route_distance():
            # if the shortest route in this generation is shorter than bestSoFar, update bestSoFar
            bestSoFar = pop[ranked[0][0]]

    print("Final distance: " + str(Route(bestSoFar).route_distance()))

    retval = []  # initialize list of location names
    for city in bestSoFar:  # add each location name to retval
        retval.append(city.name)
    print(retval)
    return retval  # return the shortest route


def geneticAlgorithmPlot(population, popSize, eliteSize, mutationRate, generations):
    """
    :param population: List of citys in chronological order.
    :param popSize: Max size the population can be.
    :param eliteSize: Min size the population can be.
    :param mutationRate: Chance an individual can mutate.
    :param generations: How many times will GA run.
    :return: Route with the shortest approximate distance.

    This function runs the whole Genetic Algorithm and plots the progress of it.
    Returns nothing but prints a graph
        """
    pop = initialPopulation(popSize, population) # create initial population
    progress = [] # the list of route distances to graph
    progress.append(1 / rankRoutes(pop)[0][1]) # puts best distance of initial pop into list to graph later

    for i in range(0, generations): # for each generation:
        pop = nextGeneration(pop, eliteSize, mutationRate) # breed and mutate to form the next generation
        progress.append(1 / rankRoutes(pop)[0][1]) # puts best distance of this gen into list to graph later

    plt.plot(progress) # plots distance on y and generatoins on x
    plt.ylabel('Distance') # plot y label
    plt.xlabel('Generation') # plot x label
    plt.show() # shows graph to user

"""
def test():
    """
    mini testing funciton
    """
    dist_mtx = [
        [0, 2.8, 3],
        [2.8,0,3.6],
        [2.4, 3.5,0]
    ]
    name_list = ["Zero", "One", "Two"]
    newAddresses = ["Orlando, Florida", "Portland, OR", "Salem, OR", "Eugene,OR", "Bend, OR"]
    newAddresses = ['NYC, NY', 'Cocoa Beach,FL', 'San Francisco, CA', 'Eugene,OR']
    # dist_mtx, name_list = genMatrix(newAddresses)

    name_list = ['NYC, NY', 'Cocoa Beach,FL', 'San Francisco, CA', 'Eugene,OR']
    dist_mtx = [[0, 1103.0, 2906.0, 2910.0], [1102.0, 0, 2877.0, 3103.0], [2903.0, 2874.0, 0, 530.0], [2911.0, 3106.0, 528.0, 0]]
    print(dist_mtx)
    print(name_list)

    population = parse_input((dist_mtx, name_list))
    popSize = 100
    eliteSize = 50
    mutationRate = 0.05
    generations = 8
    geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)


if __name__ == "__main__":
    test()
"""
