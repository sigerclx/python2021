import os
import glob
import filecmp
import hashlib

#2021-5-23

import configparser
#读取ini方法
def Read_ini(inivaluse,inikey='param'):
        config = configparser.ConfigParser()
        config.read("config.ini",encoding="utf-8-sig")
        convaluse=config.get(inikey,inivaluse)
        return convaluse

# 要查找重复文件的目标文件夹
dir_path = r''+Read_ini('path')
#print(dir_path)

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


file_md5s={}
file_lst = []
t=0
fileList=open('rptFiles1.txt',mode='w',encoding='utf-8')

#'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

allsize=0
chongfunum =0
print('start...')


list_dirs = os.walk(dir_path)
for root, dirs, files in list_dirs:
    for file in files:
        t += 1
        print(t)
        # print('num:',t,i,end=" ")
        i = os.path.join(root,file)
        tmpMd5 = GetFileMd5(i)
        # 在字典里查找md5，找到就说明重复，然后删除当前重复文件，没找到就记录到字典
        cfile = file_md5s.get(tmpMd5)
        # print(tmpMd5)
        if cfile:
            chongfunum += 1
            sizeMb = get_FileSize(i)

            if os.path.exists(i) and os.path.exists(cfile):

                try:
                    #路径长的留下，路径短的删除
                    if len(i) < len(cfile):
                        os.remove(cfile)
                        fileList.writelines(cfile + ' ' + i + '\n')
                        print('deleting ' + cfile)
                    else:
                        os.remove(i)
                        fileList.writelines(i + ' ' + cfile + '\n')
                        print('deleting ' + i)
                    allsize = allsize + sizeMb

                except  Exception as err:
                    fileList.writelines('权限不足：' + i + ' ' + cfile + '\n')
                    print('PermissionError : Can\'t deleting ' + i)
            fileList.flush()
        else:
            file_md5s[tmpMd5] = i

fileList.writelines('删除文件总数:'+str(chongfunum)+'  删除文件总大小：'+str(round(allsize,2))+'MB\n')
fileList.close()