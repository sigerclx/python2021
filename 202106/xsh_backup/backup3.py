import time
from func.tools import *
from func.Init import *
from func.Write_log import Write_log
from func.param import *
from func.File_opt import *
# 定义复制扩展名

# 馨思海 程序备份


def main():
    Param_init()
    ini_init()
    Write_log('馨思海备份第一版 2021-06-16\n')

    times = 0
    while True:
        times+=1
        Write_log(str(times)+'次：')
        # 检查源目录和目标目录是否存在
        Read_folder()
        Scan_path(Get_value('source_path'))
        print('第'+str(times)+'次：'+'备份清理已经完成')
        # Delete_path(source_path,delete_before_days)
        # print(times,'清理已经完成')
        time.sleep(Get_value("sleeptime"))
        print('sleep :'+str(Get_value("sleeptime"))+' s ')

if __name__ == '__main__':
    main()