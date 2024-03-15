# This is my analysis of the iris dataset for the programming and scripting module project in ATU 2024.

# Author: Michael Curley

# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
#The dataset contained no headers so I added them in the names parameter. Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])


# View the first 10 rows
print(df.head(10))

# Print a sumamary of the dataset
print(df.describe())
