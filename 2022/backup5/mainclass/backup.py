import backup5.tools.file
import backup5.rules.judgerules
import backup5.rules.operaterules
import backup5.tools.valueforever
import backup5.tools.ini

## 为备份而存在的类
class BackupRules:
    def __init__(self):
        # source_path=D:\picdata  是要清理的存放数据的根目录，下面是 年\月\日 形如： 2021\01\01，非规范日期目录不清理
        # destion_path = e:\compress 文件备份或压缩后存储的路径
        # protect_Days =30  当backup_method=1时，保留protect_Days天的数据不删除。#当backup_method=2时，压缩源目录到目标目录。
        # delete_onefile_sleep = 0.01 每删除一个文件，休息0.01秒，防止磁盘过度占用
        # alwaysscan = False 程序执行次数：True一直一轮轮扫描不中断，False就是执行1次
        # delay_time = 10 每循环执行一次，程序休眠的时间，alwaysscan =True时有意义
        # backupmethod 1 是备份到目标文件夹后，删除源文件及文件夹。2是压缩protect_Days内日期目录(或其子文件夹)到指定文件夹，源文件不动
        # important_folder = sample | images   日期目录下可以有重点关注的文件夹名称，目前只支持压缩时使用。important_folder为False时,不带引号，针对日期目录的整个目录
        self.sourcePath = backup5.tools.ini.read_ini('source_path')
        self.destionPath = backup5.tools.ini.read_ini('destion_path')
        self.destionShortPath = self.destionPath[self.destionPath.rfind("\\")+1:]
        self.protectDays = int(backup5.tools.ini.read_ini('protect_Days'))
        self.onefileSleep = float(backup5.tools.ini.read_ini('onefile_sleep'))
        self.delayTime = eval(backup5.tools.ini.read_ini('delay_time'))
        self.alwaysScan = backup5.tools.ini.read_ini('alwaysscan')
        self.backupMethod = eval(backup5.tools.ini.read_ini('backup_method'))
        self.rarPath = backup5.tools.ini.read_ini('rar_path')
        if backup5.tools.ini.read_ini('important_folder')!='False':
            self.importantFolders = backup5.tools.ini.read_ini('important_folder').split('|')
        else:
            self.importantFolders =False

    def showPath(self):
        print(self.sourcePath,self.destionPath)

    def backupfolder(self,current_folder):
        #获取当前目录的文件列表和目录列表
        files, folders = backup5.tools.file.folderfilelist(current_folder)
        # 目录为日期类

        # 处于保护日期范围的，不进行动作
        if not backup5.rules.judgerules.protectdays(current_folder,self):
            for file in files:
                backup5.rules.operaterules.move_file(file, self)
            backup5.tools.file.delete_folder(current_folder)

        for folder in folders:
            self.scanfolder(folder)


    def compressfolder(self,current_folder):
        # 处于要压缩的日期范围的，进行压缩处理
        if backup5.rules.judgerules.compressdays(current_folder,self):
            #print('符合压缩要求')
            # 判断目标目录里是否已经有压缩文件了。
            # 压缩
            backup5.rules.operaterules.compress_important_folder(current_folder,self)
            return

        # 获取当前目录的文件列表和目录列表
        files, folders = backup5.tools.file.folderfilelist(current_folder)

        for folder in folders:
            self.compressfolder(folder)

