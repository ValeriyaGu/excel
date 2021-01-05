import pandas as pd
import numpy as np
import re

frame = pd.DataFrame({  'color': ['white','red','green','red','green'],
                        'object': ['pen','pencil','pencil','ashtray','pen'],
                        'price1' : [5.56,4.20,1.30,0.56,2.75],
                        'price2' : [4.75,4.12,1.60,0.75,3.15]})

group = frame['price1'].groupby(frame['color'])

ggroup = frame['price1'].groupby([frame['color'],frame['object']])

#print(frame[['price1','price2']].groupby(frame['color']).mean())

# for name, group in frame.groupby('color'):
#     print(name)
#     print(group)

def range(series):
    return series.max() - series.min()

group = frame.groupby('color')

#print(group['price1'].agg(range))

#print(group.agg(range))

print(group['price1'].agg(['mean','std',range]))