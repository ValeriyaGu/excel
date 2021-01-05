import pandas as pd
import numpy as np

array1 = np.arange(9).reshape((3,3))

array2 = np.arange(9).reshape((3,3))+6

np.concatenate([array1,array2],axis=1)

np.concatenate([array1,array2],axis=0)

print(np.concatenate([array1,array2],axis=0))

ser1 = pd.Series(np.random.rand(4), index=[1,2,3,4])

ser2 = pd.Series(np.random.rand(4), index=[5,6,7,8])

print(pd.concat([ser1,ser2], keys=[1,2]))