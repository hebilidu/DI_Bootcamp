import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
cars_df = pd.read_csv(url)