import time
from func.tools import *
from func.Init import *
from func.Write_log import Write_log
from func.File_opt import *
# 定义复制扩展名

def main():
    ini_init()
    source_path = r''+Read_ini('source_path')    # 定义源文件夹
    dest_path = r''+Read_ini('dest_path')        # 定义目的文件夹
    delete_before_days = int(Read_ini('delete_before_days'))   # 删除delete_days之前源数据
    sleeptime = eval(Read_ini('sleeptime'))
    scanfoldertime = eval(Read_ini('scanfoldertime'))
    copy_onefile_sleep  = eval(Read_ini('copy_onefile_sleep'))


    times = 0
    while True:
        times+=1
        Write_log(str(times)+'次：')
        # 检查源目录和目标目录是否存在
        Read_folder()
        Copy_path(source_path, dest_path)
        print(times,'备份已经完成')
        Delete_path(source_path,delete_before_days)
        print(times,'清理已经完成')
        time.sleep(int(sleeptime))

if __name__ == '__main__':
    main()