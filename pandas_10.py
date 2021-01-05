import pandas as pd
import numpy as np
from sqlalchemy import create_engine

frame = pd.DataFrame(np.arange(20).reshape(4,5),
 			 columns=['white','red','blue','black','green'])

print(frame)

engine = create_engine('sqlite:///foo.db')

#frame.to_sql('colors',engine)

print(pd.read_sql('colors',engine))
print(pd.__version__)