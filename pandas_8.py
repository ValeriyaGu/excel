import numpy as np
import pandas as pd

frame0 = pd.DataFrame(np.arange(4).reshape(2,2))

#frame = pd.DataFrame(np.random.random((4,4)), index = ['white','black','red','blue'], columns = ['up','down','right','left'])


# s = ['<HTML>']
# s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
# s.append('<BODY>')
# s.append(frame.to_html())
# s.append('</BODY></HTML>')
# html = ''.join(s)

# html_file = open('myFrame.html','w')
# html_file.write(html)
# html_file.close()

#print(frame.to_html())

web_frames = pd.read_html('myFrame.html')

ranking = pd.read_html('https://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')

print(ranking[0])