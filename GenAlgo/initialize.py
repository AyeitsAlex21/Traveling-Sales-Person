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
    population = []

    for i in range(0, popSize):
        population.append(createValidCityList(cityList))
    return population

def createValidCityList(cityList):
    """
    ([City]) -> [City]

    Helper function creates a valid random route based on the city list given.
    Keeps the first city as the first city.

    Called by: initialPopulation
    """
    if(len(cityList) >= 2):
        temp = cityList[1:]
    else:
        temp = cityList
    route = [cityList[0]] + random.sample(temp, len(temp))
    return route

def rankRoutes(population):
    """
    ([[City]]) -> [(int, float)]

    Given a list of lists of cities representing the population,
    returns a list of tuples (index of population, route fitness) sorted in decreasing order of route fitness

    Called by: nextGeneration, geneticAlgorithm
    """
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Route(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)