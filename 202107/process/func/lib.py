import time
from func.globalValue import Set_value,Get_value
from func.configRead import readConfig

def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def writelog(strmsg,filename='pcinfo.txt'): #把strmsg写入日志
    try:
        logFile = open(filename,'a')
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write(str(strmsg)+'\n')
    except Exception as err:
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write('log write err:'+str(err)+'\n')
        pass
    finally:
        logFile.close()
    return

def getConfig():
    Set_value('program', readConfig('info', 'program'))
    Set_value('second',float(readConfig('info', 'second')))


