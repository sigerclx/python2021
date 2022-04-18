#from 下载小说.searchengine.search  import Search
# 小说下载第二版，多进程版
# https://www.shuquge.com/ 下载的小说站
from novel.mainclass import Procedure,mutiprocess_down

def main():

    global downloadProcedure
    downloadProcedure =  Procedure()

    if downloadProcedure.search_novel():
        downloadProcedure.get_novel_list()
        mutiprocess_down(downloadProcedure.zhanglist,downloadProcedure.name, 10)

if __name__ == '__main__':
    main()


