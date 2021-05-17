# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sub plots

# Defining the sixe og the figures
plt.figure(figsize=(10,10))

# Generation of variables
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([5,2,4,2,1,4,5,2])

# Generating 4 subplots in form of 2x2 matrix
# In the line below the arguments of plt.subplot are as follows:
# 2- no. of rows
# 2- no. of columns
# 1- position in matrix
# Position (0,0)
plt.subplot(2,2,1)
plt.plot(x,y,'g')
plt.title('Sub Plot 1')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Position (0,1)
plt.subplot(2,2,2)
plt.plot(y,x,'b')
plt.title('Sub Plot 2')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Position (1,0)
plt.subplot(2,2,3)
plt.plot(y*2,x*2,'y')
plt.title('Sub Plot 3')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Position (1,1)
plt.subplot(2,2,4)
plt.plot(x*2,y*2,'m')
plt.title('Sub Plot 4')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Function for layout and spacing
plt.tight_layout(h_pad=5, w_pad=10)
plt.show()