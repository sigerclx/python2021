from func.Write_log import Write_log
from func.tools import *
import os

def Read_folder():
    source_path = r'' + Read_ini('source_path')  # 定义源文件夹
    dest_path = r'' + Read_ini('dest_path')  # 定义目的文件夹
    while not os.path.exists(source_path) or not os.path.exists(dest_path) :
        if not os.path.exists(source_path):
            print('源目录 '+source_path+' 不存在!')
            Write_log('源目录 '+source_path+' 不存在!')
        if not os.path.exists(dest_path):
            print('目标目录 '+dest_path+' 不存在!')
            Write_log('目标目录 '+dest_path+' 不存在!')
        time.sleep(eval(Read_ini("scanfoldertime")))

def ini_init():
    # 首先判断config.ini 在不在,不在就创建一个,就是为了方便.
    if not os.path.exists('config.ini'):
        Write_log("[param]",timelog='off',configfile='config')
        Write_log(r"source_path = d:\pic1", timelog='off',configfile='config')
        Write_log(r"dest_path = y:\pic1", timelog='off',configfile='config')
        # 该参数是保留最近多少天delete_before_days的数据
        Write_log("delete_before_days = 20", timelog='off',configfile='config')
        # 每次copy,清理后休息sleeptime时间
        Write_log("sleeptime = 5 * 2", timelog='off',configfile='config')
        # 每次开始copy,清理前如果 源文件夹和目的文件夹不在,则报错,过scanfoldertime时间后,再测一遍
        Write_log("scanfoldertime = 5 * 2", timelog='off', configfile='config')
        # 每删除一个文件休息delete_onefile_sleep时间
        Write_log("delete_onefile_sleep = 0.01", timelog='off', configfile='config')
        # 每拷贝一个文件休息copy_onefile_sleep时间
        Write_log("copy_onefile_sleep = 0.01", timelog='off', configfile='config')

        Read_folder()

