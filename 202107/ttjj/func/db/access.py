from func.globalValue import *
import sys
import os,pyodbc
from func.globalValue import *

class DbConnect(object):

    def __init__(self):
        self.db_init()

    def db_init(self):
        dbfile = os.path.join(get_value('dbpath'), "dict.accdb")
        dbpath = os.path.abspath(dbfile)
        set_value('conn',pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + dbpath + ";Uid=;Pwd=;"))

    def search_word_mean(self,word):
        conn = get_value('conn')
        cursor = conn.cursor()

        edit_SQL="select mean from chengyu where word=\'%s\'" % (word)
        cursor.execute(edit_SQL)
        aa =cursor.fetchall()
        cursor.close()
        #print('word :=',word)

        if not aa or aa==[] or aa==None:
            # 在数据库里找不到该成语，返回空
            return
        aa = aa[0][0]
        aa = aa.replace('#','\'')
        wordmean = aa
        #set_value('conn',None)
        return wordmean

    def write_word_Mean(self,word,mean):

        conn = get_value('conn')
        cursor = conn.cursor()
        # access数据库里不能存储 ' 符号,需要替换为"
        edit_SQL = "insert into chengyu ([word],[mean])  values('%s','%s')" % (word, mean.replace("\'", "#"))
        try:
            cursor.execute(edit_SQL)
            cursor.commit()
        except Exception as err:
            print(err)
            set_value('conn', None)
            cursor.close()
            sys.exit(1)
        cursor.close()


    def __del__(self):
        set_value('conn',None)