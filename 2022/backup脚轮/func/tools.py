import datetime,os,glob,shutil,time,sys
from func.Write_log import Write_log
from func.param import *

# 按今天日期,和距今天数backup_days,返回日期列表
def Get_copy_dates(backup_days,today=1):
    if backup_days<1:
        backup_days=1  #至少保护当天的
    date_list = []
    for i in range(1-today, backup_days):
        curr_date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y\%m\%d")
        date_list.append(curr_date)
    return date_list


def Create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)


# 获取当前目录下的文件和目录，当前层，不含子目录。默认同时返回目录和文件列表
def current_folder(folder,includefile=True):
    folderlists =[]
    filelists = []
    #os.walk(folder, topdown=True)
    if includefile:
        for file in os.listdir(folder):
            file = os.path.join(folder,file)
            if os.path.isdir(file):
                folderlists.append(file)
            else:
                filelists.append(file)
        return folderlists,filelists
    else:
        for file in os.listdir(folder):
            file = os.path.join(folder, file)
            if os.path.isdir(file):
                folderlists.append(file)
        return folderlists


# 获取目录下的所有文件和目录（含所有子目录）
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
         #print(root) #当前目录路径
         #print(dirs) #当前路径下所有子目录(含子目录)
         print(files) #当前路径下所有非目录子文件(含子目录)

# 获取目录下所有目录列表，含子目录，当目录过大过深程序会慢
def Get_dir_list(source_path):
    dir_list=[]
    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isdir(i):
            dir_list.append(i)
    return dir_list


# 获取目录下所有文件列表（含子目录，目录过大过深会慢）,如果传递进来是一个文件也可以
def Get_file_list(source_path):
    files_list=[]
    if os.path.isfile(source_path):
        files_list.append(source_path)
        return files_list

    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
            print('w=',i)
        else:
            print('d=',i)
    return files_list





import configparser
#读取ini方法
def Read_ini(inivaluse,inikey='param'):
        config = configparser.ConfigParser()
        config.read("config.ini",encoding="utf-8-sig")
        convaluse=config.get(inikey,inivaluse)
        return convaluse



