#from 下载小说.searchengine.search  import Search
# 小说下载第二版，多进程版
# https://www.shuquge.com/ 下载的小说站
from multiprocessing import Manager,freeze_support
from novel.mainclass import Procedure

def main():

    #global downloadProcedure
    freeze_support() # 消除多进程的BUG : 每个进程都会出现小说名称输入提示
    #sharenovelname = Manager().list()
    #sharenovelname.append(input('请输入小说名称(eg:三寸人间/1480)：'))
    downloadProcedure =  Procedure()
    if downloadProcedure.search_novel():
        downloadProcedure.get_novel_list()
        downloadProcedure.mutiprocess_down(20)

if __name__ == '__main__':
    main()


