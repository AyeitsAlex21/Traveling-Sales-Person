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
    full_size = len(parent1)
    edge_map = []
    for i in range(full_size):
        edge_map.append([])

    # this for loop makes an edge map
    for i in range(full_size):
        right_neighbor = i
        left_neighbor = i

        if (right_neighbor + 1 == full_size):
            right_neighbor = 0
        else:
            right_neighbor += 1
        if (left_neighbor == 0):
            left_neighbor = -1
        else:
            left_neighbor -= 1

        if (parent2[right_neighbor] not in edge_map[parent2[i].num]):
            edge_map[parent2[i].num].append(parent2[right_neighbor])
        if (parent2[left_neighbor] not in edge_map[parent2[i].num]):
            edge_map[parent2[i].num].append(parent2[left_neighbor])
        if (parent1[right_neighbor] not in edge_map[parent1[i].num]):
            edge_map[parent1[i].num].append(parent1[right_neighbor])
        if (parent1[left_neighbor] not in edge_map[parent1[i].num]):
            edge_map[parent1[i].num].append(parent1[left_neighbor])

    parents = [parent1, parent2]
    gene = parents[int(random.random() * 2)][0]
    size = 0

    while(1):
        child.append(gene)
        size += 1
        # Break when child is as big as parent
        if (size >= full_size):
            break

        # remove gene from neighbor list
        for i in range(full_size):
            sub_len = len(edge_map[i])
            for j in range(sub_len):
                if (edge_map[i][j] == gene):
                    edge_map[i].pop(j)
                    break

        # if gene's neighbor list is empty randomly select from city's not in child
        if (len(edge_map[gene.num]) == 0):
            temp = []
            for i in range(full_size):
                if(edge_map[parent1[i].num] not in child):
                    temp.append(parent1[i])
            Z = temp[int(random.random() * len(temp))]

        # if not empty find gene's neighbor that has the least neighbors
        else:
            minimum = 5
            sub_len = len(edge_map[gene.num])
            for i in range(sub_len):
                neighbor = edge_map[gene.num][i]
                if (len(edge_map[neighbor.num]) < minimum):
                    minimum = len(edge_map[neighbor.num])
                    Z = neighbor
                elif(len(edge_map[neighbor.num]) == minimum):
                    if (random.random() >= 0.5):
                        Z = neighbor

        gene = Z

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
    if (random.random() < mutationRate):
        ind1 = int(random.random() * (len(individual) - 2)) + 1
        ind2 = ind1 + int(random.random() * (len(individual) - ind1))

        if (ind1 == ind2):
            ind2 += 2
        elif (ind1 + 1 == ind2):
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