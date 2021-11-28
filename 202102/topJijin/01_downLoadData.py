# coding:UTF-8
import sys,os
import pandas as pd
sys.path.append(r'/Volumes/Macintosh HD/Python/Source/2019/201912/Mforcast/myclass')
import myclass.jijin
import myclass.jijininfo
import myclass.calc_zhangfu
import myclass.yuce

def main():
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 调用多进程下载基金每日数据，第一个参数是数据下载目录，第二个参数为多进程的数目，默认为10
    #myclass.jijin.multProcess('data',10)
    # 根据data目录下已经下载的基金数据，建立带起始日期的基金基础数据，生成jijinListInfo.txt文件，放入base目录中
    cr = myclass.jijininfo.createCSV('data')
    # 根据已经下载的基金（data目录），基金列表文件（base目录)，生成涨幅数据（zhangfu目录））
    #myclass.calc_zhangfu.mutiProcess(20,'base','data','zhangfu')



if __name__ == '__main__':
    main()