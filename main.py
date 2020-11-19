from read_data import loadDataset
from knn_functions import getNeighbors, getResponse, getAccuracy


def main():

	# READ IRIS && TRAIN/TEST SPLIT	
	trainingSet=[]
	testSet=[]
	split = 0.7
	loadDataset('iris.data', split, trainingSet, testSet)
	print ('Train set: ' + repr(len(trainingSet)))
	print ('Test set: ' + repr(len(testSet)))

	# NEIGHBOURS CALCULATION && RESPONSE PREDICTION
	predictions=[]
	k = 3
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		predicted = getResponse(neighbors)
		predictions.append(predicted)
		print('> predicted=' + repr(predicted) + ', actual=' + repr(testSet[x][-1]))

	# ACCURACY ESTIMATION
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')

main()