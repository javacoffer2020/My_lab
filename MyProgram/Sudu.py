import pandas as pd
import numpy as np

a = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
print(a)

b = pd.DataFrame({"C": ['a', 'b', 'c', 'd'], "B": ['e', 'f', 'g', 'h']})

print(b)

c = pd.concat([a,b],axis=1)
print(c)