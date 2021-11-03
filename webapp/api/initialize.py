"""
Source Code for the initialization used in the Genetic Algorithm, CIS422 FA21
Author(s): Sarah Kitten, Eric Stoltz, Alex Summers
Group Name: NASAK
Last Edited: 10/28/21
Sources:
    Base version of the code:
    https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
"""

from structures import *
import random
import operator

def initialPopulation(popSize, cityList):
    """
    (int, [City]) -> [[City]]

    This function returns a list of lists of cities the size of popSize based
    on the cityList.

    Called by: geneticAlgorithm
    """
    population = [] # initialize population list

    for i in range(0, popSize): # loop up to desired population size
        population.append(createValidCityList(cityList)) # populate list with valid routes
    return population

def createValidCityList(cityList):
    """
    ([City]) -> [City]

    Helper function creates a valid random route based on the city list given.
    Keeps the first city as the first city.

    Called by: initialPopulation
    """
    temp = [] # initialize an empty list
    # if the list of city's is 2 or more make temp list a copy of city list without the first city
    if(len(cityList) >= 2):
        temp = cityList[1:]

    # keep the first city first and randomize the rest of the city's order to create a valid route
    route = [cityList[0]] + random.sample(temp, len(temp))
    return route

def rankRoutes(population):
    """
    ([[City]]) -> [(int, float)]

    Given a list of lists of cities representing the population,
    returns a list of tuples (index of population, route fitness) sorted in decreasing order of route fitness

    Called by: nextGeneration, geneticAlgorithm
    """

    fitnessResults = {} # intialize an empty dictionary that will contain route fitnesses
    for i in range(0,len(population)): # loop through the population
        # create a temp Route object using a route from of the population then calculate and return its fitness
        fitnessResults[i] = Route(population[i]).routeFitness()
    # sort fitnessResults in ascending order of fitness
    # returns a list of tuples the first index being the city number and the second being the fitness
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)
