# -*- coding:utf-8 -*-# psutil 模块需另行安装
import psutil,datetime
import os,time
from func.lib import writelog,getConfig
from func.globalValue import Set_value,Get_value
from func.pchealth import Computerinfo
import multiprocessing


if __name__ == '__main__':
    getConfig()
    #cpu_core_num = multiprocessing.cpu_count()
    #print('he=',cpu_core_num)
    print(Get_value('program'))
    computerinfo = Computerinfo()
    while True:
        computerinfo.getprocess()
        processinfo = computerinfo.findpid(Get_value('program'))
        pcinfo = computerinfo.pcinfo()
        print(pcinfo)
        writelog(pcinfo)
        if processinfo:
            print(processinfo)
            writelog(processinfo)
        else:
            print(Get_value('program'),'is quit .')
            writelog(Get_value('program'),'is quit .')


