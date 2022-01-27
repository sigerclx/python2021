import time,sys,os
from func.tools import *
from func.Init import *
from func.Write_log import Write_log
from func.param import *
from func.File_opt import *
# 定义复制扩展名


def main():
    Param_init()
    ini_init()   # 读取config.ini
    Write_log('脚轮压缩清理第一版 2022-01-24\n')


    Read_folder()

    protectdays = Get_copy_dates(Get_value("backup_days"))
    times = 0
    while True:
        times += 1
        print('第',str(times) + '次：压缩扫描')
        Write_log(str(times) + '次：')
        # 检查源目录和目标目录是否存在
        Read_folder()

        while True:
            # 获取最小日期
            # mindayPath = min_day()
            # minday = mindayPath.replace(Get_value('source_path') + '\\', '')
            if not delete_path(Get_value("source_path")):
                break

        print('sleep :' + str(Read_ini('scantime')) + ' s ')
        time.sleep(Get_value("scantime"))






if __name__ == '__main__':
    main()