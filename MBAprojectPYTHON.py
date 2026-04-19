# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:09:29 2026

@author: yadav
"""

# Importing the required libraries

import pandas as pd    #data manipulation and analysis
import numpy as np     #numerical operations
import matplotlib.pyplot as plt     # for plotting
import os

os.chdir("Downloads")  # for changing the directory

# read the file as text

with open("groceries.csv","r") as file:
    lines= file.readlines()

# split each line by commas and create a list

transactions= [line.strip().split(',') for line in lines]

#Create a dataframe from transactions

data= pd.DataFrame(transactions)

data

# Loop through the data to convert it into a suitable format 

transactions = [] 

for i in range(0, 9835): # Assuming there are 9835 transactions 

    # Convert each transaction into a list of strings 

  transactions.append([str(data.values[i,j]) for j in range(0, 32)]) 

 

# Training the Apriori model on the dataset 

from apyori import apriori 

rules = apriori(transactions = transactions,  

min_support = 0.003, min_confidence = 0.2,  

min_lift = 3, min_length = 2) 

 

# Apriori Algorithm Explanation: 

# The Apriori algorithm is a popular algorithm used in association rule mining, a technique in data mining and market basket analysis (MBA). 

# It works by discovering association rules between items in a dataset based on their co-occurrence. 

# The algorithm operates on the principle of "apriori property," which states that if an itemset is frequent, then all of its subsets must also be frequent. 

# This property enables the algorithm to efficiently prune the search space by eliminating itemsets that do not meet the minimum support threshold. 

 

# The parameters used in the Apriori algorithm are: 

# - min_support: Minimum support threshold, indicating the minimum frequency of itemsets. 

# - min_confidence: Minimum confidence threshold for association rules. 

# - min_lift: Minimum lift threshold for association rules. 

# - min_length: Minimum number of items in an association rule. 

 

# Visualising the results 

 

## Displaying the first results coming directly from the output of the apriori function 

results = list(rules) 

results 

 

## Putting the results well organised into a Pandas DataFrame  

# Define a function to extract relevant information from the results 

 

def Am(results): 

    lhs         = [tuple(result[2][0][0])[0] for result in results] # Left-hand side of the rule 

    rhs         = [tuple(result[2][0][1])[0] for result in results] # Right-hand side of the rule 

    supports    = [result[1] for result in results] # Support of the rule 

    confidences = [result[2][0][2] for result in results]  # Confidence of the rule 

    lifts       = [result[2][0][3] for result in results] # Lift of the rule 

    return list(zip(lhs, rhs, supports, confidences, lifts)) 

resultsinDataFrame = pd.DataFrame(Am(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift']) 

 

## Displaying the full results sorted: 

resultsinDataFrame 

 

## Displaying the results sorted by relevence: 

resultsinDataFrame.head(5) 

 

resultsinDataFrame 

 

# Writing the results to a CSV file: 

resultsinDataFrame.to_csv("MBA_Analysis.csv",index=False) 