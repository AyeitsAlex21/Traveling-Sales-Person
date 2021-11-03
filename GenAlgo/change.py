"""
Source Code for the initialization used in the Genetic Algorithm, CIS422 FA21
Author(s): Eric Stoltz, Alex Summers, Sarah Kitten
Last Edited: 10/28/21
Sources:
    Base version of the code:
    https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
"""

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
    matingpool = [] # list of routes to mate together
    for i in range(0, len(selectionResults)): # loop to the elite size of the population
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
    child = [] # initialize child list
    full_size = len(parent1) # get the length of the route
    edge_map = [] # initialize the edge map list
    for i in range(full_size): # loop up to length of route
        edge_map.append([]) # initialize the 2d aspect of an edge map to empty lists

    # this for loop makes an edge map
    for i in range(full_size): # loop up to size of the route
        right_neighbor = i # initialize index for left neighbor
        left_neighbor = i # initialize index for right neighbor

        if (right_neighbor + 1 == full_size): # if right neighbor + 1 would index outside the list
            right_neighbor = 0 # set right neighbor to 0
        else:
            right_neighbor += 1 # otherwise just add one to the right neighbor to be a right neighbor
        if (left_neighbor == 0):# if left_neighbor - 1 would index outside the list
            left_neighbor = -1 # make left the last index of the list
        else:
            left_neighbor -= 1 # otherwise just minus one to the left neighbor to be a left neighbor

        # if in parent two the right neighbor is not part if of the i'th city's neighbor list
        if (parent2[right_neighbor] not in edge_map[parent2[i].num]):
            edge_map[parent2[i].num].append(parent2[right_neighbor]) # add neighbor to i'th city's neighbor list
        # if in parent two the left neighbor is not part if of the i'th city's neighbor list
        if (parent2[left_neighbor] not in edge_map[parent2[i].num]):
            edge_map[parent2[i].num].append(parent2[left_neighbor]) # add neighbor to i'th city's neighbor list
        # if in parent one the right neighbor is not part if of the i'th city's neighbor list
        if (parent1[right_neighbor] not in edge_map[parent1[i].num]):
            edge_map[parent1[i].num].append(parent1[right_neighbor]) # add neighbor to i'th city's neighbor list
        # if in parent one the left neighbor is not part if of the i'th city's neighbor list
        if (parent1[left_neighbor] not in edge_map[parent1[i].num]):
            edge_map[parent1[i].num].append(parent1[left_neighbor]) # add neighbor to i'th city's neighbor list

    parents = [parent1, parent2] # creating a temp parents list
    gene = parents[int(random.random() * 2)][0] # randomly select first city from both parents
    size = 0 # set initiail size of child to 0

    while(1):
        child.append(gene) # add the city to the child list
        size += 1 # add one to children size
        # Break when child is as big as parent
        if (size >= full_size):
            break

        # remove gene from neighbor list
        for i in range(full_size): # loop up to the parent size
            sub_len = len(edge_map[i]) # get the number of neighbors
            for j in range(sub_len): # loop up to the number of neighbors
                if (edge_map[i][j] == gene): # if found the gene we are trying to remove
                    edge_map[i].pop(j) # remove from edge map
                    break # break from the inner loop to look at another city's neighbor list

        # if gene's neighbor list is empty randomly select from city's not in child
        if (len(edge_map[gene.num]) == 0):
            temp = [] # temp list containing city's who neighbor lists above 0
            for i in range(full_size): # loop up to the parents size
                if(parent1[i] not in child): # if city is not in child list yet
                    temp.append(parent1[i]) # append the city to the temp list
            Z = temp[int(random.random() * len(temp))] # randomly select a city with more than 0 neighbors

        # if not empty find gene's neighbor that has the least neighbors
        else:
            minimum = 5 # a node can have max of 4 neighbors so start minimum high
            sub_len = len(edge_map[gene.num]) # number of neighbors this city has
            temp = [] # temp list containing city's with the least amount of neighbors
            for i in range(sub_len): # loop up to the number of neighbors this city has
                neighbor = edge_map[gene.num][i] # get the neighboring city
                if (len(edge_map[neighbor.num]) < minimum): # if new min is found reset list add new min neighbor
                    minimum = len(edge_map[neighbor.num]) # get the number neighbors the new min has
                    temp = [] # reset temp list
                    temp.append(neighbor) # add the new minimum neighbor to temp list
                elif(len(edge_map[neighbor.num]) == minimum): # if the same amount of neighbors as current min
                    temp.append(neighbor) # add neighbor to temp list
            Z = temp[int(random.random() * len(temp))] # randomly decide if multiple neighbors

        gene = Z # assign the new city to be appended to the child at the start of the loop

    return child # return the child route


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
    if (random.random() < mutationRate): # mutationRate chance for this if condition to be true
        # randomly index into individual route but excluding the first and last index
        ind1 = int(random.random() * (len(individual) - 2)) + 1
        # randomly index to an index above ind1 but not outside list length
        ind2 = ind1 + int(random.random() * (len(individual) - ind1))

        if (ind1 == ind2):  # if the two indexes equal
            ind2 += 2 # add two to ind2 so something can change when mutating
        elif (ind1 + 1 == ind2): # if ind2 is one more then ind1
            ind2 += 1 # add one to ind2 so something can change when mutating
        individual[ind1:ind2] = individual[ind1:ind2][::-1] # inverse subsequence of the individual from ind1 to ind2
    return individual # return the mutated individual


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