# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Scatter plot

# Generation of x and y variables
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

# Function to plot the graph
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()