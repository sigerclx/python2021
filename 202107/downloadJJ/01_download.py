import pandas as pd
import jjclass.jijin
from func.downloadengine.search import Search,Ttjj_namelist
from sql.tomssql import Write_df
import numpy as np
from sql.mssql import MSSQL

''' 新版下载基金的程序 2021-7-23
1、可以从网上下载基金列表
2、根据基金列表更新数据库，再到网上依次下载基金数据
3、把每个下载到的基金数据更新到数据库中。不会覆盖老数据，自动下载差异天数的数据 
'''

def main():
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)

    # 清洗并下载基金名录，存入文件data/base/nolist.txt
    namelist = Ttjj_namelist()
    jjnolist = namelist.get_nolist()
    wrtie_df_to_db  = Write_df()
    wrtie_df_to_db.write_jjlist(jjnolist)

    mssql = MSSQL(host="192.168.0.51",user="sa",pwd="a1b2/a",db="Jijin")
    jjnolist = mssql.ExecQuery("select * from all_nolist_date")

    # 调用多进程下载基金每日数据，第一个参数是数据下载目录，第二个参数为多进程的数目，默认为10
    jjclass.jijin.multProcess(jjnolist,'data',processCount=10)

if __name__ == '__main__':
    main()