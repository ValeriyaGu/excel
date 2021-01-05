import pandas as pd
import numpy as np
import re

text = '16 Bolton Avenue , Boston'

r = text.split(',')

tokens = [s.strip() for s in text.split(',')]

address, city = [s.strip() for s in text.split(',')]

strings = ['A+','A','A-','B','BB','BBB','C+']

strs = '; '.join(strings)

search = 'Boston' in text

text2 = "This is an\t odd \n text!"

pro = re.split('\s+', text2)

regex = re.compile('\s+')

ipo = regex.split(text)

print(pro)

