#from 下载小说.searchengine.search  import Search
# 小说下载第二版，多进程版
# https://www.shuquge.com/ 下载的小说站
from multiprocessing import Manager,freeze_support
from novel.mainclass import Procedure
import sys

# 针对 www.0794.org的小说下载
def main():

    freeze_support() # 消除多进程的BUG : 每个进程都会出现小说名称输入提示

    downloadProcedure =  Procedure('www.0794.org')
    if downloadProcedure.search_novel():
        downloadProcedure.get_novel_list()
        downloadProcedure.mutiprocess_down(10)

if __name__ == '__main__':
    main()


