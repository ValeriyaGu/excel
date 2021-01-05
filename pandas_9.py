import pandas as pd
from lxml import objectify

xml = objectify.parse('books.xml')

root = xml.getroot()

def etree2df(root):
    column_names = []
    for i in range(0, len(root.getchildren()[0].getchildren())):
        column_names.append(root.getchildren()[0].getchildren()[i].tag)
    xmlframe = pd.DataFrame(columns=column_names)
    for j in range(0, len(root.getchildren())):
        obj = root.getchildren()[j].getchildren()
        texts = []
        for k in range(0, len(column_names)):
            texts.append(obj[k].text)
        row = dict(zip(column_names, texts))
        row_s = pd.Series(row)
        row_s.name = j
        xmlframe = xmlframe.append(row_s)
    return xmlframe

print(etree2df(root))