import numpy as np
from numpy.lib.nanfunctions import _nanquantile_dispatcher

old = [2,4,6,8,13,2020]
np_old = np.array(old)
np_new = np_old.reshape((3,2))
# print("old", np_old)
# print("new", np_new)

old2 = ([
    [3,5,7,-4,1],
    [0,5,33,-750,2]
    ])
np_old2 = np.array(old2)
# print(np_old2[:, :3])
# print(np_old2[0,-2]) # 2nd but last of column 1

# print(np.mean(np_old2[0])) # mean of all numbers
# print(np.mean(np_old2[:,0])) # mean of 1st row
# print(np.mean(np_old2[:,1])) # mean of 2nd row

# np.median?
# print(np.median(np_old2, axis = 0))
# print(np.median(np_old2, axis = 1))

# Min and Max 
# print(np_old2[:,:3].min(axis=1)) # min of first 3 numbers of each line (axis=1 means line)

# Broadcasting
np_new = np_old ** 3

# Generate an array
a = np.arange(9).reshape((3,3))

# Exercise
# Create a function which takes that numpy 1-D array as input and returns the following (in the same order as listed):

# * The minimum value in the array * The standard deviation of the data * The product of the elements in the array * Dot product of the array to itself * An array with 4 subtracted from every element in the input array

def funct(arr_1d):
    np_arr_1d = np.array(arr_1d)
    print("array: ",np_arr_1d)
    print("standard deviation: ", round(np.std(np_arr_1d), 2))
    print("min of whole array: ", np.min(np_arr_1d))
    print("product of all elements: ", np.prod(np_arr_1d))
    print("dot: ", np.dot(np_arr_1d, np_arr_1d))
    print("substract 4 from all elements: ", np_arr_1d - 4)

# funct([3,5,65,-2])
