import random
import csv


# READ IRIS && TRAIN/TEST SPLIT		

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as datafile:
	    lines = csv.reader(datafile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])
	datafile.close()