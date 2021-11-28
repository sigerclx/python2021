import os,glob
# 获取目录文件列表,如果传递进来是一个文件也可以
def Get_file_list(source_path):
    files_list=[]
    if os.path.isfile(source_path):
        files_list.append(source_path)
        return files_list

    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
    return files_list

def getEbooknames():
    path ='book'
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