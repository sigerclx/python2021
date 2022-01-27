from func.Write_log import Write_log
from func.tools import *
from func.param import *
import os

def Read_folder():
    source_path = Get_value('source_path')  # 定义源文件夹


    if not os.path.exists(source_path):
        print('源目录 '+source_path+' 不存在!')
        Write_log('源目录 '+source_path+' 不存在!')

def ini_init():
    # 首先判断config.ini 在不在,不在就创建一个,就是为了方便.
    if not os.path.exists('config.ini'):
        Write_log("[param]",timelog='off',configfile='config')
        Write_log(r"source_path = d:\pic1", timelog='off',configfile='config')
        Write_log(r"compress_path = d:\pic1", timelog='off', configfile='config')
        # 该参数是source_path 对应盘符的最小报警空间 GB为单位，5GB以下就要报警了
        Write_log("min_disk_spaceGB = 5", timelog='off',configfile='config')
        # 至少保留30天的数据不能删除，即便空间不足也不能删除
        Write_log("backup_days =30", timelog='off',configfile='config')
        # 每删除一个文件休息delete_onefile_sleep时间
        Write_log("delete_onefile_sleep = 0.01 ", timelog='off', configfile='config')
        Write_log("rarpath = 'C:\programe files\winrar\winrar.exe' ", timelog='off', configfile='config')


    Read_config()

def Read_config():
    Set_value('source_path', r'' + Read_ini('source_path'))  # 定义源文件夹
    Set_value('compress_path', r'' + Read_ini('compress_path'))  # 定义压缩目的文件夹
    Set_value('min_disk_spaceGB', int(Read_ini('min_disk_spaceGB')))
    Set_value('backup_days', eval(Read_ini('backup_days')))
    Set_value('scantime', eval(Read_ini('scantime')))
    Set_value('delete_onefile_sleep', float(Read_ini('delete_onefile_sleep')))
    Set_value('rarpath', Read_ini('rarpath'))
