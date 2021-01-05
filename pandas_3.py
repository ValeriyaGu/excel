import pandas as pd

import numpy as np

ser = pd.Series([2,5,7,4], index=['one','two','three','four'])

ser2 = ser.reindex(['three','four','five','one'])

ser3 = pd.Series([1,5,6,3],index=[0,3,5,6])

ser3 = ser3.reindex(range(6),method='bfill')

ser = pd.Series(np.arange(4.), index = ['red','blue','yellow','white'])

frame = pd.DataFrame(np.arange(16).reshape((4,4)), 
                      index=['red', 'blue', 'yellow', 'white'],
                      columns=['ball', 'pen', 'pencil', 'paper'])

s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])

print(s1 + s2)