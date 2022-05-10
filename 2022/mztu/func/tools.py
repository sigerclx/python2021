import datetime
import time
import os,configparser
import glob
import sys
from func.globalValue import *

def recordLog(strmsg,filename='answer.log'): #把strmsg写入日志
    try:
        logFile = open(filename,'a')
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write(strmsg+'\n')
    except Exception as err:
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write('log write err:'+str(err)+'\n')
        pass
    finally:
        logFile.close()
    return

#获得当前日期
def get_day():
    ct = time.time()
    local_time = time.localtime(ct)
    hourtime = time.strftime("%Y-%m-%d", local_time)
    return hourtime

#比较两个日期
def day_cmp(first_time, second_time):
    
    if (first_time==0) or (second_time==0):
        return 0
    #if first_time<second_time:
    #   first_time, second_time = second_time, first_time
    return (datetime.datetime.strptime(first_time,"%Y-%m-%d") - datetime.datetime.strptime(second_time,"%Y-%m-%d")).days


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def get_hour():
    ct = time.time()
    local_time = time.localtime(ct)
    hourtime = time.strftime("%H:%M:%S", local_time)
    return hourtime	

def time_cmp(first_time, second_time):
    
    if (first_time==0) or (second_time==0):
        return 0
    if first_time<second_time:
       first_time, second_time = second_time, first_time
    return (datetime.datetime.strptime(first_time,"%H:%M:%S") - datetime.datetime.strptime(second_time,"%H:%M:%S")).seconds


# 获取目录文件列表,如果传递进来是一个文件也可以
def get_file_list(source_path):
    files_list=[]
    if os.path.isfile(source_path):
        files_list.append(source_path)
        return files_list

    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
    return files_list

def writelisttohtml(mylist,htmlfile):
    #htmlfile = configRead.readConfig('parameter','webfile')

    try:
        webUrlFile=open(htmlfile,'w',encoding='utf-8')
    except Exception as err:
        recordLog(str(err))
        return
        
    try:
        webUrlFile.write(r'''
                
    <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                </head>
                <style type=text/css>
                table.gridtable
                        {
                                font-family: verdana,arial,sans-serif;
                                font-size:14px;
                                color:#333333;
                                border-width: 1px;
                                border-color: #666666;
                        }
                table.gridtable th {
                                border-width: 1px;
                                padding: 1px;
                                border-style: solid;
                                border-color: #666666;
                                background-color: #dedede;
                        }
                table.gridtable td {
                                border-width: 1px;
                                padding: 6px;
                                border-style: solid;
                                border-color: #666666;
                                background-color: #ffffff;}
                                
                </style>''')

        webUrlFile.write('<h2>'+get_time_stamp()+'</h2>\n')
        webUrlFile.write('\n<table class=gridtable align=\'left\'>\n')

        for t1 in mylist:
                webUrlFile.write('<tr>')
                for t2 in t1:
                        webUrlFile.write('<td>'+str(t2)+'</td>')
                webUrlFile.write('<tr>\n')
        webUrlFile.write('</table>')
    except Exception as err:
            recordLog("write to html errors")
            recordLog(str(err))
    finally:
            webUrlFile.close()




#a1='17:05:05'
#a2=get_hour()
#print(time_cmp(a1,a2))
