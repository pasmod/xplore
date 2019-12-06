<h1 align="center">
  <img src="logo.svg" alt="Markdownify" width="200"></a>
</h1>

<h4 align="center">Automatic Explorative Data Analysis</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
</p>

Many steps in explorative data analysis (EDA) can be considered as repitetive tasks. A common workflow among many data scientists when getting a new dataset is to create a notebook for reading the data and getting an overview about the properties of the data. This includes steps, such as identifiying existing data types, collecting statistics about the missing values and creating plots to observe the distribution of the variables. Exploration steps like this are not considered as a creative work and mostly consumes a lot of time to implement. 

xPlore is a Python library to automate this process. Given a data set, xPlore automatically creates a Jupyter notebook, which contains most of the code required for explorative data analysis. The notebook includes not only the results, but also the implementations, so that the data scientist can modify it according to their needs.

xPlore is by no means intends to replace the create work of a data scientist! This library is still in early phases of development, so contributions are very welcomed.

## Key Features

* Automatic Generation of a Jupyter notebook for EDA
* Support for Classification Tasks


## How To Use
Clone the project and build the Docker image:
```
cd xplore
make build
```

Start the service:

```
make up
```

Enter the URL shown in the terminal into your browser to access the notebook:
```
http://127.0.0.1:8888/?token=f3d07473cbfadc784d6411b1c41c77fdfc940a316e0e77b3
```

Define tha path to the data set for which you want to generate and explorative data analysis report
```python
path = "../resources/iris.csv"
```

Create an exploration object by calling the explore method
```python
import xplore

exploration = xplore.me(path, mode="classification", target="class")
```
Create a notebook file using the exploration object created in the previous step. Give it a name and specify a language

```python
from xplore.notebook import Notebook

Notebook(exploration).name("iris_exploration").tongue("en").build()
```
