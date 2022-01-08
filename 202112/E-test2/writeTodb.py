import pyodbc,sys
from func.getWordMean import *
# 将一个单词的含义写入数据库
# 为了补全数据库,这是备用程序

path=r'D:\Python\pythonLearn\2021\202106\E-test1\db\engdict.accdb'
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path + ";Uid=;Pwd=;")
cursor = conn.cursor()

word = 'august'
mean = str(getwordMean(word))

if mean:
    print(mean)
    print(mean.replace("\'", "\\\'"))
else:
    print('no mean')
    sys.exit(1)
sys.exit(1)
#access数据库里不能存储 ',需要替换为" mean.replace("\'", "#")
edit_SQL = "insert into english ([word],[mean])  values('%s','%s')" % (word,mean.replace("\'", "#"))
try:
    cursor.execute(edit_SQL)
    cursor.commit()
except Exception as err:
    print(err)

cursor.close()
conn.close()



