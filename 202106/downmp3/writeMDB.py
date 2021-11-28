import pyodbc
from tools import *

# 将单词的含义写入数据库

path=r'D:\Python\pythonLearn\2021\202106\downmp3\engdict.accdb'
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path + ";Uid=;Pwd=;")
cursor = conn.cursor()

dict = open('eng2000Mean.txt', mode='r', encoding='utf-8')
i=0
for line in dict:
    i+=1
    line =line.lower()
    line = line.replace('\n','')
    line = line.split("=")
    print(i,line)
    #access数据库里不能存储 ',需要替换为"
    edit_SQL = "insert into english ([word],[mean])  values('%s','%s')" % (line[0].replace("\'","\""),line[1].replace("\'","\""))

    try:
        cursor.execute(edit_SQL)
        cursor.commit()
    except Exception:
        #print(line)
        write_log(line[0],'chongfu')

conn.close()
dict.close()

