# This is my analysis of the iris dataset for the programming and scripting module project in ATU 2024.

# Author: Michael Curley

# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset. The dataset used in this project is taken from the UCI website. https://archive.ics.uci.edu/dataset/53/iris
#The dataset contained no headers so I added them in the names parameter. Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])


# View the first 10 rows
print(df.head(10))

# Print a sumamary of the dataset
print(df.describe())

#Checking missing values
print(df.isnull().sum())

#Checking for duplicates. df.drop_duplicates() will remove all duplicates from the dataset
data = df.drop_duplicates(subset='species',)
print(data)

#Checking the group size of each species
print(df.groupby('species').size())

#plotting the dataset. Firstly create variables for each species and store the data in them. Here we are storing 
#the data for each species in a separate variable. 
setosa = df[df.species == "Iris-setosa"]
versicolor = df[df.species=='Iris-versicolor']
virginica = df[df.species=='Iris-virginica']

fig, ax = plt.subplots()

# lables and scatter points. We are plotting three scatter plots on the same graph. Each scatter plot represents a species.
ax.scatter(setosa['petal_length'], setosa['petal_width'], label="Setosa", facecolor="blue")
ax.scatter(versicolor['petal_length'], versicolor['petal_width'], label="Versicolor", facecolor="green")
ax.scatter(virginica['petal_length'], virginica['petal_width'], label="Virginica", facecolor="red")

#Set th Axis lables
ax.set_xlabel("petal length (cm)")
ax.set_ylabel("petal width (cm)")
#Add a grid
ax.grid()
#Add a title
ax.set_title("Iris petals")
#Add a legend
ax.legend()

#Set your x and y axis limits
ax.set_xlim(0, 8)
ax.set_ylim(0, 3)

plt.show()

#Final version of the code to create a histogram for each variable for each species on the same plot
#Create a function to create histograms for each variable
def create_histogram(df, variable): #The function takes in two parameters, the dataframe and the variable to create the histogram foran
    #Using the dataframe we can create local variable for each species
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    #The stateful approach to creating a histogram as recommended by real python website
    #https://realpython.com/python-histograms/ 
    fig, ax = plt.subplots()

    #Create the histogram for the same variable for each species on the one plot. Therefore three histograms will be 
    #created on the same plot.
    ax.hist(setosa[variable], bins=10, label="Setosa", color="blue", alpha=0.5)
    ax.hist(versicolor[variable], bins=10, label="Versicolor", color="green", alpha=0.5)
    ax.hist(virginica[variable], bins=10, label="Virginica", color="red", alpha=0.5)

    #Set the x and y axis labels
    ax.set_xlabel(variable)
    ax.set_ylabel("Frequency")
    
    #Add a title
    ax.set_title(variable)

    #Add a legend
    ax.legend()

    #Save the plot as a .png file
    plt.savefig(variable + "_histogram.png")

#Main program
#Call the function to create histograms for each variable
create_histogram(df, "sepal_length")
create_histogram(df, "sepal_width")
create_histogram(df, "petal_length")
create_histogram(df, "petal_width")










