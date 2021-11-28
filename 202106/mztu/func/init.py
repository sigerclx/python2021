from func.ini.read import readini
from func.globalValue import *
from func.tools import *
import os

def getconfig():
    set_value('questionnum', int(readini('set', 'questionnum')))
    set_value('practice',int(readini('set', 'practice')))
    set_value('bookpath', readini('set', 'bookpath'))
    set_value('dbpath', readini('set', 'dbpath'))
    set_value('engine', readini('set', 'engine'))

def getEbooknames():
    path =get_value('bookpath')
    books = get_file_list(path)
    #没有成语书，就返回空
    if not books:
        return

    bookdict={}
    i=0
    for bookfile in books:
        i+=1
        file,ext = os.path.splitext(bookfile)
        cpath, file = os.path.split(file)
        bookname =  file.replace(ext,'')
        bookdict.setdefault(str(i),bookname)

    return bookdict

def selectbook():
    # 获取单词书目
    bookdict = getEbooknames()

    for no, bookname in bookdict.items():
        print(no, ':', bookname)
    chioce = input("请选择书: ")
    return bookdict[chioce]

# 根据书名获取书里的成语，返回成语的列表
def getbookcontent(book):
    path = get_value('bookpath')
    cbook = open(os.path.join(path, book + '.txt'), mode='r', encoding='utf-8')

    book_words = []
    for line in cbook:
        line = line.replace('\n', '')
        if "=" in line:   # 当发现=号的时候，后面的单词忽略(方便没学的单词可以放到=号后面)
            break
        if "-" in line:   # 当发现-号的时候，前面的单词忽略(方便没学的单词可以放到-号前面)
            book_words = []
            continue
        # 去除空行
        if (len(line)>0):
            book_words.append(line)
    cbook.close()
    return book_words

