# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# MULTIPLE LINES CHART

# Generation of 1 set of variables 
x = np.arange(0,11)
y = x**3

# Generation of 1 set of variables
x2 = np.arange(0,11)
y2 = (x**3)/2

# Printing all variables
print(x,y,x2,y2,sep="\n")

# "linewidth" is used to specify the width of the lines
# "color" is used to specify the colour of the lines
# "label"is used to specify the name of axes to represent in the lengend 
plt.plot(x,y,color='r',label='first data', linewidth=5) 
plt.plot(x2,y2,color='y',linewidth=5,label='second data')
plt.title('Multiline Chart')

# Uses the label attribute to display reference in legend
plt.ylabel('Y axis')
plt.xlabel('X axis')

# Shows the legend in the best postion with respect to the graph
plt.legend()
plt.show()