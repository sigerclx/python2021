import pyodbc,sys
from func.getWordMean import *
# 将文件words.txt的单词写入空数据库的english表，生成字典数据库

path=r'D:\Python\pythonLearn\2021\202106\E-test1\db\dict.accdb'
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path + ";Uid=;Pwd=;")
cursor = conn.cursor()

wordfile = open('words.txt',mode='r',encoding='utf-8')
i=0
for word in wordfile:
    i+=1
    word = word.replace('\n','')

    mean = str(getwordMean(word))
    print(i,word)
    if not mean:
        print('no mean')
        sys.exit(1)

#access数据库里不能存储 ',需要替换为"
    edit_SQL = "insert into english ([word],[mean])  values('%s','%s')" % (word,mean.replace("\'", "#"))
    try:
        cursor.execute(edit_SQL)
        cursor.commit()
    except Exception as err:
        print(err)

cursor.close()
conn.close()



