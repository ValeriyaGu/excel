import pandas as pd
import numpy as np

frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
 			           'price': [12.33,11.44,33.21,13.23,33.62]})

frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
        			   'color': ['white','red','red','black']})

frame3 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
 			   'color': ['white','red','red','black','green'],
 			   'brand': ['OMG','ABC','ABC','POD','POD']})

frame4 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
 			   'brand': ['OMG','POD','ABC','POD']})

print(pd.merge(frame3,frame4, on='brand'))
