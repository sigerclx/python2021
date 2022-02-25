import os,sys,shutil,time
import tools.file,tools.log
import rules.judgerules
import tools.valueforever

def copy_file(file,backupinfo):


    # 每拷贝一个文件休息copy_onefile_sleep时间
    sleepms = backupinfo.onefileSleep

    dest_file = file.replace(backupinfo.sourcePath, backupinfo.destionPath)
    dest_path = dest_file[0:dest_file.rfind("\\")]

    # 目标文件夹不存在,则建立
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
        #Write_log(dest_path + " Created ")

    try:
        shutil.copy2(file, dest_path)
        time.sleep(sleepms)
        print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        tools.log.write_log("copying " + file + ' to ' + dest_path)
    except Exception as e:
        print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        tools.log.write_log('rules.operaterules.copy_file: '+ " Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        tools.log.write_log(e)


def move_file(file,backupinfo):
    copy_file(file,backupinfo)
    # copy后正常检测文件存在后，再删除源文件
    if rules.operaterules.__destion_file_exist(file,backupinfo):
        rules.operaterules.delete_sourcefile(file,backupinfo)



def __destion_file_exist(file,backupinfo):
    dest_file = file.replace(backupinfo.sourcePath, backupinfo.destionPath)
    return rules.judgerules.fileexist(dest_file)

def delete_sourcefile(file,backupinfo):
    # 删除文件列表,每删除一个文件,都休息delete_onefile_sleep时间
    sleepms = backupinfo.onefileSleep
    try:
        os.remove (file)
        time.sleep(sleepms)
        tools.log.write_log('deleting file ' + file + ' ...')
        print('deleting file ' + file + ' sleep:' + str(sleepms) + ' ...')
    except Exception as e:
        tools.log.write_log('rules.operaterules.delete_sourcefile:'+ ' deleting file ' + file + ' sleep:' + str(sleepms) + ' ...')
        tools.log.write_log(e)
        print(e)

