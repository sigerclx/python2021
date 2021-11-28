import psutil
from func.globalValue import Set_value,Get_value
from func.lib import writelog



class Computerinfo(object):
    def __init__(self):
        # 所有的进程列出来
        self.pl = psutil.pids()
        self.second = Get_value('second')

    def getprocess(self):
        self.pl = psutil.pids()

    def pcinfo(self):
        line =[]
        mem = psutil.virtual_memory()  # - ---》监控物理内存
        disk = psutil.disk_usage(r'c:')  # - ---》监控硬盘
        cpu = psutil.cpu_percent(1)  # - ----》cpu使用率监控
        line.append('Cpu='+str(cpu))
        line.append('Mem=' +  str(mem[2]))
        line.append('diskC=' + str(disk[3]))
        return line

    def findpid(self,name):
        line=[]
        for pid in self.pl:
            try:
                self.process = psutil.Process(pid)
            except Exception:
                writelog('NoSuchProcess:' +name)
                return False

            if  self.process.name()==name :
                #print(pinfo)
                line.append(self.process.pid)
                line.append(self.process.name())

                line.append(self.process.is_running())
                line.append(self.process.status())
                line.append(self.process.cpu_percent(interval=1))
                line.append(str(round(self.process.memory_percent(), 2)))
                return line
        return False