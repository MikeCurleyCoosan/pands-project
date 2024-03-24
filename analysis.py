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

        # Write a summary of the Sepal Length variable to the file
        file.write('\n')
        file.write("Summary of the Sepal Length Variable of the Dataset\n\n")
        #The describe() function applies basic statistical computations on the dataset like extreme values, 
        #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
        #describe() function gives a good picture of the distribution of data
        #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
        sepal_length_summary = df[["sepal_length", "species"]].groupby("species").describe()
        file.write(sepal_length_summary.to_string() + "\n\n")
        file.write("\n")
        file.write("****************************************************************************************************\n")

        # Write a summary of the Sepal Width variable to the file
        file.write('\n')
        file.write("Summary of the Sepal Width Variable of the Dataset\n\n")
        #The describe() function applies basic statistical computations on the dataset like extreme values, 
        #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
        #describe() function gives a good picture of the distribution of data
        #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
        sepal_width_summary = df[["sepal_width", "species"]].groupby("species").describe()
        file.write(sepal_width_summary.to_string() + "\n\n")
        file.write("\n")
        file.write("****************************************************************************************************\n")

        # Write a summary of the Petal Length variable to the file
        file.write('\n')
        file.write("Summary of the Petal Length Variable of the Dataset\n\n")
        #The describe() function applies basic statistical computations on the dataset like extreme values, 
        #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
        #describe() function gives a good picture of the distribution of data
        #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
        petal_length_summary = df[["petal_length", "species"]].groupby("species").describe()
        file.write(petal_length_summary.to_string() + "\n\n")
        file.write("\n")
        file.write("****************************************************************************************************\n")

        # Write a summary of the Petal Width to the file
        file.write('\n')
        file.write("Summary of the Petal Width Variable of the Dataset\n\n")
        #The describe() function applies basic statistical computations on the dataset like extreme values, 
        #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
        #describe() function gives a good picture of the distribution of data
        #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
        petal_width_summary = df[["petal_width", "species"]].groupby("species").describe()
        file.write(petal_width_summary.to_string() + "\n\n")
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

    #Our figure and axes are created using the subplots() function. 
    #The subplots() function returns an instance of the figure and an array of axes objects.
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

