import os,shutil,time
import backup5.tools.file
import backup5.tools.log
import backup5.rules.judgerules
import backup5.tools.valueforever

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
        backup5.tools.log.write_log("copying " + file + ' to ' + dest_path)
    except Exception as e:
        print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        backup5.tools.log.write_log('rules.operaterules.copy_file: '+ " Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        backup5.tools.log.write_log(e)


def move_file(file,backupinfo):
    copy_file(file,backupinfo)
    # copy后正常检测文件存在后，再删除源文件
    if backup5.rules.operaterules.__destion_file_exist(file,backupinfo):
        backup5.rules.operaterules.delete_sourcefile(file,backupinfo)



def __destion_file_exist(file,backupinfo):
    dest_file = file.replace(backupinfo.sourcePath, backupinfo.destionPath)
    return backup5.rules.judgerules.fileexist(dest_file)

def delete_sourcefile(file,backupinfo):
    # 删除文件列表,每删除一个文件,都休息delete_onefile_sleep时间
    sleepms = backupinfo.onefileSleep
    try:
        os.remove (file)
        time.sleep(sleepms)
        backup5.tools.log.write_log('deleting file ' + file + ' ...')
        print('deleting file ' + file + ' sleep:' + str(sleepms) + ' ...')
    except Exception as e:
        backup5.tools.log.write_log('rules.operaterules.delete_sourcefile:'+ ' deleting file ' + file + ' sleep:' + str(sleepms) + ' ...')
        backup5.tools.log.write_log(e)
        print(e)

def compress_folder(folder,backupinfo):
    # winrar a - md5  e:\test\02\1.rar  e:\test\01  压缩01目录到1.rar文件

    foldershortName = folder[folder.rfind("\\") + 1:]
    # 目标文件存在，不需要压缩
    if not os.path.exists(os.path.join(backupinfo.destionPath, foldershortName + '.rar')):
        command = backupinfo.rarPath + ' a -md5 ' + os.path.join(backupinfo.destionPath,
                                                               foldershortName + '.rar') + ' ' + folder
        print(command)
        os.system(command)
    else:
        print('压缩文件已经存在:',os.path.join(backupinfo.destionPath,foldershortName + '.rar'))


def compress_important_folder(folder,backupinfo):
    # winrar a - md5  e:\test\02\1.rar  e:\test\01  压缩01目录到1.rar文件
    foldershortName = folder[folder.rfind("\\") + 1:]
    if backupinfo.importantFolders!=False:
        for importantFolder in backupinfo.importantFolders:
            if os.path.exists(os.path.join(folder, importantFolder)):
                # 目标文件存在，不需要压缩
                if not os.path.exists(os.path.join(backupinfo.destionPath, foldershortName +'_'+importantFolder+'.rar')):
                    print('压缩子文件夹：',importantFolder)
                    command = backupinfo.rarPath + ' a -md5 ' + os.path.join(backupinfo.destionPath,
                                                                           foldershortName  +'_'+importantFolder+ '.rar') + ' ' + os.path.join(folder,importantFolder)
                    print(command)
                    os.system(command)
                else:
                    print('压缩文件已经存在:',os.path.join(backupinfo.destionPath,foldershortName  +'_'+importantFolder+ '.rar'))
            else:
                print('目标文件夹不存在:',os.path.join(folder, importantFolder))
    else:
        compress_folder(folder,backupinfo)