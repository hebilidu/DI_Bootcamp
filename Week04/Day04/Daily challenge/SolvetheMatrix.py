# Week04 Day04 - Daily challenge - Solve the Matrix
# Created on  : 210428 by : lidu
# Modified on : 210428 by : lidu

# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) 
# with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting 
# from the leftmost column, select only the alpha characters and connect them, 
# then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:
#     7i3
#     Tsi
#     h%x
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!
list = [
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM',
    '$a',
    '#t%',
    '^r!',
]
def dematrix(*arg):
    '''Transpose lines of text to be read by columns into a continuous string'''
    print(arg)

dematrix(list)
dematrix(*list)