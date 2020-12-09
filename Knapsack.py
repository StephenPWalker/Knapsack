import random as rand
from random import sample
##############################################################################
#Create our random start data
##############################################################################
def createData(amount):    
    for i in range(amount):
        weights.append(rand.randint(1,10))
        values.append(rand.randint(1,100))

##############################################################################
#Alogorithms
##############################################################################        
#Iterative heuristic using random search and recursion
def computeKnapsack(weights, values, capacity, value, visited):
    position = sample(range(len(weights)), 1)[0]
    def recurse(weights, values, capacity, value, visited):
        nextPosition = sample(range(len(weights)), 1)[0]
        #Base case
        if capacity == 0 or nextPosition in visited:
            return value, capacity
        else:
            visited.append(nextPosition)           
        if capacity - weights[nextPosition] >= 0:
            result2 = capacity - weights[nextPosition]
            result = value + values[nextPosition]
            listx.append(nextPosition)
        else:
            result = value
            result2 = capacity
            return recurse(weights, values, result2, result, visited)
        return recurse(weights, values, result2, result, visited)   
    return recurse(weights, values, capacity, value, visited) 

#Cached iterative heuristic
def cachedKnapsack(weights, values, capacity, value, visited):
    position = sample(range(len(weights)), 1)[0]
    cache = {}
    def recurse(weights, values, capacity, value, visited, position):
        #Base case
        if capacity == 0 or position in visited:
            return value, capacity
        else:
            visited.append(position)           
        if capacity - weights[position] >= 0:
            result2 = capacity - weights[position]
            result = value + values[position]
            listx.append(position)
            position = sample(range(len(weights)), 1)[0]
        else:
            result = value
            result2 = capacity
            position = sample(range(len(weights)), 1)[0]
            return recurse(weights, values, result2, result, visited, position)
        cache[(value,capacity)] = result, result2
        return recurse(weights, values, result2, result, visited, position)   
    return recurse(weights, values, capacity, value, visited, position)   
##############################################################################
#Hill climbing based search iterative
##############################################################################
def hillClimbingSearch(weights, values, capacity, value, visited):
    position = sample(range(len(weights)), 1)[0]
    for i in range(len(weights) - 2):
        #End case
        if capacity == 0 or position in visited:
            break
        elif(capacity - weights[position] >= 0):
            visited.append(position)
            capacity -= weights[position]
            value += values[position]
            listx.append(position)
            position = sample(range(len(weights)), 1)[0]
    return value,capacity
    
##############################################################################
#Main can edit these values, currently both should return global optimum
##############################################################################    
weights = []
values = []
bestList = []
createData(10)
bestVal = 0
tries =  2000
bagSize = 20
############################################################################## 
# Knapsack using dynamic programming
############################################################################## 
print('Weights: {} \nValues: {}'.format(weights,values))
print('\n####################################################################################\n')
for i in range (tries):
    listx = []
    visited = []
    value, capacity = cachedKnapsack(weights, values, bagSize, 0, visited)
    if(value > bestVal):
        bestVal = value
        bestList = listx
        print('Value of knapsack dynamic programming: {} \nSpace in bag: {}'.format(value,capacity))
        print('Values at indexes used dynamic programming: {}'.format(listx))
##############################################################################
bestVal2 = 0
bestList2 = []
print('\n####################################################################################\n')
##############################################################################
# Knapsack using hillclimbing swap
##############################################################################
for i in range(tries):
    listx = []
    visited = []
    value, capacity = hillClimbingSearch(weights, values, bagSize, 0, visited)
    if(value > bestVal2):
        bestVal2 = value
        bestList2 = listx
        print('Value of knapsack hillclimbing: {} \nSpace in bag: {}'.format(value,capacity))
        print('Values at indexes used hillclimbing: {}'.format(listx))
