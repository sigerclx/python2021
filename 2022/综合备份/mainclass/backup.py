import tools.file
import rules.judgerules
import rules.operaterules
import tools.valueforever
import tools.ini

class BackupRules:
    def __init__(self):

        self.sourcePath = tools.ini.read_ini('source_path')
        self.destionPath = tools.ini.read_ini('destion_path')
        self.protectDays = int(tools.ini.read_ini('protect_Days'))
        self.onefileSleep = float(tools.ini.read_ini('onefile_sleep'))
        self.scanTime = eval(tools.ini.read_ini('scan_time'))

    def showPath(self):
        print(self.sourcePath,self.destionPath)

    def scanfolder(self,current_folder):
        #获取当前目录的文件列表和目录列表
        files, folders = tools.file.folderfilelist(current_folder)
        # 目录为日期类

        # 处于保护日期范围的，不进行动作
        if not rules.judgerules.protectdays(current_folder,self):
            for file in files:
                rules.operaterules.move_file(file, self)
            tools.file.delete_folder(current_folder)

        for folder in folders:
            self.scanfolder(folder)

