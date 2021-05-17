import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# HISTOGRAM

# Generation of variable
stock_prices = [32,67,43,56,45,43,42,46,48,53,73,55,54,56,43,55,54,20,33,65,62,51,79,31,27]

# Function to show the chart
plt.figure(figsize = (8,5))
plt.hist(stock_prices, bins = 5)
plt.show()