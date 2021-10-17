from structures import *
import random
import operator

def initialPopulation(popSize, cityList):
    """
    (int, [City]) -> [Route]

    This function returns a list of routes the size of popSize based
    on the cityList.
    """
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population

def createRoute(cityList):
    """
    ([City]) -> [Route]

    Helper function creates a valid random route based on the city list given.

    TODO
    MAYBE HAVE TO CHANGE SO IT DOES NOT CHANGE THE STARTING CITY
    """
    temp = cityList[1:]
    route = cityList[0] + random.sample(temp, len(temp))
    return route

def rankRoutes(population):
    """
    ([Route]) -> [Route]

    Given a list of routes representing the population this function sorts the
    population in order of shortest to farthest distances
    """
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Route(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)