import os
import glob
import filecmp
import hashlib


# 要查找重复文件的目标文件夹
dir_path = r'd:\pic1'


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(2048)
        if not b :
            break
        myhash.update(b)
        f.close()
        return myhash.hexdigest()



file_lst = []

for i in glob.glob(dir_path + '/**/*', recursive=True):
    if os.path.isfile(i):
        file_lst.append(i)


file_lst1= list(file_lst)
file_lst2= list(file_lst)
print(id(file_lst),id(file_lst1))

chongfufiles ={}

fileList=open('rptFiles.txt',mode='w',encoding='utf-8')

for x in file_lst:
    for y in file_lst1:
        if x != y and os.path.exists(x) and os.path.exists(y):
            if filecmp.cmp(x, y):
                #print('same:',x,y)文件重复后，进行记录
                fileList.writelines(x+" "+y+"\n")
                fileList.flush()  # 强行写入文件
                chongfufiles[x]=GetFileMd5(x)
                chongfufiles[y] = GetFileMd5(y)
                try:
                    file_lst2.remove(x)
                except Exception:
                    pass

                file_lst2.remove(y)
                #os.remove(y)
    file_lst1 = list(file_lst2)

fileList.close()
print(chongfufiles)

# 如果含某个目录，则删除。
folder ='E:\公司'

for key in chongfufiles:
    if folder in key:
        print(key)

        # os.remove(key)