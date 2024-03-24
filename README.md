#### pands-project

# Project for the Programming and Scripting Module 2024

## **by Michael Curley**

![Iris Data Set](Images/iris_image.png)


<a target="_blank" href="https://docs.python.org/3/tutorial/index.html">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
</a>
<a target="_blank" href="https://www.anaconda.com/">
  <img src="https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white" alt="Anaconda"/>
</a>
<a target="_blank" href="https://numpy.org/devdocs/index.html">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
</a>
<a target="_blank" href="https://pypi.org/project/pandas/">
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
</a>
<a target="_blank" href="https://matplotlib.org/">
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib"/>
</a>
<a target="_blank" href="https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">
  <img src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown"/>
</a>
<a target="_blank" href="https://www.latex-project.org/">
  <img src="https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX"/>
</a>
<a target="_blank" href="https://code.visualstudio.com/">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="Visual Studio Code"/>
</a>
<a target="_blank" href="https://jupyter.org/">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook"/>
</a>

-----

_This README has being written with [GitHub's Documentation on README's](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind. You should refer to that documentation for more information on writing an appropriate README for visitors to your 
repository._

_You can find out more about writing in MarkDown in [GitHub Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)_

-----


## Table of Contents.

* [About this project](#about-this-project)
* [Use of this project](#use-of-this-project)
* [Get Started](#get-started)
* [Get Help](#get-help)
* [Contribute](#contribute)
* [Author](#author)

## ***1.0 About this project***

This repository contains the Iris Fisher dataset and Python code for analysing it using a variety of Python software modules such as [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/). This project was undertaken as part of the 'Programming and Scripting' module in the Higher Diploma in Data Analytics in ATU, Galway in the year 2024.

As per the project requirements, the project [README](https://github.com/MikeCurleyCoosan/pands-project/blob/main/README.md) contains an overview of the project, my 
research into the Iris dataset, visualisations of the Iris datasets generated by running python scripts, detailed explanations and discussion as 
well as a list of all references used.The Python script containing the Python code used to investigate the Iris dataset is called  [analysis.py](https://github.com/MikeCurleyCoosan/pands-project/blob/main/analysis.py).

### ***1.1 About the Iris Fisher dataset***

The Iris Fisher dataset is a very popular dataset for data analysis and visualization tasks. It is also known as the Iris Flower dataset and consists of different attribute information for three differen classes of the Iris species. The dataset is quite small, consisting of 50 samples of each of the three different classes, to give a total of 150 instances in total. For each instance the different attributes that were taken were as follows, given below as dataset columns.

#### ***1.1.1 Dataset Columns***

- **sepal_length**: The sepal length for each instance, in cms.
- **sepal_width**: The sepal width for each instance, in cms.
- **petal_length**: The petal length for each instance in cms.
- **petal_width**: The petal width for each instance in cms.
- **species**: Iris species (Iris setosa, Iris versicolor, and Iris virginica).

The data was collected in the Gaspé Peninsula in Canada by botanist Edgar Anderson, and famously used by statistician Ronald Fisher in his 1936 paper ["The Use of Multiple Measurements in Taxonomic Problems"](https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x) to demonstrate how classification can be gauged by statistics. He argues that, due to some significant attribute differences between the species in this dataset, Iris group membership could potentially be determined by sepal and petal measurements - a method that would become known as [linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis#:~:text=Linear%20discriminant%20analysis%20(LDA)%2C,classes%20of%20objects%20or%20events.). 

## ***2.0 Project Tasks***

### ***2.1 Generate a summary of each variable to a single text file***

The first task of the project was to write a program called [analysis.py](https://github.com/MikeCurleyCoosan/pands-project/blob/main/analysis.py) that outputs a summary of each variable to a single text file. In order to achieve this we create a function in the analysis.py script called create_summary. This function takes in two variables, the dataframe, and the name of the file that the summary is to be written to. When the function is called it then genetates the summary.txt file which stores this information. The function is called by using the python text below

```python

create_summary(df, FILENAME)

```
We use the with open function as below to check if a file with the filename summary.txt exists. If this file already exists it is overwritten each time the analysis.py script is run, or if we choose to do so each time the create_summary function is run within that script. 

```python
with open('summary.txt', 'w') as file:
```



#### <b id="">Summary statistics of dataset</b>

|       | sepal length in cm | sepal width in cm | petal length in cm | petal width in cm |
|-------|--------------------|-------------------|--------------------|-------------------|
| count | 150.000000         | 150.000000        | 150.000000         | 150.000000        |
| mean  | 5.843333           | 3.054000          | 3.758667           | 1.198667          |
| std   | 0.828066           | 0.433594          | 1.764420           | 0.763161          |
| min   | 4.300000           | 2.000000          | 1.000000           | 0.100000          |
| 25%   | 5.100000           | 2.800000          | 1.600000           | 0.300000          |
| 50%   | 5.800000           | 3.000000          | 4.350000           | 1.300000          |
| 75%   | 6.400000           | 3.300000          | 5.100000           | 1.800000          |
| max   | 7.900000           | 4.400000          | 6.900000           | 2.500000          |


#### <b id="">Sepal Length in cm</b>
|                 | count | mean  | std      | min | 25%   | 50% | 75% | max |
|-----------------|-------|-------|----------|-----|-------|-----|-----|-----|
| species         |       |       |          |     |       |     |     |     |
| *Iris-setosa*     | 50.0  | 5.006 | 0.352490 | 4.3 | 4.800 | 5.0 | 5.2 | 5.8 |
| *Iris-versicolor* | 50.0  | 5.936 | 0.516171 | 4.9 | 5.600 | 5.9 | 6.3 | 7.0 |
| *Iris-virginica*  | 50.0  | 6.588 | 0.635880 | 4.9 | 6.225 | 6.5 | 6.9 | 7.9 |

#### <b id="">Sepal Width in cm</b>
|                 | count | mean  | std      | min | 25%   | 50% | 75%   | max |
|-----------------|-------|-------|----------|-----|-------|-----|-------|-----|
| species         |       |       |          |     |       |     |       |     |
| *Iris-setosa*     | 50.0  | 3.418 | 0.381024 | 2.3 | 3.125 | 3.4 | 3.675 | 4.4 |
| *Iris-versicolor* | 50.0  | 2.770 | 0.313798 | 2.0 | 2.525 | 2.8 | 3.000 | 3.4 |
| *Iris-virginica*  | 50.0  | 2.974 | 0.322497 | 2.2 | 2.800 | 3.0 | 3.175 | 3.8 |

#### <b id="">Petal Length in cm</b>
|                 | count | mean  | std      | min | 25% | 50%  | 75%   | max |
|-----------------|-------|-------|----------|-----|-----|------|-------|-----|
| species         |       |       |          |     |     |      |       |     |
| *Iris-setosa*     | 50.0  | 1.464 | 0.173511 | 1.0 | 1.4 | 1.50 | 1.575 | 1.9 |
| *Iris-versicolor* | 50.0  | 4.260 | 0.469911 | 3.0 | 4.0 | 4.35 | 4.600 | 5.1 |
| *Iris-virginica*  | 50.0  | 5.552 | 0.551895 | 4.5 | 5.1 | 5.55 | 5.875 | 6.9 |

#### <b id="">Petal Width in cm</b>
|                 | count | mean  | std      | min | 25% | 50% | 75% | max |
|-----------------|-------|-------|----------|-----|-----|-----|-----|-----|
| species         |       |       |          |     |     |     |     |     |
| *Iris-setosa*     | 50.0  | 0.244 | 0.107210 | 0.1 | 0.2 | 0.2 | 0.3 | 0.6 |
| *Iris-versicolor* | 50.0  | 1.326 | 0.197753 | 1.0 | 1.2 | 1.3 | 1.5 | 1.8 |
| *Iris-virginica*  | 50.0  | 2.026 | 0.274650 | 1.4 | 1.8 | 2.0 | 2.3 | 2.5 |


From above tables, we can conclude that there is a lot of overlap in sepal length and width between all species. Iris setosa typically has a smaller sepal length, than Iris versicolor and Iris virginica. We can also see that Iris setosa has wider sepals than the other two species. The biggest difference between species can be seen in the petal length, with Iris setosa having much shorter petals than Iris versicolor, and Iris virginica having the longest. 

From the overall table we could see that the standard deviation for petal length was relatively high, but now when the samples are separated by species, the standard deviation is smaller for each. We can conclude from this that there is a large difference between the species types, which skewed the values in the overall table. The pattern is similar for petal width, with Iris setosa being the narrowest and Iris virginica being the widest, but this difference is not as large as it is for petal length.

### ***2.2 Generate a histogram of each variable***

Histograms are used to represent the frequency of a particular variable in a dataset. A function called create_histogram has been written to generate four histograms - one for each of the four measured variables. This function takes in two parameters, the dataframe and the variable you wish to create a histogram for. The same function can then be re-used to create all other histograms by just changing the variable we are passing into it.

```python

def create_histogram(df, variable): 
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']
    fig, ax = plt.subplots()
    ax.hist(setosa[variable], bins=10, label="Setosa", color="blue", alpha=0.5, e
    ax.hist(versicolor[variable], bins=10, label="Versicolor", color="green", alp
    ax.hist(virginica[variable], bins=10, label="Virginica", color="red", alpha=0
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    ax.set_xlabel(variable.capitalize().replace('_', ' '), fontdict=font2)
    ax.set_ylabel("Frequency", fontdict=font2)
    ax.set_title(variable.capitalize().replace('_', ' '), fontdict=font1)
    ax.legend()
    plt.savefig("Plots/" + variable + "_histogram.png")

```

#### <b id="">Sepal Length Histogram</b>
![Sepal Length](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/sepal_length_histogram.png)

#### <b id="">Sepal Width Histogram</b>
![Sepal Width](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/sepal_width_histogram.png)

#### <b id="">Petal Length Histogram</b>
![Petal Length](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/petal_length_histogram.png)

#### <b id="">Petal Width Histogram</b>
![Petal Width](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/petal_width_histogram.png)


While the summary tables when separated by species gave us useful information, plotting this information graphically can tell us about these findings faster than looking 
through a table of numbers. Many of the conclusions mentioned above after looking at the summary tables can be seen at a glance using histograms. For example, we can see 
how the petals of *Iris setosa* are all smaller than *Iris versicolor* and *Iris virginica*, and how there is a lot of overlap between all three species when looking at 
their sepal width. If we were shown three *Iris* flowers at random that were measured for this dataset, one from each species, and tasked with determining what species each 
flower was, we could be 100% confident in identifying the *Iris setosa* flower by its petal size alone. It would also be reasonable to assume the flower with the largest 
petals is an *Iris virginica*, but we would be less confident in this answer due to the slight overlap between the petal sizes of *Iris versicolor* and *Iris virginica* 
among some of the measured samples.
 
The summary tables and histograms complement each other well - the histogram to quickly see patterns in the data, and the tables for precise measurements of the summaries.


### ***2.3 Generate a scatter plot of each set of variables***

Scatter plots are used for multivariate analysis and allow us to look at the relationship between two variables at a time. A function called create_scatter_plot has been written to generate the six scatter plots required to plot all combination of variables in a dataset with 4 distinct variables such as the iris dataset - one for each of the two pairs of variables. This function takes in three parameters, the dataframe and the x and y variables you wish to create your scatter plot for. The same function can then be re-used to create all other scatter plots by just changing the variable we are passing into it.

```python
def create_scatter_plot(df, x, y): 
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']
    fig, ax = plt.subplots()
    ax.scatter(setosa[x], setosa[y], label="Setosa", facecolor="blue")
    ax.scatter(versicolor[x], versicolor[y], label="Versicolor", facecolor="green")
    ax.scatter(virginica[x], virginica[y], label="Virginica", facecolor="red")
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15
    ax.set_xlabel(x.capitalize().replace('_', ' ')+ " (cm)", fontdict=font2)
    ax.set_ylabel(y.capitalize().replace('_', ' ') + " (cm)", fontdict=font2)
    ax.grid()
    ax.set_title("Iris " + x.capitalize().replace('_', ' ') + " vs " + y.capitalize().replace('_', ' '), fontdict=font1)
    ax.legend()
    plt.savefig("Plots/" + x + "_vs_" + y + "_scatter.png")

```

#### <b id="">Sepal Width vs Sepal Length Scatter Plot</b>
![Sepal Width vs Sepal Length](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/sepal_width_vs_sepal_length_scatter.png)

#### <b id="">Petal Width vs Petal Length Scatter Plot</b>
![Petal Width vs Petal Length](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/petal_width_vs_petal_length_scatter.png)


#### <b id="">Petal Length vs Sepal Length Scatter Plot</b>
![Petal Length vs Sepal Length](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/petal_length_vs_sepal_length_scatter.png)


#### <b id="">Petal Length vs Sepal Width Scatter Plot</b>
![Petal Length vs Sepal Width](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/petal_length_vs_sepal_width_scatter.png)


#### <b id="">Petal Width vs Sepal length Scatter Plot</b>
![Petal Width vs Sepal Length](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/petal_width_vs_sepal_length_scatter.png)

#### <b id="">Petal Width vs Sepal Width Scatter Plot</b>
![Petal Width vs Sepal Width](https://github.com/MikeCurleyCoosan/pands-project/blob/main/Plots/petal_width_vs_sepal_width_scatter.png)

### ***2.4 Other Appropriate Analysis***

#### ***2.4.1 Box plot***

Another useful plot type for analysing data is the [boxplots](https://builtin.com/data-science/boxplot). It gives us the quartile ranges of the data, while also indicating if the data is skewed and if there are any outliers.

![Boxplot](Images/Box.png)

As above, the box itself shows the range of values that lie between the 25% and 75% range, with the line within the box indicating the median. The lines extending outwards from the box are called whiskers, which show the rest of the data except for the outliers, indicated by a symbol beyond the whiskers. Outliers are data points that deviate so far from the norm that they may negatively influence the rest of the analysis. A function called create_boxplot has been written to generate a boxplot for each of the four measured variables. This function takes in two parameters, the dataframe and the variable you wish to create the boxplot for. The same function can 
then be re-used to create all other boxplots by just changing the variable we are passing into it.


```python
def create_boxplot(df, variable): 
  
   setosa = df[df.species == "Iris-setosa"]
   versicolor = df[df.species=='Iris-versicolor']
   virginica = df[df.species=='Iris-virginica']
   colors = ['red', 'green', 'blue']
   fig, ax = plt.subplots()
   ax.boxplot(setosa[variable], positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
   ax.boxplot(versicolor[variable], positions=[4], widths=1.5, patch_artist=True, labels=['versicolor'], boxprops=dict(facecolor=colors[1], color='black'))
   ax.boxplot(virginica[variable], positions=[6], widths=1.5, patch_artist=True, labels=['virginica'], boxprops=dict(facecolor=colors[0], color='black'))
   font1 = {'family':'serif','color':'blue','size':20}
   font2 = {'family':'serif','color':'darkred','size':15}
   fig.suptitle("Boxplot of " + variable.capitalize().replace('_', ' '), fontdict=font1)
   min = df[variable].min() - 0.2
   max = df[variable].max() + 0.2
   ax.set_ylim(min, max)
   fig.tight_layout(pad=3.0) 
   ax.set_xlabel("Species", fontdict=font2)
   ax.set_ylabel(variable.capitalize().replace('_', ' ') + " (cm)", fontdict=font2)
   ax.grid(linestyle='--', linewidth=0.5, color='black', alpha=0.4)
   plt.savefig("Plots/" + variable + "_boxplot.png")

```



Correlations Table as generated by corr() function

|                    | sepal length in cm | sepal width in cm | petal length in cm | petal width in cm |
|--------------------|--------------------|-------------------|--------------------|-------------------|
| sepal length in cm | 1.000000           | -0.109369         | 0.871754           | 0.817954          |
| sepal width in cm  | -0.109369          | 1.000000          | -0.420516          | -0.356544         |
| petal length in cm | 0.87175            | -0.420516         | 1.000000           | 0.96275           |
| petal width in cm  | 0.817954           | -0.356544         | 0.962757           | 1.000000          |


### Use of this Project


### Get Started


1. Clone the repository to your local machine. 

```sh
git clone https://github.com/MikeCurleyCoosan/pands-project.git

```
2. Download and install [Anaconda](https://www.anaconda.com/). Anaconda comes with its own set of pre-installed data science packages and tools, making it convenient for 
beginners to set up their environment quickly. The pre-installed packages that are required to work with the project are [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/).

3. Download and install [Visual Studio Code](https://code.visualstudio.com/). Visual Studio Code is a code editor with support for development operations like debugging, 
task running, and version control.

4. Download and install the latest version of [Git](https://git-scm.com/). Git is a free and open source version control system designed to handle everything from small to 
very large projects with speed and efficiency.

5. Navigate to the project directory in VS Code


I used [Open in Colab](https://openincolab.com/) to generate the following clickable link. It opens the 'iris_dataset.ipynb' notebooks in [Google Colab](https://colab.research.google.com/).



### Get Help

Where users can get help with your project

### Contribute 

Who maintains and contributes to the project

### Author

About me....

### References

- Reference #1: https://archive.ics.uci.edu/ml/datasets/iris
- Reference #2: https://www.w3schools.io/file/markdown-images/ 
- Reference #3: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
- Reference #4: https://realpython.com/python-histograms/ 
- Reference #5: https://realpython.com/python-matplotlib-guide/
- Reference #6: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
- Reference #7: https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d
- Reference #8: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
- Reference #9: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
- Reference #10: https://www.tablesgenerator.com/markdown_tables
- Reference #11: https://builtin.com/data-science/boxplot
- Reference #12:


