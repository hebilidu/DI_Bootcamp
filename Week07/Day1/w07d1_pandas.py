import pandas as pd
import numpy as np
import requests

# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

with open('data.txt') as f:
    rf = f.read()

print(type(rf))

df = pd.read_csv('data.txt')
print(type(df))
print(df.head())
print("Info:\n,", df.info)
print("Columns:\n", df.columns)
print("species.unique:\n", df.species.unique)

print("Select the row 1 to 5 of the species column")
print(df.loc[1:5, 'species'])

# Sorting
# df.sort_values('sepal_length', ascending=False, inplace=True)
df.sort_values('sepal_length', ascending=False)

# Grouping
# print(df['species'].value.counts())

# Exercise
print("*** Using the Iris DataFrame, print out the 50th row.")
print(df.iloc[50])
# - Get the 50th to 60th row of the Iris DataFrame skipping every other row and return a new DataFrame of just
# the species, petal_length, and petal_width
print("*** 50 to 60 rows, 1 out of 2")
print(df.iloc[50:61:2][['species', 'petal_length', 'petal_width']])
# - Group the data by species and get the median and the sum of sepal_length for each group
print("*** grouped by species with median and sum for each group")
print(df.groupby('species')['sepal_length'].agg([np.median, np.sum]))#