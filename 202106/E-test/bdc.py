import csv
import os
import time
import random
import pprint
import sys
import win32com.client
from tools import *
from getWordMean import getwordMean
from listen_write import *

#单词书存放路径
path = r'books'
#单词MP3存放路径
pathMp3 = r'us_words'

books = Get_file_list(path)
i=0
bookdict={}

for bookfile in books:
    i+=1
    file,ext = os.path.splitext(bookfile)
    cpath, file = os.path.split(file)
    bookname =  file.replace(ext,'')
    bookdict.setdefault(str(i),bookname)

print(bookdict)

cbook = open(os.path.join(path,bookdict["1"]+'.txt'),mode='r',encoding='utf-8')

book_words=[]
book_phrases=[]
book_sentences=[]
biaodian=['?','.',',','!']
for line in cbook:
    line = line.replace('\n','')
    if  not any((i in line) for i in biaodian):
        if ' ' in line:
            book_phrases.append(line)
        else:
            book_words.append(line)
    else:
        book_sentences.append(line)
cbook.close()
# print(book_words)
# print(book_phrases)
# print(book_sentences)

line = {}
words =[]
for i in book_words:

    line.setdefault('word',i )
    line.setdefault('mean', str(getwordMean(i)['mean']))
    line.setdefault('mp3', os.path.join(pathMp3,i+'.mp3'))

    words.append(line)
    line = {}
random.shuffle(words)

print(words)
listenWrite(words,10)