#Create a function to create a boxplot for each variable
def create_boxplot(df, variable): #The function takes in two parameters, the dataframe and the variable to create a boxplot for.

    #Create local variables for each species
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    #Create a list of colours to use for the boxplots
    colors = ['red', 'green', 'blue'] #The colours for the boxplots

    #Our figure and axes are created using the subplots() function. 
    #The subplots() function returns an instance of the figure and an array of axes objects.
    fig, ax = plt.subplots()

    #Create a boxplot for each variable on one plot. Therefore three boxplots will be created on the same plot.
    ax.boxplot(setosa[variable], positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
    #positions=[2] is used to position the boxplot on the x-axis
    #widths=1.5 is used to set the width of the boxplot
    #patch_artist=True is used to fill the boxplot with colour
    #labels=['setosa'] is used to label the boxplot
    #boxprops=dict(facecolor=colors[2], color='black') is used to set the colour of the boxplot

    #We have created a boxplot for setosa and now we need to create a boxplot for versicolor and virginica
    ax.boxplot(versicolor[variable], positions=[4], widths=1.5, patch_artist=True, labels=['versicolor'], boxprops=dict(facecolor=colors[1], color='black'))
    ax.boxplot(virginica[variable], positions=[6], widths=1.5, patch_artist=True, labels=['virginica'], boxprops=dict(facecolor=colors[0], color='black'))

    #Set the font for the x and y axis labels and the title 
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    #Add a title to the boxplot
    fig.suptitle("Boxplot of " + variable.capitalize().replace('_', ' '), fontdict=font1)

    #Variables to set the minimum and maximum values for the y-axis
    min = df[variable].min() - 0.2
    max = df[variable].max() + 0.2

    #Set the y-axis limits
    ax.set_ylim(min, max)

    #Add some padding to the subplots
    fig.tight_layout(pad=3.0) 

    #Set the x and y axis labels
    ax.set_xlabel("Species", fontdict=font2)
    ax.set_ylabel(variable.capitalize().replace('_', ' ') + " (cm)", fontdict=font2)

    #Add a grid
    ax.grid(linestyle='--', linewidth=0.5, color='black', alpha=0.4)


    #Save the plot as a .png file
    plt.savefig("Plots/" + variable + "_boxplot.png")

#Create a function to create a pairplot of the dataset without using the seaborn library
def create_pairplot(df):
    #Our figure and axes are created using the subplots() function. 
    #The subplots() function returns an instance of the figure and an array of axes objects.
    fig, ax = plt.subplots(2,2)

    #Add some padding to the subplots
    fig.tight_layout(pad=3.0) 

    #Create local variables for each species
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']
    #  Create a list of colours to use for the boxplots
    colors = ['red', 'green', 'blue'] #The colours for the boxplots

    x1_min = df['sepal_length'].min() - 0.2
    x1_max = df['sepal_length'].max() + 0.2
    y1_min = df['sepal_width'].min() - 0.2
    y1_max = df['sepal_width'].max() + 0.2

    ax[0,0].set_xlim(x1_min, x1_max)
    ax[0,0].set_ylim(y1_min, y1_max)

    x2_min = df['petal_length'].min() - 0.2
    x2_max = df['petal_length'].max() + 0.2
    y2_min = df['petal_width'].min() - 0.2
    y2_max = df['petal_width'].max() + 0.2

    ax[0,1].set_xlim(x2_min, x2_max)
    ax[0,1].set_ylim(y2_min, y2_max)

    x3_min = df['sepal_length'].min() - 0.2
    x3_max = df['sepal_length'].max() + 0.2
    y3_min = df['petal_length'].min() - 0.2
    y3_max = df['petal_length'].max() + 0.2

    ax[1,0].set_xlim(x3_min, x3_max)
    ax[1,0].set_ylim(y3_min, y3_max)

    x4_min = df['sepal_width'].min() - 0.2
    x4_max = df['sepal_width'].max() + 0.2
    y4_min = df['petal_width'].min() - 0.2
    y4_max = df['petal_width'].max() + 0.2

    ax[1,1].set_xlim(x4_min, x4_max)
    ax[1,1].set_ylim(y4_min, y4_max)


    #Create the pairplot for the dataset
    ax[0,0].scatter(setosa["sepal_length"], setosa["sepal_width"], label="Sepal Length vs Sepal Width", facecolor="blue") 
    #Create the scatter plot for sepal length vs sepal width
    ax[0,0].scatter(versicolor["sepal_length"], versicolor["sepal_width"], label="Sepal Length vs Sepal Width", facecolor="green")
    ax[0,0].scatter(virginica["sepal_length"], virginica["sepal_width"], label="Sepal Length vs Sepal Width", facecolor="red")

    ax[0,1].scatter(setosa["petal_length"], setosa["petal_width"], label="Petal Length vs Petal Width", facecolor="blue") 
    #Create the scatter plot for petal length vs petal width
    ax[0,1].scatter(versicolor["petal_length"], versicolor["petal_width"], label="Petal Length vs Petal Width", facecolor="green")
    ax[0,1].scatter(virginica["petal_length"], virginica["petal_width"], label="Petal Length vs Petal Width", facecolor="red")

    ax[1,0].scatter(setosa["sepal_length"], setosa["petal_length"], label="Sepal Length vs Petal Length", facecolor="blue") 
    #Create the scatter plot for sepal length vs petal length
    ax[1,0].scatter(versicolor["sepal_length"], versicolor["petal_length"], label="Sepal Length vs Petal Length", facecolor="green")
    ax[1,0].scatter(virginica["sepal_length"], virginica["petal_length"], label="Sepal Length vs Petal Length", facecolor="red")

    ax[1,1].scatter(setosa["sepal_width"], setosa["petal_width"], label="Sepal Width vs Petal Width", facecolor="blue")  
    #Create the scatter plot for sepal width vs petal width
    ax[1,1].scatter(versicolor["sepal_width"], versicolor["petal_width"], label="Sepal Width vs Petal Width", facecolor="green")
    ax[1,1].scatter(virginica["sepal_width"], virginica["petal_width"], label="Sepal Width vs Petal Width", facecolor="red")

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
    plt.savefig("Plots/pairplot.png")

def create_correlation_matrix(df):

    #Create a correlation matrix for the dataset
    df_corr = df.drop(columns='species') # Drop the species column as it is not needed for the correlation matrix

    CORRELATION = df_corr.corr()
    with open("Correlation/correlations.txt", 'w') as f:

        #Write the correlation matrix to the file
        f.write("Correlation Matrix of the Iris Dataset\n")
        f.write("\n") #Add a new line to the file
        f.write("****************************************************************************************************\n")
        f.write("\n")
        f.write(CORRELATION.to_string() + "\n\n")  #The correlation matrix of the dataset
        f.write("\n")
        f.write("****************************************************************************************************\n")
        f.write("\n")
        f.write("The correlation matrix shows the correlation between each variable in the dataset.\n")
        f.write("The correlation coefficient ranges from -1 to 1. If the value is close to 1,\n")
        f.write("it means that there is a strong positive correlation between the two variables.\n")
        f.write("If the value is close to -1, it means that there is a strong negative correlation between the two variables.\n")
        f.write("If the value is close to 0, it means that there is no correlation between the two variables.\n")

    #Create a heatmap of the correlation matrix
    fig, ax = plt.subplots() # Create a figure and axis

    corr_map = sns.heatmap(CORRELATION, annot=True, cmap='coolwarm') # Create a heatmap of the correlation matrix
    #cmap is used to set the colour map for the heatmap
    # fixed an initial issue where axis labels were being cut off: 
    #https://stackoverflow.com/questions/33660420/seaborn-ticklabels-are-being-truncated 
    plt.savefig('Correlation/correlation_heatmap.png') # Save the heatmap as a .png file



       
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

#Create a pairplot of the dataset
create_pairplot(df)

#Create a correlation matrix for the dataset
create_correlation_matrix(df)

#Future work: Thinking out loud.......
#1. Summary.txt file.....Research and see if anything else should be included in the summary of the dataset?? Examples. skewness, kurtosis, etc.
#2. Define a function to create a violin plot for each variable.....
#3. Define a function to create a swarm plot for each variable.....
#4  Flesh out each of the plots to include more details and add to README.md file
#5. Create a function to create a scatter plot matrix using the seaborn library.....have seen this online and it looks great.
#6. Create a function to create a pairplot using the seaborn library.....

#References:
