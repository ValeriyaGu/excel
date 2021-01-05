import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)), 
 			 index=['red','blue','yellow','white'], 
 			 columns=['ball','pen','pencil','paper'])

def f(x): 
    return pd.Series([x.min(), x.max()], index=['min','max'])

ser = pd.Series([5,0,3,8,4], 
 		    index=['red','blue','yellow','white','green'])

frame = pd.DataFrame(np.arange(16).reshape((4,4)), 
 			 index=['red','blue','yellow','white'], 
 			 columns=['ball','pen','pencil','paper'])

seq2 = pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008',
                        '2009','2010','2011','2012','2013'])
seq = pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008',
                        '2009','2010','2011','2012','2013'])

ser = pd.Series([0,1,2,np.NaN,9],
 		    index=['red','blue','yellow','white','green'])
ser['white'] = None 

frame3 = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
 			  index = ['blue','green','red'],
 			  columns = ['ball','mug','pen'])

mser = pd.Series(np.random.rand(8),
  	     index=[['white','white','white','blue','blue','red','red',
 'red'], ['up','down','right','up','down','up','down','left']])

mframe = pd.DataFrame(np.random.randn(16).reshape(4,4),
 			  index=[['white','white','red','red'], ['up','down','up','down']],
 			  columns=[['pen','pen','paper','paper'],[1,2,1,2]])


mframe = mframe.swaplevel('colors','status')
print(mframe.sort_index(level='colors'))

