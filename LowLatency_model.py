from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from joblib import dump, load


if __name__ == '__main__':

	# Load Training dataset

	df = pd.read_csv(f"LatencyTraining.csv").iloc[:,1]

	temp = pd.DataFrame(df.copy())

	# Create windowsize, K no. of neighbours, features and targets

	WINDOWSIZE = 500
	K = 100

	for i in range(WINDOWSIZE - 1):

	  next_return = pd.DataFrame(df.shift(i + 1))
	  next_return.columns = [f'LogReturns_tm{i + 1}']
	  temp = pd.concat([temp, next_return], axis = 1)

	# Declare and train model using KNN

	X, y = temp.iloc[WINDOWSIZE - 1:-1], df.shift(-1).iloc[WINDOWSIZE - 1:-1]

	classifier = KNeighborsClassifier(n_neighbors = K)

	knn = classifier.fit(X, y > 0)

	# Store model as library

	dump(knn, 'knn_classifier.joblib')

