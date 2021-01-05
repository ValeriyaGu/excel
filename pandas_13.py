import pandas as pd
import numpy as np

dframe = pd.DataFrame({'color': ['white', 'white', 'red', 'red', 'white'],
                       'value': [2, 1, 3, 3, 2]})

dframe = dframe.drop_duplicates()

frame = pd.DataFrame({'item': ['ball', 'mug', 'pen', 'pencil', 'ashtray'],
                      'color': ['white', 'rosso', 'verde', 'black', 'yellow'],
                      'price': [5.56, 4.20, 1.30, 0.56, 2.75]})

print(frame)

newcolors = {
    'rosso': 'red',
    'verde': 'green'
}

print(frame.replace(newcolors))
