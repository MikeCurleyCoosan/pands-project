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
        file.write("\n") #Add a new line to the file
        #
        file.write("****************************************************************************************************\n")

        #Write the first 10 rows of the dataset to the file
        file.write('\n')
        file.write("First 10 rows of the dataset\n\n")
        #https://www.grepper.com/answers/242389/dataframe+to+txt
        file.write(df.head(10).to_string() + "\n")  #The first 10 rows of the dataset
        file.write("\n")

        file.write("****************************************************************************************************\n")

        # Write a summary of the dataset to the file
        file.write('\n')
        file.write("Summary of the dataset\n\n")
        #The describe() function applies basic statistical computations on the dataset like extreme values, 
        #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
        #describe() function gives a good picture of the distribution of data
        #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
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
    #Using the dataframe we can create local variable for each species, therefore we can amalgamate each species onto our histogram in different colours
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    #The stateless approach to creating a histogram as recommended by real python website
    #https://realpython.com/python-matplotlib-guide/
    #https://realpython.com/python-histograms/ 
    fig, ax = plt.subplots()

    #Create the histogram for the same variable for each species on the one plot. Therefore three histograms will be 
    #created on the same plot.
    ax.hist(setosa[variable], bins=10, label="Setosa", color="blue", alpha=0.5, edgecolor='black') #The alpha parameter is used to make the bars transparent
    ax.hist(versicolor[variable], bins=10, label="Versicolor", color="green", alpha=0.5, edgecolor='black')
    ax.hist(virginica[variable], bins=10, label="Virginica", color="red", alpha=0.5, edgecolor='black')

    #Set the font for the x and y axis labels and the title (https://www.w3schools.com/python/matplotlib_labels.asp)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    #Set the x and y axis labels
    ax.set_xlabel(variable.capitalize().replace('_', ' '), fontdict=font2)
    ax.set_ylabel("Frequency", fontdict=font2)
    
    #Add a title
    ax.set_title(variable.capitalize().replace('_', ' '), fontdict=font1)

    #Add a legend
    ax.legend()

    #Save the plot as a .png file
    plt.savefig("Plots/" + variable + "_histogram.png")

#todo: Try and figure out how to take in values for the x and y scale for the scatter plot function....


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

    #Set the font for the x and y axis labels and the title (https://www.w3schools.com/python/matplotlib_labels.asp)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    #Set the x and y axis labels
    ax.set_xlabel(x.capitalize().replace('_', ' ')+ " (cm)", fontdict=font2)
    ax.set_ylabel(y.capitalize().replace('_', ' ') + " (cm)", fontdict=font2)

    #Add a grid
    ax.grid()

    #Add a title
    ax.set_title("Iris " + x.capitalize().replace('_', ' ') + " vs " + y.capitalize().replace('_', ' '), fontdict=font1)

    #Add a legend
    ax.legend()

    #Save the plot as a .png file
    plt.savefig("Plots/" + x + "_vs_" + y + "_scatter.png")
