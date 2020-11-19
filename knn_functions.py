import math
import operator


# DISTANCE CALCULATION -> Euclidian	

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


# NEIGHBOURS CALCULATION -> used euclideanDistance()  	

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


# ACCURACY ESTIMATION

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range( len(testSet) ):

		#print("testSet[x][-1]:{} | predictions[x]:{}" .format(testSet[x][-1] , predictions[x]) )

		if testSet[x][-1] == predictions[x]:
			correct += 1

			#print("CORRECT !!!!!! CORRECT !!!!!! CORRECT !!!!!!"

	return (correct/float(len(testSet))) * 100.0