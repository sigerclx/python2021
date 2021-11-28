import os,time,shutil,datetime

def write_log(str1,timelog='ON',configfile='date'):
    if configfile=='date':
        logfile = (datetime.datetime.now()).strftime("%Y-%m-%d")+ '.txt'
    else:
        logfile = 'config.ini'

    fileList = open(logfile, mode='a', encoding='utf-8')
    if timelog=='ON':
        logtime = (datetime.datetime.now()).strftime("%Y-%m-%d %H-%M-%S") + " "
    else:
        logtime = ""

    fileList.writelines(logtime+str(str1)+"\n")
    fileList.close()

def copy_file(sourcefile,dest_path):
    sleepms = 0.01
    if os.path.exists(sourcefile):
        try:
            shutil.copy2(sourcefile, dest_path)
            time.sleep(sleepms)
            print("Copying " + sourcefile + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
            write_log("Copying " + sourcefile + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        except Exception:
            print("Copying " + sourcefile + ' to ' + dest_path + " is error!")
            write_log("Copying " + sourcefile + ' to ' + dest_path + " is error!")

def move_file(sourcefile,dest_path):
    sleepms = 0
    if os.path.exists(sourcefile):
        try:
            shutil.move(sourcefile, dest_path)
            #time.sleep(sleepms)
            print("Moving " + sourcefile + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
            write_log("Moving " + sourcefile + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        except Exception:
            print("Moving " + sourcefile + ' to ' + dest_path + " is error!")
            write_log("Moving " + sourcefile + ' to ' + dest_path + " is error!")

def create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)


