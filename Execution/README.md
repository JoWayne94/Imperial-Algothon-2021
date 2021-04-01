# Low Latency Challenge

This repository contains a classifier that predicts whether a single ticker's price will go up or down in the next sample, based on the 500 previous log returns.

Files:
1. LatencyTraining.csv - Data provided with log returns for training purposes
2. LowLatency_model.py - Trains a k-Nearest-Neighbors (k-NN) Model with Scikit-learn using provided data 1.
3. LowLatency_predict.py - Imports the classifier and take inputs through the terminal. The input will be several comma separated terms
4. Makefile - File used to compile code for the program

==============================================================================================

Run **make run**. In the command line, please input 500 numbers delimited by commas (previous log returns).
Returns 1 or 0 if it expects the signal to increase or decrease respectively.

**Test Run**

Run **time make run < test_case{i}.txt** for the k-NN version.

Files:
1. test_case1.txt - single line of input
2. test_case2.txt - multiple lines of input
