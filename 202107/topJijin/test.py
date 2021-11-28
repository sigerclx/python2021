# coding:UTF-8
import sys
sys.path.append(r'/Volumes/Macintosh HD/Python/Source/2019/201912/Mforcast/myclass')
import calc_zhangfu
sys.path.append(r'/Volumes/Macintosh HD/Python/Source/2019/201912/Mforcast/lib')
import jackylib

from datetime import datetime

def main():

    # 调用多进程下载基金每日数据，第一个参数是数据下载目录，第二个参数为多进程的数目，默认为10
    #jijin.multProcess('data',10)
    # 根据data目录下已经下载的基金数据，建立带起始日期的基金基础数据，生成jijinListInfo.txt文件，放入base目录中
    #cr = jijininfo.createCSV('data')
    # 根据已经下载的基金（data目录），基金列表文件（base目录)，生成涨幅数据（zhangfu目录））
    calc_zhangfu.mutiProcess(15,'base','data','zhangfu')

    # starttime = datetime.now()
    # pdate = '2017-12-28'
    # period = [0, 7, 30, 90, 180, 360, 720]
    # one = calc_zhangfu.oneJijin(1)
    #
    # for i in range(100):
    #     date = jackylib.cha(pdate,i)
    #     print('date=',date)
    #     #aa = one.t_jingZhi(date)
    #     bb = one.t_periodJingzhi(date,period)
    #     #cc = one.periodJingzhi(date, period)
    #     print(bb)
    #     #print(cc)
    #
    #
    # endtime = datetime.now()
    # print(' 涨幅运行时间：', endtime - starttime, '\n')
    # print('涨幅计算完毕！')

if __name__ == '__main__':
    main()