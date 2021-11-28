#! python3
# 古诗 把TXT的古诗作者，整理成字典存于gushi.csv

import csv
import os
import pprint

gushiTXT = open('75gushi.txt')

gushilines = gushiTXT.readlines()

gushi=[]
line=[]

for str1 in gushilines:
    str1=str1.strip('\n')
    str2 = str1.split(',')
##    print(str2[0])
##    print(str2[1]+'\n')
##    print(str(str2[2:]))
    line.append(str2[0])
    line.append(str2[1])
    line.append(str2[2:])
    gushi.append(line)
    #print(line)
    line=[]



writeFile=open('gushi.csv','w',newline='')
csvWriter=csv.writer(writeFile)
for i in gushi:
    #print(i)
    csvWriter.writerow(i)
writeFile.close()



