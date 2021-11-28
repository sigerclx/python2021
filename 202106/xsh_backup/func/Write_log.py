import datetime
# 登记log
def Write_log(str1,timelog='ON',configfile='date1'):
    if configfile=='date':
        logfile = (datetime.datetime.now()).strftime("%Y-%m-%d")+ '.txt'
    else:
        logfile = 'log.txt'

    fileList = open(logfile, mode='a', encoding='utf-8')
    if timelog=='ON':
        logtime = (datetime.datetime.now()).strftime("%Y-%m-%d %H-%M-%S") + " "
    else:
        logtime = ""

    fileList.writelines(logtime+str(str1)+"\n")
    fileList.close()