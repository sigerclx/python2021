# -*- coding:utf-8 -*-# psutil 模块需另行安装
import psutil,datetime
import os,time
from func.lib import writelog,getConfig
from func.configRead import readConfig
from func.globalValue import Set_value,Get_value

def millis(t1, t2):
    micros = (t2 - t1).microseconds
    #print("micros: ",micros)
    #delta = micros/1000
    return micros

def get_use():

    while True:
        #t1 = datetime.datetime.now()
        mem = psutil.virtual_memory() #- ---》监控物理内存

        disk = psutil.disk_usage(r'c:') #- ---》监控硬盘

        cpu = psutil.cpu_percent(1) #- ----》cpu使用率监控
        print('\n你的cpu情况还行噢,已经使用了%s' % cpu)
        print('你的物理内存顶不住了，占用率为%s' % mem[2])
        print('你的C盘里放了多少资源啊，使用率高达%s' % disk[3])

        #t2 = datetime.datetime.now()

        #print('time=',millis(t1,t2))

        time.sleep(1) #睡三秒


def checkprocess():
    # --获取进程信息--
    pl = psutil.pids()  #所有的进程列出来

    # # --获取CPU的信息--
    # cpu_count = psutil.cpu_count()  # CPU逻辑数量
    # cpu_times = psutil.cpu_times()  # 统计CPU的用户 I 系统 J 空闲时间
    #
    # # --获取系统负载--
    # getloadavg = psutil.getloadavg()    # 分别表示 1 分钟， 5 分钟， 15 分钟的系统负载情况
    #
    # # --获取内存信息--
    # virtual_memory = psutil.virtual_memory()   #获取物理内存的大小
    # swap_memory = psutil.swap_memory()  #获取交换内存的大小
    #
    # # --获取磁盘分区，磁盘使用率和磁率IO信息--
    # disk_partitions = psutil.disk_partitions()
    #
    # print(cpu_times,getloadavg,virtual_memory,swap_memory,disk_partitions)


    for pid in pl:
        process = psutil.Process(pid)
        print(pid,process.name(),'cpu=',process.cpu_percent(),'mem=',process.memory_percent())
        print('\n\n')






if __name__ == '__main__':
    getConfig()
    print(Get_value('program'))

    while True:
        processinfo = findpid(Get_value('program'))
        print(processinfo)
        writelog(processinfo)
        time.sleep(Get_value('second'))