# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# BAR CHART

# Generation of variables 
x = ["India",'USA',"Japan",'Australia','Italy']
y = [6,7,8,9,2]

# Printing the variables
print(x)
print(y)

plt.bar(x,y, label='Bars1', color ='r') # Function to plot

# Function to give x and y labels 
plt.xlabel("Country")
plt.ylabel("Inflation Rate%")

# Function to give heading of the chart
plt.title("Bar Graph")

# Function to show the chart
plt.show()