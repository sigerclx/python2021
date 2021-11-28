import datetime,os,time,sys,shutil
from func.tools import *
from func.Write_log import Write_log

def Delete_file(path):
    # 删除目录下的文件,每删除一个文件,都休息delete_onefile_sleep时间
    sleepms = Read_ini("delete_onefile_sleep")
    source_path = Read_ini("source_path")
    dest_path = Read_ini("dest_path")

    files_list = Get_file_list(path)
    for i in files_list:
        # 源文件和目标文件都存在,才能删除源文件.
        if (os.path.exists(i) and os.path.exists(i.replace(source_path,dest_path))):
            try:
                os.remove (i)
                time.sleep(eval(sleepms))
                Write_log('deleting file ' + i + ' ...')
                print('deleting file ' + i + ' sleep:' + sleepms + ' ...')
            except Exception as e:
                print(e)
                continue


def Delete_path(source_path,delete_before_days):
    #获取源目录里需要保留（不能删除）的目录清单
    date_list = Get_copy_dates(delete_before_days, today=1)
    #获取源目录里所有的文件夹
    dir_list = Get_dir_list(source_path)

    for each_dir in dir_list:
        curr_path = each_dir.replace(source_path + "\\", "")
        # 不能删除 要保留 delete_before_days 天数的最近文件夹和文件
        if not any((s in curr_path or curr_path in s) for s in date_list):
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


def Copy_path(spath, dpath):
    # 将源文件夹复制到目标文件夹
    allpic_files = Get_file_list(spath)
    sleepms = Read_ini("copy_onefile_sleep")  # 每拷贝一个文件休息copy_onefile_sleep时间
    curr_date = (datetime.datetime.now()).strftime("%Y\%m\%d")
    # print(curr_date)
    for file in allpic_files:
        dest_file = file.replace(spath, dpath)
        dest_path = dest_file[0:dest_file.rfind("\\")]

        # 当日文件不删除
        if curr_date in file:
            continue

        # 目标文件夹不存在,则建立
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            Write_log(dest_path + " Created ")

        # 目标文件不存在,则拷贝备份
        if not os.path.exists(dest_file):
            try:
                shutil.copy2(file, dest_path)
                time.sleep(eval(sleepms))
                print("Copying " + file + ' to ' + dest_path + "sleep : " + str(sleepms) + '...')
            except Exception:
                print("Copying " + file + ' to ' + dest_path + "sleep : " + str(sleepms) + '...')
                Write_log("copying " + file + ' to ' + dest_path+' error: 源文件找不到 或其他错误')
                continue
            Write_log("copying " + file + ' to ' + dest_path)

    Write_log("备份完成")