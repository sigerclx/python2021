# 根据文件里的单词查询含义
from func.tools import search_word_mean
from func.globalValue import *
import os,pyodbc

def db_init():
    dbfile = os.path.join('db', "engdict.accdb")
    dbpath = os.path.abspath(dbfile)
    Set_value('conn',pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + dbpath + ";Uid=;Pwd=;"))


# 根据书名获取书里的单词，返回单词的列表
def getbookcontent(book):
    path = 'books'
    cbook = open(os.path.join(path, book + '.txt'), mode='r', encoding='utf-8')

    book_words = []
    book_phrases = []
    book_sentences = []
    biaodian = ['?', '.', ',', '!','\'']
    for line in cbook:
        line = line.replace('\n', '')
        if "=" in line:   # 当发现=号的时候，后面的单词忽略(方便没学的单词可以放到=号后面)
            break
        if "-" in line:   # 当发现-号的时候，前面的单词忽略(方便没学的单词可以放到-号前面)
            book_words = []
            continue
        if not any((i in line) for i in biaodian):
            if (' ' in line) and len(line)>0:
                book_phrases.append(line)
            else:
                # 去除空行
                if (len(line)>0):
                    book_words.append(line)
        else:
            book_sentences.append(line)

    cbook.close()
    return book_words,book_phrases,book_sentences
db_init()
book_words,book_phrases,book_sentences = getbookcontent("UU")
for word in book_words:

    print(word,search_word_mean(word)['mean'],'\n')

    a=input()
