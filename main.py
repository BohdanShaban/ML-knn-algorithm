import csv
import random
import math
import operator


# READ IRIS && TRAIN/TEST SPLIT		
import math

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])


# DISTANCE CALCULATION -> Euclidian	

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


# NEIGHBOURS CALCULATION -> used euclideanDistance()  	
import operator 

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors


# RESPONSE PREDICTION -> based on getNeighbors() 
import operator
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted( classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

# Test the getResponse function 
			
neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = getResponse(neighbors)
print(response)


def main():
	# READ IRIS && TRAIN/TEST SPLIT	
	trainingSet=[]
	testSet=[]
	split = 0.7
	loadDataset('iris.data', split, trainingSet, testSet)
	print ('Train set: ' + repr(len(trainingSet)))
	print ('Test set: ' + repr(len(testSet)))


main()