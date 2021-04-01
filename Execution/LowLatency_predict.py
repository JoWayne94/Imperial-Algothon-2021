import numpy as np
import sys
from joblib import load

if __name__ == '__main__':

	# Load trained model from LowLatency_model.py

	knn = load("knn_classifier.joblib")

	# Classify terminal input

	for line in sys.stdin:

		X_in = np.array([float(i) for i in line.split(",")])

		print(int(knn.predict(X_in.reshape(1, -1)) * 1))
