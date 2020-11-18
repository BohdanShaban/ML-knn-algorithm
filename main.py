import csv
import random
import math
import operator

# READ IRIS && TRAIN/TEST SPLIT		

fileName = 'iris.data'
split = 0.7
trainingSet=[]
testSet=[]

with open(fileName, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

print('Train set: ' + repr(len(trainingSet)))
print('Test set: ' + repr(len(testSet)))

