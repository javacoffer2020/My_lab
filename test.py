
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

profile = pd.read_csv('E:\Jupyter\GitHub\Transactions.csv')
print(profile.head())

train_data, test_data = train_test_split(profile.[],test_size=0.3, train_size=0.7, )

