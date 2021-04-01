# Long-Short Sector Strategy Challenge

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
