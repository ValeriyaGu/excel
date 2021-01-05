import pandas as pd
import numpy as np

s = pd.Series([14, 5, 6, 7, 13], index=['a', 'b', 'c', 'd', 'e'])

arr = np.array([1,2,3,4])
s3 = pd.Series(arr)

s4 = pd.Series(s)

arr[2] = -2

serd = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green',' green','yellow'])

s2 = pd.Series([5, -3, np.NaN, 14])

mydict = {'red': 2000, 'blue': 1000, 'yellow': 500,
 'orange': 1000}

mydict2 = {'red':400,'yellow':1000,'black':700}

colors = ['red','yellow','orange','blue','green']

myseries = pd.Series(mydict, index = colors)

myseries2 = pd.Series(mydict2)

data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'],
        'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}

frame = pd.DataFrame(data)

frame2 = pd.DataFrame(data, columns=['object', 'color'])

frame3 = pd.DataFrame(np.arange(20).reshape((5,4)),
                       index=['red', 'blue', 'yellow', 'white', 'black'],
                       columns=['ball', 'pen', 'pencil', 'paper'])
frame.index.name = 'id'
frame.columns.name  = 'item'

frame['new'] = [3.0, 1.3, 2.2, 0.8, 1.1]



ser = pd.Series(np.arange(5))

frame['new'] = ser


del frame['new']

nestdict = {'red': { 2012: 22, 2013: 33},
             'white': { 2011: 13, 2012: 22, 2013: 16},
             'blue': { 2011: 17, 2012: 27, 2013: 18}}

frame2 = pd.DataFrame(nestdict)

ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])

serd = pd.Series(range(6), index=['white','white','blue','green', 'green','yellow'])

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
           index=['red', 'blue', 'yellow', 'white'],
           columns=['ball','pen','pencil','paper'])

ser = pd.Series(np.arange(4), index=['ball','pen','pencil','paper'])
ser['mug'] = 9



