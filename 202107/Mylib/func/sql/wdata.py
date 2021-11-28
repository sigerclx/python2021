import sys
sys.path.append(r'D:\Python\python-book03\2021\topJijin\myclass')
import mssql
import pandas as pd
from pandas import DataFrame, Series
import pymssql
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine
import math
import os

def eachFile(filepath,ext='.txt'):
    '''
    遍历指定目录，显示目录下的所有文件名
    :param filepath:
    :return:
    '''
    fileList = []
    pathDir = os.listdir(filepath)
    for allFile in pathDir:
        child = os.path.join(filepath, allFile)
        if ext in child.lower():
            fileList.append(child)
    return fileList


def SaveDataFrame(filename):
        '''
        根据文件路径，取得该文件名称，基金数据起始日期，结束日期
        :param filename:
        :return:
        '''
        #ms = myclass.mssql.MSSQL(host="192.168.3.12", user="sa", pwd="Lun123456", db="Jdata")

        #conn = pymssql.connect(server="192.168.3.12", user="sa", password="Lun123456", database="Jdata")
        engine = create_engine('mssql+pymssql://sa:Lun123456@192.168.3.12/Jdata')

        jijinDF = pd.read_csv(filename, header=None,)

        tmp1 = filename.split('\\')
        jijinNO = tmp1[-1].replace('.txt', '')
        record = len(jijinDF)
        print(jijinNO,record)
        # 设定基金列名，对应数据表的字段名
        jijinDF.columns=['date', 'jingzhi', 'leijijingzhi', 'zhangfu', 'statusBuy','statusSell','remark']

        col_name = jijinDF.columns.tolist()  # 将jijinDF的列名全部提取出来存放在列表里
        col_name.insert(0, 'no')  # 在列索引为0的位置插入一列,列名为:no，刚插入时不会有值，整列都是NaN
        jijinDF = jijinDF.reindex(columns=col_name)  # DataFrame.reindex() 对原行/列索引重新构建索引值
        jijinDF['no'] = jijinNO  #整列都等于基金编号
        # 在此处可以将处理好的数据一次写入数据库
        jijinDF.to_sql('A_Data' ,engine, index=False,if_exists='append',dtype={'no':sqlalchemy.types.NVARCHAR(),'date': sqlalchemy.types.NVARCHAR(),'jingzhi':sqlalchemy.types.FLOAT(),'leijijingzhi':sqlalchemy.types.FLOAT(),'zhangfu':sqlalchemy.types.NVARCHAR() ,'statusBuy':sqlalchemy.types.NVARCHAR(), 'statusSell':sqlalchemy.types.NVARCHAR(), 'remark':sqlalchemy.types.NVARCHAR() })


#file = '..\data\000001.txt'
#SaveDataFrame(file)

allFileName = eachFile(r'data')
for file in allFileName:
    SaveDataFrame(file)