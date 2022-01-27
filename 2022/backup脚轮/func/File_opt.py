import datetime,os,time,sys,shutil
from func.tools import *
from func.Write_log import Write_log
from func.param import *

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

    try:
        shutil.copy2(file, dest_path)
        time.sleep(sleepms)
        print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        Write_log("copying " + file + ' to ' + dest_path)
    except Exception:
        print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        Write_log("copying " + file + ' to ' + dest_path + ' error: 源文件找不到 或其他错误')


def Delete_file(filelists):
    # 删除文件列表,每删除一个文件,都休息delete_onefile_sleep时间
    sleepms = Get_value("delete_onefile_sleep")

    # 逐一删除文件
    for file in filelists:
        try:
            os.remove (file)
            time.sleep(sleepms)
            Write_log('deleting file ' + file + ' ...')
            print('deleting file ' + file + ' sleep:' + str(sleepms) + ' ...')
        except Exception as e:
            print(e)

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



def Delete_folder(path):
    # 如果上面文件都删除了，那就把目录也删除掉
    if os.path.isdir(path):
        try:
            os.rmdir(path)  # 删空目录,如果目录里文件不空,则不能删除
            print('deleting folder ' + path + ' ...')
            Write_log('deleting folder ' + path)
        except Exception as e:
            #print(e)
            Write_log(e)

# 获取目标目录里最小日期
def min_day():
    sourcePath = Get_value("source_path")
    folders1,files = current_folder(sourcePath)
    if folders1:
        folders1.sort()
        folders2,files = current_folder(folders1[0])
        if folders2:
            folders2.sort()
            folders3, files = current_folder(folders2[0])
            if folders3:
                folders3.sort()
                return folders3[0]
            else:
                return folders2[0]
        else:
            return folders1[0]


    print('min_day：目录不含年月日层次！程序将休眠一段时间后再次启动，请不要关闭！')
    return False

def delete_path(rootDir):

    # 如果是保护目录，则返回
    protectdays = Get_copy_dates(Get_value("backup_days"))
    print('-------------------------------------------------------------')
    print(protectdays)
    print(rootDir)
    for protectday in protectdays:
        if protectday in rootDir:
            print(rootDir,protectday,'目录保护')
            return

    mindaypath = min_day()
    if mindaypath:
        minday = mindaypath.replace(r's:\训练数据\test' + '\\', '')
        mindayfilename = minday.split('\\')
        print(minday)
        if mindaypath == rootDir and len(mindayfilename)==3:
            # 压缩
            command = Get_value("rarpath") + ' a -md5 ' + os.path.join(Get_value("compress_path"),mindayfilename[0] + mindayfilename[1] + mindayfilename[2] + '.rar') + ' ' + mindaypath
            #command = Get_value("rarpath") + ' a -md5 ' + os.path.join(mindaypath[:-2],mindayfilename[0] + mindayfilename[1] +mindayfilename[2] + '.rar') + ' ' + mindaypath
            print('\n',command)
            os.system(command)
        #Delete_folder(rootDir)
            folders, files = current_folder(rootDir)

            Delete_file(files)
            if folders:
                for folder in folders:
                    delete_path(folder)
            else:
                # 删除空目录
                Delete_folder(rootDir)
        else:
            folders, files = current_folder(rootDir)

            if folders:
                for folder in folders:
                    delete_path(folder)
            else:
                # 删除空目录
                Delete_folder(rootDir)
    else:
        return False








