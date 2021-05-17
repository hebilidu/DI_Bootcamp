# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# LINE CHART

# Generation of variables 
x=np.arange(0,10) #Array of range 0 to 9
y=x**3

# Printing the variables
print(x)
print(y)

plt.plot(x,y) # Function to plot
plt.title('Line Chart') # Function to give title

# Functions to give x and y labels
plt.xlabel('X-Axis') 
plt.ylabel('Y-Axis')

# Functionn to show the graph  
plt.show()