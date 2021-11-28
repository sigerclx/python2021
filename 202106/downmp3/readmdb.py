
import pyodbc,os
from tools import *

path=r'D:\Python\pythonLearn\2021\202106\downmp3\engdict.accdb'
path = os.path.abspath("engdict.accdb")
print(path)

mean=search_word_mean('hello')
if mean:
    print(mean['mean'])

