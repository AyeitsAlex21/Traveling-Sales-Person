import random
from initialize import *
import pandas as pd
import numpy as np

def selection(popRanked, eliteSize):
    """
    ([(int, float)], int) -> [int]

    Uses a sorted list of (index, route fitness) tuples and the size we want the population
    to shrink down to, to output a list of indices that represent
    the selected parents to mate in the population.

    Called by: nextGeneration
    """
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

def matingPool(population, selectionResults):
    """
    ([[City]], [int]) -> [[City]]

    Takes the population list and the results of the parent selection list
    to return a list of the parent Routes.

    Called by: nextGeneration
    """
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2):
    """
    ([City], [City]) -> [City]

    Uses Genetic Edge Recombination on the two parents to output a child path.

    Called by: breedPopulation

    //TODO:
    DOWN BELOW IS NOT THE GENETIC EDGE RECOMBINATION WE NEED TO CHANGE BUT MAYBE
    TEST WITH THIS IMPLEMENTATION
    """
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child


def breedPopulation(matingpool, eliteSize):
    """
    ([[City]], int) -> [[City]]

    Takes a list of selected parents and breeds them to output a
    list of children.

    Called by: nextGeneration
    """
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children


def mutate(individual, mutationRate):
    """
    ([City], float) -> [City]

    Randomly mutates the list of cities based on the mutation rate.

    Called by: mutatePopulation
    """
    if random.random() < mutationRate:
        # randomly select indices greater than 0 (do not mutate first index)
        ind1 = int(random.random() * (len(individual) - 2)) + 1
        ind2 = ind1 + int(random.random() * (len(individual) - ind1))

        if ind1 == ind2:
            ind2 += 2
        elif ind1 + 1 == ind2:
            ind2 += 1
        individual[ind1:ind2] = individual[ind1:ind2][::-1]
    return individual


def mutatePopulation(population, mutationRate):
    """
    ([[City]], float) -> [[City]]

    Calls the mutate function on every indivdual in the population

    Called by: nextGeneration
    """
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def nextGeneration(currentGen, eliteSize, mutationRate):
    """
    ([[City]], int, float) -> [[City]]

    Goes through one generation of the GA based on the initial
    population given.

    Called by: geneticAlgorithm
    """
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration