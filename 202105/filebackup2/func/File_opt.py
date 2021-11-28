import datetime,os,time,sys,shutil
from func.tools import *
from func.Write_log import Write_log
from func.param import *

def Delete_file(path):
    # 删除目录下的文件,每删除一个文件,都休息delete_onefile_sleep时间
    sleepms = Get_value("delete_onefile_sleep")
    source_path = Get_value("source_path")
    dest_path = Get_value("dest_path")
    delete_file = Get_value("deletefile")

    files_list = Get_file_list(path)
    for i in files_list:
        # 源文件和目标文件都存在,才能删除源文件.
        if os.path.exists(i):
            if os.path.exists(i.replace(source_path,dest_path)):
                try:
                    if delete_file:
                        os.remove (i)
                        time.sleep(sleepms)
                        Write_log('deleting file ' + i + ' ...')
                        print('deleting file ' + i + ' sleep:' + str(sleepms) + ' ...')
                    else:
                        print('DEMO: deleting file ' + i + ' sleep:' + str(sleepms) + ' ...')
                except Exception as e:
                    print(e)
                    continue
            else:
                Copy_file(i)  # 如果目标文件不存在，先备份，本次不删除
    Delete_folder(path)


def Delete_folder(path):
    # 如果上面文件都删除了，那就把目录也删除掉
    if os.path.isdir(path):
        try:
            os.rmdir(path)  # 删空目录,如果目录里文件不空,则不能删除
            print('deleting folder ' + path + ' ...')
            Write_log('deleting folder ' + path)
        except Exception as e:
            print(e)

#只删除当前目录下的文件夹和文件，只读当前层
def Delete_child_path(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        Delete_file(path)
    Delete_folder(rootDir)

def Delete_path(source_path):
    #获取源目录里所有的文件夹
    dir_list = Get_dir_list(source_path)
    for each_dir in dir_list:
        if os.path.exists(each_dir):
            try:
                Delete_file( r'' + each_dir)  # 依次删除文件,每删一个文件休息delete_onefile_sleep时间
                os.rmdir(each_dir)  # 删空目录,如果目录里文件不空,则不能删除
                print('deleting folder ' + each_dir + ' ...')
                Write_log('deleting folder ' + each_dir)
            except Exception as e:
                print(e)
                continue

    Write_log("清理过期文件夹及文件完成")


#读当前目录下的文件夹和文件，只读当前层
def Copy_child_path(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            #print('path: ',path)
            Copy_path(path)
        if os.path.isfile(path):
            #print('file: ',path)
            Copy_file(path)


def Scan_path():
    curr_date = (datetime.datetime.now()).strftime("%Y\%m\%d")
    # 获取源目录里需要保留（不能删除）的目录清单
    date_list = Get_copy_dates(Get_value("delete_before_days"), today=1)
    source_path = Get_value('source_path')
    list_dirs = os.walk(source_path)
    for root, dirs, files in list_dirs:
        for d in dirs:
            curr_path = os.path.join(root, d)
            test_str =  curr_path.replace(Get_value('source_path')+'\\',"")
            # 含当日日期的不备份，也不删除
            if curr_date in curr_path:
                continue
            if Is_valid_date(test_str):
                # 当日文件不COPY,怕影响性能
                # print('date：',curr_date,curr_path)
                Copy_child_path(curr_path)
                #删除path
                # 如果是保护天数外的文件夹，可以删除
                if test_str not in date_list:
                    Delete_child_path(curr_path)
            else:
                # print('not path ',curr_path)
                # print(path)
                # 不能删除 要保留 delete_before_days 天数的最近文件夹和文件.保护其上层所有文件夹不要被删除
                if not any((test_str in s or s in test_str) for s in date_list):
                    # print('not path in', curr_path)
                    Delete_child_path(curr_path)

        # 复制非常规文件，不在日期目录下的文件，比如根，年，月目录下的文件
        for file in files:
            curr_file = os.path.join(root, file)
            # print(curr_file)
            filesplit = curr_file.split('\\')
            if len(filesplit)>2 and len(filesplit)<6:
                # print(len(filesplit),curr_file)
                Delete_file(curr_file)


def Copy_path(spath):
    # 将源文件夹复制到目标文件夹
    allpic_files = Get_file_list(spath)

    sleepms = Get_value("copy_onefile_sleep")# 每拷贝一个文件休息copy_onefile_sleep时间
    source_path = Get_value('source_path')  # 定义源文件夹
    dest_path1 = Get_value('dest_path')  # 定义目的文件夹

    for file in allpic_files:
        dest_file =  file.replace(source_path, dest_path1)
        dest_path =  dest_file[0:dest_file.rfind("\\")]
        # 目标文件夹不存在,则建立
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            Write_log(dest_path + " Created ")

        # 目标文件不存在,则拷贝备份
        if not os.path.exists(dest_file):
            try:
                shutil.copy2(file, dest_path)
                time.sleep(sleepms)
                print("path Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
            except Exception:
                print("path Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
                Write_log("path copying " + file + ' to ' + dest_path+' error: 源文件找不到 或其他错误')
                continue
            Write_log("path copying " + file + ' to ' + dest_path)


def Copy_file(file):
    sleepms = Get_value("copy_onefile_sleep")  # 每拷贝一个文件休息copy_onefile_sleep时间
    source_path = Get_value('source_path')  # 定义源文件夹
    dest_path1 = Get_value('dest_path')  # 定义目的文件夹

    dest_file = file.replace(source_path, dest_path1)
    dest_path = dest_file[0:dest_file.rfind("\\")]

    # 目标文件夹不存在,则建立
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
        Write_log(dest_path + " Created ")

    # 目标文件不存在,则拷贝备份
    if not os.path.exists(dest_file):
        try:
            shutil.copy2(file, dest_path)
            time.sleep(sleepms)
            print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
            Write_log("copying " + file + ' to ' + dest_path)
        except Exception:
            print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
            Write_log("copying " + file + ' to ' + dest_path + ' error: 源文件找不到 或其他错误')


