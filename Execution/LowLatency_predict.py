"""
Inputs:  A row of 500 windowsized log returns, delimited by commas.
Outputs: Prediction of 0 and 1, if next timestep log return is going to decrease or increase.
"""

import numpy as np
import sys
from joblib import load

if __name__ == '__main__':

	# Load trained model from LowLatency_model.py

	knn = load("knn_classifier.joblib")

	# Classify terminal input

	for line in sys.stdin:

		X_in = np.array([float(i) for i in line.split(",")]).reshape(1, -1)

		print(int(knn.predict(X_in) * 1))
