# This is my analysis of the iris dataset for the programming and scripting module project in ATU 2024.

# Author: Michael Curley

# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# View the first 10 rows
print(df.head(10))
