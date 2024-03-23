# pands-project

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

## Table of Contents.

* [About this project](#about-this-project)
* [Use of this project](#use-of-this-project)
* [Get Started](#get-started)
* [Get Help](#get-help)
* [Contribute](#contribute)
* [Author](#author)

### ***About this project***

This repository contains the Iris Fisher dataset and Python code for analysing it using a variety of Python software modules such as [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/). This project was undertaken as part of the 'Programming and Scripting' module in the Higher Diploma in Data Analytics in ATU, Galway in the year 2024.

The Iris Fisher dataset is a very popular dataset for data analysis and visualization tasks. It is also known as the Iris Flower dataset and consists of different attribute information for three differen classes of the Iris species. The dataset is quite small, consisting of 50 samples of each of the three different classes, to give a total of 150 instances in total. For each instance the different attributes that were taken were as follows, given below as dataset columns. 

### ***Dataset Columns***

- **sepal_length**: The sepal length for each instance, in cms.
- **sepal_width**: The sepal width for each instance, in cms.
- **petal_length**: The petal length for each instance in cms.
- **petal_width**: The petal width for each instance in cms.
- **species**: Iris species (Iris setosa, Iris versicolor, and Iris virginica).

The data was collected in the Gaspé Peninsula by botanist Edgar Anderson, and famously used by statistician Ronald Fisher in his 1936 paper ["The Use of Multiple Measurements in Taxonomic Problems"](https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x) to demonstrate how classification can be gauged by statistics. He argues that, due to some significant attribute differences between the species in this dataset, Iris group membership could potentially be determined by sepal and petal measurements - a method that would become known as [linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis#:~:text=Linear%20discriminant%20analysis%20(LDA)%2C,classes%20of%20objects%20or%20events.). From here it is postulated that new iris flowers could be classified based on the statistical information gleaned from the dataset.

The Iris Dataset remains a popular example as an introduction to exploratory data analysis, pattern recognition, and machine learning algorithms for the following reasons [Brownlee, 2016](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)

1. It is a complete, balanced dataset in that there are no null values and each class is equally represented.
1. Each of the four features (sepal and petal length and width) are measured in the same units (centimetres).
1. One iris species (setosa) is linearly separable from the other two. While the other two species have some overlap, they are still distinguishable from one another in certain measurements. As a result classification is relatively easy, and therefore the dataset predictive cababilities are quite strong.

Iris dataset [01](#references) used in this analysis can be found among files in this repository as iris_data.csv.


### ***Variable Classification***

For efficient data handling and modlelling in Python, it is imperative to choose the correct variable types to represent the various datasets we are modelling. Numerical data types can be represented using Pythons built in native data types while categorical variables are best represented as categorical data types in pandas for memory efficiency and best performance.


### Use of this Project

Why the project is useful

### Get Started

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
- Reference #8: 

