import numpy as np
import pandas as pd

csvframe = pd.read_csv('ch05_01.csv')

csvframe2 = pd.read_table('ch05_01.csv', sep=',')

csvframe3 = pd.read_csv('ch05_02.csv', names=['white', 'red', 'blue', 'green', 'animal'])

csvframe4 = pd.read_csv('ch05_03.csv', index_col=['color', 'status'])

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
		 index = ['red', 'blue', 'yellow', 'white'],
		 columns = ['ball', 'pen', 'pencil', 'paper'])

frame.to_csv('ch05_07.csv', index=False, header=False)

frame3 = pd.DataFrame([[6,np.nan,np.nan,6,np.nan],
 	      [np.nan,np.nan,np.nan,np.nan,np.nan],
 	      [np.nan,np.nan,np.nan,np.nan,np.nan],
          [20,np.nan,np.nan,20.0,np.nan],
 	      [19,np.nan,np.nan,19.0,np.nan]
 	      ],
 		     index=['blue','green','red','white','yellow'],
		     columns=['ball','mug','paper','pen','pencil'])

frame3.to_csv('ch05_09.csv', na_rep ='NaN')
