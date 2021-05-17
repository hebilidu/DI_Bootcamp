# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# MULTIPLE BAR CHART

# Generation of 1 set of variables 
x = ["India",'USA',"Japan",'Australia','Italy']
y = [6,7,8,9,5]

# Generation of 2 set of variables
x2 = ["India",'USA',"Japan",'Australia','Italy']
y2 = [5,1,3,4,2]

# Printing all variables
print(x,y,x2,y2,sep="\n")

# Functions to plot 
plt.bar(x,y, label='Inflation', color ='y')
plt.bar(x2,y2, label='Growth', color ='g')

# Functions to give x and y labels
plt.xlabel("Country")
plt.ylabel("Inflation & Growth Rate%")

plt.title("Multiple Bar Graph")
plt.legend()
plt.show()