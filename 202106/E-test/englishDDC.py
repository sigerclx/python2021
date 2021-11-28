import csv
import os
import time
import random
import pprint
import sys
import listen_write
import configRead
from tools import *

#打开我自己生成的单词表，导入到words并且返回
def openmyWordBook(filename='english.csv'):
    mp3path=r'us_words/'
    with open(filename,encoding='utf-8') as englishFile:
        englishReader = csv.reader(englishFile)
        words=[]
        line={}
        for i in englishReader:
            if str(i[6])=="1":
                book= str(i[0])
                grade= str(i[1])
                volume= str(i[2])
                module=str(i[4])
                word= str(i[5])
                mp3= mp3path+word+'.mp3'
                mean= str(i[-1])
                
                line.setdefault('book',book)
                line.setdefault('grade',grade)
                line.setdefault('volume',volume)
                line.setdefault('module',module)
                line.setdefault('word',word)
                line.setdefault('mean',mean)
                line.setdefault('mp3',mp3.lower())
                
                words.append(line)
                line={}
    #random.shuffle(words)
    return words

#按过滤条件过滤单词
def filtersMyBook(words,filter):
    filterWords=[]
    for i in words:
        zhengque=1
        if len(filter['book'])>0:
            if filter['book']!=i['book']:
                zhengque=0

        if len(filter['grade'])>0:
            if filter['grade']!=i['grade']:
                zhengque=0

        if len(filter['volume'])>0:
            if filter['volume']!=i['volume']:
                zhengque=0

        if len(filter['module'])>0:
            if (int(i['module']) not in filter['module']):
                zhengque=0

        if zhengque==1:
            filterWords.append(i)
    random.shuffle(filterWords)
    return filterWords


words=openmyWordBook()

#filters={'book':'外语教学与研究出版社','grade':'二年级','volume':'下册','module':[2]}
filters={}
filters.setdefault('book', configRead.readConfig('listenwrite','book'))
filters.setdefault('grade', configRead.readConfig('listenwrite','grade'))
filters.setdefault('volume', configRead.readConfig('listenwrite','volume'))
filters.setdefault('module', configRead.readConfig('listenwrite','module'))
words=filtersMyBook(words,filters)

questionnum= configRead.readConfig('listenwrite','questionnum')
print('英语小测验  共'+str(questionnum)+'题')
print('答题时请注意：')
print(r'1、 按 回车 键可以重新听单词发音')
print(r'2、 按 s回车 键可以看到单词的拼写')
print('')
print('')

listen_write.listenWrite(words,questionnum)

    

        
        


