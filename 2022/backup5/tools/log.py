import datetime
# 登记log日志的函数
def write_log(str1,timelog='ON',file='date'):
    if file=='date':
        logfile = (datetime.datetime.now()).strftime("%Y-%m-%d")+ '.txt'
    else:
        logfile = 'configNG.ini'

    fileList = open(logfile, mode='a', encoding='utf-8')
    if timelog=='ON':
        logtime = (datetime.datetime.now()).strftime("%Y-%m-%d %H-%M-%S") + " "
    else:
        logtime = ""

    fileList.writelines(logtime+str(str1)+"\n")
    fileList.close()
