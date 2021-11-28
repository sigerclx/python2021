from getWordMean import getwordMean
import datetime
from tools import *
import json

# 根据worddict里的单词，下载单词含义

mydict ={}
dict = open('worddict.txt', mode='r', encoding='utf-8')
i=0
for line in dict:
    i+=1
    word =line.lower()
    word = word.replace('\n','')
    mean = getwordMean(word)
    print(i,word)
    if mean:
        mydict.setdefault(word,mean )
        write_log(word +"="+str(mean), 'engmean')
    else:
        write_log(word, 'nomean')

dict.close()

#
#
# mydict ={}
# i =0
# for file in files:
#     i+=1
#     file =file.lower()
#     file =file.replace(".mp3","")
#     print(i,file)
#     word = file.split("\\")[1]
#     mean = getwordMean(word)
#     if mean:
#         mydict.setdefault(word,mean )
#         write_log(word +"="+str(mean), 'engmean1')
#     else:
#         write_log(word, 'nomean')
#
# write_log(str(mydict), 'eng')

