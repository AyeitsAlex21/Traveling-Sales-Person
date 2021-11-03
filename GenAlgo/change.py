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
    selectionResults = [] # list of indexes that represent the mating pool
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"]) # create 3d mutable array
    df['cum_sum'] = df.Fitness.cumsum() # calculating relative fitness
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()  # calculating relative fitness

    for i in range(0, eliteSize): # loop up to the elite size
        selectionResults.append(popRanked[i][0]) # add every elite individual to selection result list
    for i in range(0, len(popRanked) - eliteSize): # loop through remaining size of population
        pick = 100 * random.random() # randomly get a number 0 to 100
        for i in range(0, len(popRanked)): # loop through the population
            if pick <= df.iat[i, 3]: # if random number less then weight of the mate
                selectionResults.append(popRanked[i][0]) # append route id break inner loop
                break
    return selectionResults # return a list of indexes that represent the mating pool

def matingPool(population, selectionResults):
    """
    ([[City]], [int]) -> [[City]]

    Takes the population list and the results of the parent selection list
    to return a list of the parent Routes.

    Called by: nextGeneration
    """
    matingpool = [] # list of routes to mate together
    for i in range(0, len(selectionResults)): # loop to the elite size of the population
        index = selectionResults[i] # index is now id of the route
        matingpool.append(population[index]) # append the route to mating pool
    return matingpool # return the list of parent routes


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
    children = [] # initialize list of children
    length = len(matingpool) - eliteSize # get the remaining size of the population to be filled
    # return random subsequence of the matingpool the size of remaining size
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize): # loop the elite size of the population
        children.append(matingpool[i]) # append the

    for i in range(0, length): # loop to remaining size of the population to be filled
        child = breed(pool[i], pool[len(matingpool) - i - 1]) # breed two parents to get a child
        children.append(child) # append the child to the children list
    return children # return children list


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
    mutatedPop = [] # initialize list of the mutated population

    for ind in range(0, len(population)): # loop up to population size
        mutatedInd = mutate(population[ind], mutationRate) # call mutate on each individual of the population
        mutatedPop.append(mutatedInd) # append the new individual to the mutatedPop
    return mutatedPop # return a list of the mutated routes

def nextGeneration(currentGen, eliteSize, mutationRate):
    """
    ([[City]], int, float) -> [[City]]

    Goes through one generation of the GA based on the initial
    population given.

    Called by: geneticAlgorithm
    """
    popRanked = rankRoutes(currentGen) # sorts the routes from smallest distance to biggest
    selectionResults = selection(popRanked, eliteSize) #
    matingpool = matingPool(currentGen, selectionResults) # selects route ID's to breed
    children = breedPopulation(matingpool, eliteSize) # breeds the population
    nextGeneration = mutatePopulation(children, mutationRate) # mutates the population
    return nextGeneration # returns the new generation of routes