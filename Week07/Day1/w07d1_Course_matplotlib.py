import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# basic example
# x = [1, 2, 3, 4]
# y = [2, 20, 35, 6]
# plt.plot(x, y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('first graph')
# plt.show()

with open('data.txt') as f:
    rf = f.read()
data = pd.read_csv('data.txt')

# plt.plot(data.index, data["sepal_length"], "r--") 
# plt.show()

# scatter plot (when dta non linear)
# plt.scatter(data['sepal_length'], data['petal_length'])
# plt.xlabel('sepal_length (cm)')
# plt.ylabel('petal_length (cm)')
# plt.grid() 
# plt.show()

# subplots

# setosa_data = data[data.species == 'setosa']
# print(setosa_data['species'].count())
# print(setosa_data['species'].unique())
# versicolor_data = data[data.species == 'versicolor']
# virginica_data = data[data.species == 'virginica']

# fig, ax=plt.subplots(1,3,figsize=(13, 5))


# ax[0].hist(setosa_data.petal_length, color='g', label = 'setosa')
# ax[1].hist(versicolor_data.petal_length, color='r', label = 'versicolor')
# ax[2].hist(virginica_data.petal_length, color='b', label = 'virginica')

# ax[0].legend()
# ax[1].legend()
# ax[2].legend()
# ax[0].set_ylabel('Frequency')
# ax[1].set_ylabel('Frequency')
# ax[2].set_ylabel('Frequency')
# ax[0].set_xlabel('petal length (cm)')
# ax[1].set_xlabel('petal length (cm)')
# ax[2].set_xlabel('petal length (cm)')

# plt.show()

# EXERCISE
# - Using NumPy, create an array of length 100 filled with random ints between 0 and 75
randnums= np.random.randint(0,76,100)
# - Reshape that array to a 50 x 2 matrix
wrk_array = 

# - Make a scatter plot of the 1st column as the x axis and the second column as the y axis

# - Now make a histogram of each of the columns and make titles for each plot
