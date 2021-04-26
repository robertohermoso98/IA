import numpy as np


a=np.empty([2,3])

for i in range(2):
    for e in range(3):
        a[i][e]=3

print(a)
