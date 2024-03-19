# This is my analysis of the iris dataset for the programming and scripting module project in ATU 2024.

# Author: Michael Curley

# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Create a variable to store the name of the file to write the summary of the dataset too. 
#Capital letters are used to indicate that this is a constant and should not be changed.
FILENAME = "summary.txt"

#Load the iris dataset. The dataset used in this project is taken from the UCI website. https://archive.ics.uci.edu/dataset/53/iris
#The dataset contained no headers so I added them in the names parameter. Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Create a function to display a summary of the dataset into a file called summary.txt
def create_summary(df, FILENAME): #The function takes in two parameters, the dataframe and the name of the file to write the summary to.
    FILENAME = "summary.txt"

    #Create a file called summary.text and have the file ready to write to. If the file already exists it will be overwritten.
    with open('summary.txt', 'w') as file:

        #Write the first line to the file
        file.write("Summary of the Iris Dataset\n")
        file.write("\n")

        file.write("****************************************************************************************************\n")

        #Write the first 10 rows of the dataset to the file
        file.write('\n')
        file.write("First 10 rows of the dataset\n\n")
        file.write(df.head(10).to_string() + "\n")  #The first 10 rows of the dataset
        file.write("\n")

        file.write("****************************************************************************************************\n")

        # Write a summary of the dataset to the file
        file.write('\n')
        file.write("Summary of the dataset\n\n")
        file.write(df.describe().to_string() + "\n")  #The summary of the dataset
        file.write("\n")


        file.write("****************************************************************************************************\n")

        #Write the number of rows and columns in the dataset to the file
        file.write('\n')
        file.write("Number of rows and columns in the dataset\n\n")
        rows_columns = df.shape #The number of rows and columns in the dataset
        file.write("Number of rows: " + str(rows_columns[0]) + "\n")  #The number of rows in the dataset
        file.write("Number of columns: " + str(rows_columns[1]) + "\n")  #The number of columns in the dataset
        file.write("\n")

        file.write("****************************************************************************************************\n")
    
        #Write the number of missing values in the dataset to the file
        file.write('\n')
        file.write("Number of missing values in the dataset\n\n")
        file.write(df.isnull().sum().to_string() + "\n")  #The number of missing values in the dataset
        file.write("\n")


        file.write("****************************************************************************************************\n")

        #Write the number of duplicates in the dataset to the file
        file.write('\n')
        file.write("Number of duplicates in the dataset\n")
        file.write(str(df.duplicated().sum()) + "\n")  #The number of duplicates in the dataset
        file.write("\n")

        file.write("****************************************************************************************************\n")

        #Write the number of unique values in the dataset to the file
        file.write('\n')
        file.write("Number of unique values in the dataset\n")
        file.write(df.nunique().to_string() + "\n")  #The number of unique values in the dataset
        file.write("\n")

        file.write("****************************************************************************************************\n")

        #Checking the group size of each species
        file.write('\n')
        file.write("Group size of each species\n")
        file.write(df.groupby('species').size().to_string() + "\n")  #The group size of each species
        file.write("\n")

        file.write("****************************************************************************************************\n")

#Final version of the code to create a histogram for each variable for each species on the same plot
#Create a function to create histograms for each variable
def create_histogram(df, variable): #The function takes in two parameters, the dataframe and the variable to create the histogram foran
    #Using the dataframe we can create local variable for each species
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    #The stateless approach to creating a histogram as recommended by real python website
    #https://realpython.com/python-matplotlib-guide/
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

#Use same approach as above to create a scatter plot for each pair of variables. Therefore we create a function to create the scatter plots
def create_scatter_plot(df, x, y): #The function takes in three parameters, the dataframe and the two variables to create the scatter plot for

    #Create local variables for each species
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    #The stateless approach to creating a scatter plot as recommended by real python website
    #https://realpython.com/python-matplotlib-guide/
    #https://realpython.com/python-histograms/
    fig, ax = plt.subplots()

    #Create the scatter plot for the two variables for each species on the one plot. Therefore three scatter plots will be
    #created on the same plot.
    ax.scatter(setosa[x], setosa[y], label="Setosa", facecolor="blue")
    ax.scatter(versicolor[x], versicolor[y], label="Versicolor", facecolor="green")
    ax.scatter(virginica[x], virginica[y], label="Virginica", facecolor="red")

    #Set the x and y axis labels
    ax.set_xlabel(x + " (cm)")
    ax.set_ylabel(y + " (cm)")

    #Add a grid
    ax.grid()

    #Add a title
    ax.set_title("Iris " + x + " vs " + y)

    #Add a legend
    ax.legend()

    #Save the plot as a .png file
    plt.savefig(x + "_vs_" + y + "_scatter.png")

#Create a function to create a pairplot of the dataset without using the seaborn library
def create_pairplot(df):
    #The stateless approach to creating a pairplot as recommended by real python website
    #https://realpython.com/python-matplotlib-guide/
    #https://realpython.com/python-histograms/
    fig, ax = plt.subplots()

    #Create the pairplot for the dataset
    ax.scatter(df['sepal_length'], df['sepal_width'], label="Sepal Length vs Sepal Width", facecolor="blue")
    ax.scatter(df['petal_length'], df['petal_width'], label="Petal Length vs Petal Width", facecolor="green")
    ax.scatter(df['sepal_length'], df['petal_length'], label="Sepal Length vs Petal Length", facecolor="red")
    ax.scatter(df['sepal_width'], df['petal_width'], label="Sepal Width vs Petal Width", facecolor="yellow")

    #Set the x and y axis labels
    ax.set_xlabel("Sepal Length (cm)")
    ax.set_ylabel("Sepal Width (cm)")
    ax.set_xlabel("Petal Length (cm)")
    ax.set_ylabel("Petal Width (cm)")
    ax.set_xlabel("Sepal Length (cm)")
    ax.set_ylabel("Petal Length (cm)")
    ax.set_xlabel("Sepal Width (cm)")
    ax.set_ylabel("Petal Width (cm)")

    #Add a grid
    ax.grid()

    #Add a title
    ax.set_title("Iris Pairplot")

    #Add a legend
    ax.legend()

    #Save the plot as a .png file
    plt.savefig("pairplot.png")



#Main program
#Call the function to create histograms for each variable.......May be a more efficient way to do this.....come back to it later.
#(Look to see if you can call the function in a loop or something.....)



create_summary(df, FILENAME)
create_histogram(df, "sepal_length")
create_histogram(df, "sepal_width")
create_histogram(df, "petal_length")
create_histogram(df, "petal_width")
create_scatter_plot(df, "sepal_length", "sepal_width")
create_scatter_plot(df, "petal_length", "petal_width")
create_scatter_plot(df, "sepal_length", "petal_length")
create_scatter_plot(df, "sepal_width", "petal_width")
create_pairplot(df)

#Future work: Thinking out loud.......
#1. Define a function to create a summary of each variable to a .txt file....what data should be included in the summary?
#2. Define a function to create a pairplot of the dataset......may be a bit ambitious for me at the moment
#3. Define a function to create a boxplot for each variable.....can this be done using the same approach as the histogram function?
#4. Define a function to create a correlation matrix for the dataset....
#5. Define a function to create a heatmap of the correlation matrix.....
#6. Define a function to create a violin plot for each variable.....

#Have come across the above named plots and matrices but not sure how to use them yet, or what they are for. Will look into them further.














