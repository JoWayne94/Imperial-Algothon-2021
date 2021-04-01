# Description & Context

Where to find the data?
They are avaialble in the following Google drive. https://drive.google.com/drive/folders/180FaVThDIFtmrCZ2cGiYskvlyvyMv5Au

**Data Cleaning Challenge**

A small timeseries dataset has been corrupted in some form. This dataset is cleaned and evaluated on the MSE of the cleaned dataset and the uncorrupted data.

**Submission**
Uncorrupted the 'data_clean.csv' file and submitted the clean vision: "LaPacks_data_cleaning.csv".

**Results**
2nd out of 50 teams.

**Long-Short Sector Strategy Challenge**
**Goal**
Students were asked to choose develop a long-short strategy in one of the 3 sectors provided (tech=1, energy=2 and gold=3).

They must have a neutral position at all times, and their task is to provide a time series of weights of their long and short stocks. The weights can be any number between -1 and 1, with a negative number meaning a short position.

Within the provided class (LongShort), the predict() function takes as input the features relevant to a ticker and a given time index (a specific day). The output of this function needs to be a number between -1 and 1, representing the position on that asset at that specific timestamp. Note that for a given timestamp, the sum of the weights for all tickers must equal 0 to give a neutral position.

**Evaluation Criteria**
The performance of the model was assessed by calculating cumulative returns-0.5 * max drawdown. This metric needs to be maximised.

**Data**
The data provided contains 5 US stocks from the sector chosen. Several encrypted features are provided and the target are the forward 5-day log returns.

**Submission**
Validation data: "LaPacks_validation_long_short.csv", Test data: "LaPacks_test_long_short.csv".

**Results**
2nd out of 50 teams.

**Low Latency Challenge**

This repository contains a classifier that predicts whether a single ticker's price will go up or down in the next sample, based on the 500 previous log returns.

Files:
1. LatencyTraining.csv - Data provided with log returns for training purposes
2. LowLatency_model.py - Trains a k-Nearest-Neighbors (k-NN) Model with Scikit-learn using provided data 2.
3. LowLatency_predict.py - Imports the classifier and take inputs through the terminal. The input will be several comma separated terms
4. Makefile - File used to compile code for the program

=================================================================

Run **make run**. In the command line, please input 500 numbers delimited by commas (previous log returns).
Returns 1 or 0 if it expects the signal to increase or decrease respectively.

**Test Run**
Run **time make run < test_case{i}.txt** for the numpy version, and **time python latency_predict_old.py < test_case{i}.txt**

Files:
1. test_case1.txt - single line of input
2. test_case2.txt - multiple lines of input
3. test_case3.txt - original training data LatencyTraining.csv
