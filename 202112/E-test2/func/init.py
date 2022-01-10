from func.tools import *
import os,pyodbc,random,sys
from func.globalValue import *
from func.downloadfile import *

def db_init():
    dbfile = os.path.join(Get_value('dbpath'), "engdict.accdb")
    dbpath = os.path.abspath(dbfile)
    Set_value('conn',pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + dbpath + ";Uid=;Pwd=;"))

def getEbooknames():
    path =Get_value('bookpath')
    books = Get_file_list(path)
    #没有单词书，就返回空
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

# 根据书名获取书里的单词，返回单词的列表
def getbookcontent(book):
    path = Get_value('bookpath')
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

def getConfig():
    Set_value('questionnum', int(readConfig('listenwrite', 'questionnum')))
    Set_value('practice',int(readConfig('listenwrite', 'practice')))
    Set_value('bookpath', readConfig('listenwrite', 'bookpath'))
    Set_value('dbpath', readConfig('listenwrite', 'dbpath'))
    Set_value('mp3path', readConfig('listenwrite', 'mp3path'))
    Set_value('dispmean', readConfig('listenwrite', 'dispmean'))


def getTestQuestions(book_words):
    pathMp3 = Get_value('mp3path')
    line = {}
    words = []
    for i in book_words:
        #构成 {'word':'hi','mean':'你好','mp3':'us_words\hi.mp3'}
        line.setdefault('word', i)
        # t1 = get_time_stamp().split(":")[-1]
        try:
            mean = search_word_mean(i)
            mean = mean['mean']
        except Exception as err:
            print('init.py 函数 getTestQuestions : ',err)
            sys.exit(1)

        line.setdefault('mean', str(mean))
        # t2 = get_time_stamp().split(":")[-1]
        # print(float(t2)-float(t1))
        mp3file = os.path.join(pathMp3, i + '.mp3')
        if not os.path.exists(mp3file):
            downloadmp3(i)
        line.setdefault('mp3', mp3file)
        words.append(line)
        line = {}
    random.shuffle(words)
    return words


def replaceall(juzi):
    biaodian = ['?', '.', ',', '!', ' ']
    for str in biaodian:
        juzi = juzi.replace(str,'')
    return juzi