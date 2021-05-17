# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Pie chart

# Collection of raw data
raw_data={'names':['Nick','Sani','John','Rubi','Maya'],
'jan_score':[123,124,125,126,128],
'feb_score':[23,24,25,27,29],
'march_score':[3,5,7,6,9]}

# Segregating the raw data into usuable form/variables
df=pd.DataFrame(raw_data,columns=['names','jan_score','feb_score','march_score'])
df['total_score']=df['jan_score']+df['feb_score']+df['march_score']

# Printing the data
print(df)

# Function to plot the graph
plt.pie(df['total_score'],labels=df['names'],autopct='%.2f%%')
plt.axis('equal')
plt.axis('equal')
plt.show()