'''
def create_boxplot(df, variable): #The function takes in two parameters, the dataframe and the variable to create the boxplot for

    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    colors = ['red', 'green', 'blue'] #The colours for the boxplots

    #The stateless approach to creating a boxplot as recommended by real python website
    fig, ax = plt.subplots(1,3)

    #Create the boxplot for the variable for each species on the one plot. Therefore three boxplots will be
    #created on the same plot.
    ax[0].boxplot(setosa[variable], patch_artist=True, labels=['setosa'], boxprops=dict(color=colors[0]))
    ax[1].boxplot(versicolor[variable], patch_artist=True, labels=['versicolor'], boxprops=dict(color=colors[1]))
    ax[2].boxplot(virginica[variable], patch_artist=True, labels=['virginica'], boxprops=dict(color=colors[2]))

    #Set the font for the x and y axis labels and the title (https://www.w3schools.com/python/matplotlib_labels.asp)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    fig.suptitle("Boxplot of " + variable.capitalize().replace('_', ' '), fontdict=font1)

    min = df[variable].min() - 0.2
    max = df[variable].max() + 0.2

    ax[0].set_ylim(min, max)
    ax[1].set_ylim(min, max)
    ax[2].set_ylim(min, max)

    fig.tight_layout(pad=3.0) #Add some padding to the subplots

    #Save the plot as a .png file
    plt.savefig("Plots/" + variable + "_boxplot.png")
'''
def create_boxplot(df, variable): #The function takes in two parameters, the dataframe and the variable to

    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    colors = ['red', 'green', 'blue'] #The colours for the boxplots

    #The stateless approach to creating a boxplot as recommended by real python website
    fig, ax = plt.subplots()

    #Create the boxplot for the variable for each species on the one plot. Therefore three boxplots will b
    #created on the same plot.
    ax.boxplot(setosa[variable], positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
    ax.boxplot(versicolor[variable], positions=[4], widths=1.5, patch_artist=True, labels=['versicolor'], boxprops=dict(facecolor=colors[1], color='black'))
    ax.boxplot(virginica[variable], positions=[6], widths=1.5, patch_artist=True, labels=['virginica'], boxprops=dict(facecolor=colors[0], color='black'))

    #Set the font for the x and y axis labels and the title 
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    fig.suptitle("Boxplot of " + variable.capitalize().replace('_', ' '), fontdict=font1)

    min = df[variable].min() - 0.2
    max = df[variable].max() + 0.2

    ax.set_ylim(min, max)

    fig.tight_layout(pad=3.0) #Add some padding to the subplots

    #Save the plot as a .png file
    plt.savefig("Plots/" + variable + "_boxplot.png")

#Create a function to create a pairplot of the dataset without using the seaborn library
def create_pairplot(df):
    #The stateless approach to creating a pairplot as recommended by real python website
    #https://realpython.com/python-matplotlib-guide/
    #https://realpython.com/python-histograms/
    fig, ax = plt.subplots(2,2)

    fig.tight_layout(pad=3.0) #Add some padding to the subplots

    #Create the pairplot for the dataset
    ax[0,0].scatter(df["sepal_length"], df["sepal_width"], label="Sepal Length vs Sepal Width", facecolor="blue") #Create the scatter plot for sepal length vs sepal width
    ax[0,1].scatter(df["petal_length"], df["petal_width"], label="Petal Length vs Petal Width", facecolor="green") #Create the scatter plot for petal length vs petal width
    ax[1,0].scatter(df["sepal_length"], df["petal_length"], label="Sepal Length vs Petal Length", facecolor="red") #Create the scatter plot for sepal length vs petal length
    ax[1,1].scatter(df["sepal_width"], df["petal_width"], label="Sepal Width vs Petal Width", facecolor="yellow")  #Create the scatter plot for sepal width vs petal width

    #Set the x and y axis labels
    ax[0,0].set_xlabel("Sepal Length (cm)") #Set the x axis label for the first subplot
    ax[0,0].set_ylabel("Sepal Width (cm)") #Set the y axis label for the first subplot

    ax[0,1].set_xlabel("Petal Length (cm)") #Set the x axis label for the second subplot
    ax[0,1].set_ylabel("Petal Width (cm)") #Set the y axis label for the second subplot

    ax[1,0].set_xlabel("Sepal Length (cm)") #Set the x axis label for the third subplot
    ax[1,0].set_ylabel("Petal Length (cm)") #Set the y axis label for the third subplot

    ax[1,1].set_xlabel("Sepal Width (cm)") #Set the x axis label for the fourth subplot
    ax[1,1].set_ylabel("Petal Width (cm)") #Set the y axis label for the fourth subplot


    #Add a grid
    ax[0,0].grid() #Add a grid to the first subplot
    ax[0,1].grid() #Add a grid to the second subplot
    ax[1,0].grid() #Add a grid to the third subplot
    ax[1,1].grid() #Add a grid to the fourth subplot

    #Add a title
    ax[0,0].set_title("Sepal Length vs Sepal Width") #Add a title to the first subplot
    ax[0,1].set_title("Petal Length vs Petal Width") #Add a title to the second subplot
    ax[1,0].set_title("Sepal Length vs Petal Length") #Add a title to the third subplot
    ax[1,1].set_title("Sepal Width vs Petal Width") #Add a title to the fourth subplot

    #Save the plot as a .png file
    plt.savefig("pairplot.png")
   
def get_variables(df):
    #Get the variables in the dataset
    variables = df.columns.to_numpy()
    variables = np.delete(variables, 4) #Remove the species variable from the list of variables
    return variables

#Main program
#Call the function to create the summary of the dataset
create_summary(df, FILENAME)

#Create a histogram for each variable
#Get the variables in the dataset
my_var = get_variables(df)
#Loop through the variables and call the function to create a histogram for each variable
for variable in my_var:
    create_histogram(df, variable)
    create_boxplot(df, variable)

#Create a scatter-plot for each pair of variables  
#Get the variables in the dataset
my_var = get_variables(df)  
#Loop through the variables and call the function to create a scatter plot for each pair of variables
for i in range(len(my_var)):
    for j in range(i+1, len(my_var)):
        create_scatter_plot(df, my_var[j], my_var[i])








#Future work: Thinking out loud.......
#1. Summary.txt file.....Research and see if anything else should be included in the summary of the dataset?? Examples. skewness, kurtosis, etc.
#2. Pairplot function......update the function to put the species in different colours on the subplots??
#3. Define a function to create a boxplot for each variable.....can this be done using the same approach as the histogram function?
#4. Define a function to create a correlation matrix for the dataset....
#5. Define a function to create a heatmap of the correlation matrix.....
#6. Define a function to create a violin plot for each variable.....

#Have come across the above named plots and matrices but not sure how to use them yet, or what they are for. Will look into them further.

#References:
