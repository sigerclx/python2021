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

        edit_SQL="select mean,source,example,pinyin from chengyu where name=\'%s\'" % (word)
        cursor.execute(edit_SQL)
        aa =cursor.fetchall()
        cursor.close()
        #print('word :=',word)

        if not aa or aa==[] or aa==None:
            # 在数据库里找不到该成语，返回空
            return "",""

        mean = aa[0][0].replace('#','\'')
        source = aa[0][1].replace('#', '\'')
        example = aa[0][2].replace('#', '\'')
        pinyin = aa[0][3].replace('#', '\'')

        wordmean = mean+'\n出处: '+source + '\n示例: '+example
        #set_value('conn',None)
        return wordmean,pinyin

    def write_word_Mean(self,word,mean):

        conn = get_value('conn')
        cursor = conn.cursor()
        # access数据库里不能存储 ' 符号,需要替换为"
        edit_SQL = "insert into chengyu ([name],[pinyin],[mean],[source],[example])  values('%s','%s','%s','%s','%s')" % (word,'无', mean.replace("\'", "#"),'无','无')
        #print(edit_SQL)
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