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
    # Find longest string
    longest = 0
    for str in arg:
        if len(str) > longest:
            longest = len(str)
    # Build a string by reading the 1st char of each string, then 2nd, ... and get rid of excess spaces
    new_str = ''
    current_is_space = False
    for idx in range(len(str)):
        for str in arg:
            # Case when line is shorter that the longest line
            # print(idx, str,new_str+'.')
            if len(str) <= idx:
                if not current_is_space:
                    new_str += ' '
                    current_is_space = True
            else:
                if str[idx].isalpha():
                    new_str += str[idx]
                    current_is_space = False
                elif not current_is_space:
                    new_str += ' '
                    current_is_space = True
    return new_str

print("\nCoded message :", *list)
print("Decoded :",dematrix(*list), "\n")
