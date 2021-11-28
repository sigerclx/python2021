import re, sys, os
from datetime import datetime
import numpy as np
import pandas as pd

from base import downNoList

'''
根据基金数据目录的所有数据文件，生成基金编号，起始日，截止日的列表文件jijininfo.py
根据data目录下已经下载的基金数据，建立带起始日期的基金基础数据，生成jijinListInfo.txt文件，放入base目录中
如下即可使用生成文件
    cr = jijininfo.createCSV('data')
'''
class createCSV():
    def __init__(self,path='data'):
        starttime = datetime.now()
        self.path = path
        fileList = self.eachFile(path)
        #print(fileList[0])
        #print(fileList[1])
        #sys.exit(0)
        info = self.getManyJijinInfo(fileList)

        self.writeJinListFile(info)
        endtime = datetime.now()
        print('基金列表下载程序运行时间：', endtime - starttime, '\n')
        print('程序计算完毕！')

    def eachFile(self,filepath):
        '''
        遍历指定目录，显示目录下的所有文件名
        :param filepath:
        :return:
        '''
        fileList = []
        pathDir = os.listdir(filepath)
        for allFile in pathDir:
            child = os.path.join(filepath, allFile)
            fileList.append(child)
        return fileList

    def getOneJijinInfo(self,filename):
        '''
        根据文件路径，取得该文件名称，基金数据起始日期，结束日期
        :param filename:
        :return:
        '''
        line =[]
        jijinDF = pd.read_csv(filename, header=None,)
        tmp1 = filename.split('/')
        #jijinNO = '\''+tmp1[-1].replace('.txt', '')+'\''
        jijinNO = tmp1[-1].replace('.txt', '')
        info = self.getinfo(jijinNO)
        startDate = jijinDF.head(1).iloc[0, 0]
        endDate = jijinDF.tail(1).iloc[0, 0]
        #try:
        line.append(jijinNO)
        line.append(info[2])
        line.append(info[3])
        line.append(startDate)
        line.append(endDate)
        #except Exception as err:
        #    print(jijinNO)
        return line

    def getManyJijinInfo(self,fileList):
        info = []
        for i in fileList:
            print(i,type(i))
            if "txt" in i.lower():
                tmp = self.getOneJijinInfo(i)
                #print(tmp[0])
                info.append(tmp)
        info = pd.DataFrame(np.array(info),columns=['No','name','type','startDate','endDate'])
        return info

    def writeJinListFile(self,info):
        jijinDF = info.sort_values(by=['No'], axis=0, ascending=True)
        jijinDF.to_csv(os.path.join('base','jijinListInfo.txt'), sep=',', header=True, index=False, mode='w')

    def getinfo(self,No):
        for i in downNoList.jijin:
            if No == i[0]:
                return i