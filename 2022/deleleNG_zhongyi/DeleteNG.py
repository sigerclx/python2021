import os,sys,time
import datetime
import configparser
#读取ini方法
def read_ini(inivaluse,inikey='param'):
        config = configparser.ConfigParser()
        config.read("configNG.ini",encoding="utf-8-sig")
        try:
            convaluse=config.get(inikey,inivaluse)

            return convaluse
        except Exception as err:
            print(err)

# 获取当前目录下的文件和目录，当前层，不含子目录。默认同时返回目录和文件列表
def folderlist(folder):
    if not os.path.exists(folder):
        print("目标文件夹 : %s 不存在 ！" % folder)
        Write_log("目标文件夹  不存在 ！ " + folder, configfile="NG.txt")
        sys.exit(1)
    folderlists =[]

    for file in os.listdir(folder):
        file = os.path.join(folder,file)
        if os.path.isdir(file):
            folderlists.append(file)
    return folderlists

# 获取当前目录下的文件和目录
def folderfilelist(folder):
    folderlists =[]
    filelists = []

    for file in os.listdir(folder):
        file = os.path.join(folder,file)
        if os.path.isdir(file):
            folderlists.append(file)
        else:
            filelists.append(file)

    return filelists,folderlists


def Delete_folderAndfile(path):
    filelists,folderlists = folderfilelist(path)
    for file in filelists:
        try:
            print('deleting file in NG folder ' + path + file+' ...')
            os.remove(file)
            Write_log('deleting file in NG folder ' + path+ file, configfile="NG.txt")
            time.sleep(0.02)
        except Exception as e:
            print("删除出错了！: ",e)
            Write_log(e, configfile="NG.txt")

    for folder in folderlists:
        Delete_folderAndfile(folder)
    # 如果上面文件都删除了，那就把目录也删除掉
    if os.path.isdir(path):
        try:
            os.rmdir(path)  # 删空目录,如果目录里文件不空,则不能删除
            print('deleting NG folder' + path + ' ...')
            Write_log('deleting folder ' + path,configfile="NG.txt")
        except Exception as e:
            #print(e)
            Write_log(e,configfile="NG.txt")

def scan_folder(folder):
    folderlists = folderlist(folder)

    for folder in folderlists:
        print("scan folder :" ,folder)
        nopathfolder = folder.split('\\')[-1]
        if nopathfolder.upper() == "NG":
            Delete_folderAndfile(folder)
            continue
        scan_folder(folder)

def Write_log(str1,timelog='ON',configfile='date'):
    if configfile=='date':
        logfile = (datetime.datetime.now()).strftime("%Y-%m-%d")+ '.txt'
    else:
        logfile = configfile

    fileList = open(logfile, mode='a', encoding='utf-8')
    if timelog=='ON':
        logtime = (datetime.datetime.now()).strftime("%Y-%m-%d %H-%M-%S") + " "
    else:
        logtime = ""

    fileList.writelines(logtime+str(str1)+"\n")
    fileList.close()

if __name__ == '__main__':
    # 删除目标文件夹里的所有名字为NG的目录
    dest_folder = read_ini(r"NGdestion_path")
    scan_folder(dest_folder)



