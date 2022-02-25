import time
import mainclass.backup
import schedule

backupinfo = mainclass.backup.BackupRules()

schedule.every(backupinfo.scanTime).seconds.do(backupinfo.scanfolder, backupinfo.sourcePath)

i=0
while True:
    i +=1
    schedule.run_pending()
    print('------ 第',i,'次 轮询检测：-------')
    time.sleep(2)





