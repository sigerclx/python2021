import time,sys
import backup5.mainclass.backup
import schedule
# 编译方法：D:\Python\python2021\2022>pyinstaller -F backup5\bak.py
# 如上：编译需要带路径，不能在程序文件所在文件夹编译，再上一级才行

backupinfo = backup5.mainclass.backup.BackupRules()

#backupinfo.scanfolder是函数, backupinfo.sourcePath是函数的参数,scanfolder是备份文件功能
if backupinfo.backupMethod ==1:
    #schedule.every(backupinfo.scanTimes).seconds.do(backupinfo.backupfolder, backupinfo.sourcePath)
    backfunction = backupinfo.backupfolder
if backupinfo.backupMethod ==2:
    #schedule.every(backupinfo.scanTimes).seconds.do(backupinfo.compressfolder, backupinfo.sourcePath)
    backfunction = backupinfo.compressfolder


backfunction(backupinfo.sourcePath)
i = 1

while backupinfo.alwaysScan==True:
    i +=1
    print('第',i,'次扫描')
    backfunction(backupinfo.sourcePath)
    time.sleep(backupinfo.delayTime)





