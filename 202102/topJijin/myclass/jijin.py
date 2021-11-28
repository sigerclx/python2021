# coding:UTF-8
import os, requests, re, sys, time
import numpy as np
from datetime import datetime
import datetime as date
import pandas as pd

'''
基金下载类，同时含有一个多线程函数，可以多线程下载基金数据，使用时直接调用多进程函数multProcess即可
调用多进程基金每日数据，第一个参数是数据下载目录，第二个参数为多进程的数目，默认为10
jijin.multProcess('data',20)
'''

sys.path.append(r'/Volumes/Macintosh HD/Python/Source/2019/201912/Mforcast/lib')
import jackylib

sys.path.append(r'/Volumes/Macintosh HD/Python/Source/2019/201912/Mforcast/base')
import downNoList

from multiprocessing import Process

class jijin(object):
    def __init__(self, datapth ,sdate='1980-01-01', edate='2099-01-01'):
        '''
        :param jijinNo: 基金编号

        '''
        self.__perPage = 40
        self.__records = 0
        self.__totalPages = 0
        self.__sdate = sdate
        self.__edate = edate
        self.__dataPath = datapth #jackylib.uppath('data')
        # 从静态文件中获取基金列表等信息
        self.__getjijinList()
        # self.downJijin()

    def __getjijinList(self):
        # 从jijinNolist.py 中取出基金编号的列表,含中文名称等
        jijinList = np.array(downNoList.jijin)
        self.jijinNos = list(jijinList[:, 0])  # 只要编号
        # jijinNos = jijinNos[7164:7364]
        self.jijinCount = len(self.jijinNos)

    def __filedate(self):
        # 判断文件是否存在，存在则打开文件判断，最后一行的最新数据日期，如果小于sdate，则可以正常追加，否则退出即可
        filename = os.path.join(jackylib.realpath(), self.__dataPath , self.__jijinNo + ".txt")
        #print(filename,os.path.exists(filename))
        endDate = []
        if os.path.exists(filename) == True:
            try:
                jijinDF = pd.read_csv(filename, header=None)
                endDate = jijinDF.tail(1).iloc[0, 0]
            except Exception as err:
                print('filedate出错了：', self.__jijinNo, err)
                return False

            if len(endDate) < 2:
                print('filedate出错了：', self.__jijinNo)
                return False
        else:
            return False
        return endDate

    def __geturlCode(self, page, fdtd):
        """
        获得天天基金API提供的基金按天的数据页面
        page ： 下载的页号
        """
        url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=' + self.__jijinNo + '&page=' + str(
            page) + '&per=' + str(self.__perPage) + '&sdate=' + str(fdtd) + '&edate=' + str(self.__edate)
        # print(url)
        try:
            res = requests.get(url)
        except Exception as err:
            print('geturlCode出错了：', self.__jijinNo, err)
            return 0
        pageStr = str(res.content, 'utf-8')
        return pageStr

    def __getlinesData(self, pageStr):
        """
        利用下载的数据页面根据<tr></tr>分出每一行，含<td>html代码
        """
        pat1 = '<tr>(.+?)</tr>'
        self.__linesData = re.findall(pat1, pageStr)
        return self.__linesData

    def __getData(self, linesData):
        """
        利用每一行含<td>html代码过滤每行的7个数据，最后一个分红字段可能为空
        """
        jijinData = np.array([])
        pat1 = re.compile('>(.*?)<')
        for i in linesData:
            s = re.findall(pat1, i)
            jijinData = np.append(jijinData, s[::2])
        return jijinData

    def __getinfo(self, pageStr):
        """
        利用每一行含<td>html代码过滤每行的7个数据，最后一个可能为空
        (?:xxxx) 是该分组不作为搜索结果集
        #在 records:4351,pages:871,curpage:1}; 里过滤
        """
        pat1 = '(?:records:)(.+?)(?:,pages:)(.+?)(?:,curpage:)(.+?)(};)'

        result = re.search(pat1, pageStr)
        recordsCount = result.group(1)
        recordsPages = result.group(2)
        self.__records = recordsCount
        self.__totalPages = recordsPages

        print('recordsCount =', recordsCount, 'recordsPages =', recordsPages, end='')
        # return recordsPages

    def downOne(self, jijinNo, processName):
        '''
        根据基金编号下载基金数据
        :return:
        '''
        self.__jijinNo = jijinNo
        print('进程', processName, " start downloading : ", self.__jijinNo, ' ', end='')

        mydate = self.__filedate()
        # print('mydate===', mydate)

        if mydate != False:
            if jackylib.diffdate(mydate, self.__edate) == True:
                # 如果文件现有数据的日期大于等于要下载的数据日期，则不需要下载
                return 0
            else:
                fdtd = str(jackylib.change_ymd(mydate) + date.timedelta(days=1))
        else:
            fdtd = self.__sdate

        pageStr = self.__geturlCode(1, fdtd)
        # pageStr = self.__geturlCode(1, '2019-01-01')
        #print("pageStr=",pageStr)
        if pageStr == 0:
            print(self.__sdate, ' - ', self.__edate, '......不需要下载')
            return

        self.__getinfo(pageStr)

        # print('p',pageStr)
        # 没有数据就继续下一个
        if (self.__records == '0'):
            print(" ...... 没有数据 ! \n")
            jackylib.writelog(self.__jijinNo, 'nodata.txt')
            return

        #  从最后一页self.__totalPages开始取数据

        jijinDF = pd.DataFrame(np.array([]))

        for j in range(int(self.__totalPages), 0, -1):
            print('page=',j)
            pageStr = self.__geturlCode(j, fdtd)
            if pageStr == 0:
                print(self.__sdate, ' - ', self.__edate, '......不需要下载')
                return
            linesData = self.__getlinesData(pageStr)
            #print('line=',linesData)

            # # 保险类基金编号写入文件，不下载数据
            # jackylib.writelog(self.__jijinNo, 'baoxian.txt')
            # print(" ...... bao xian ! \n")
            # return

            jijinData = self.__getData(linesData)

            #print('jijinData=', jijinData)
            # 验证jijinData是否符合规范
            jijinDFOne = self.__checkNpData(jijinData, j)
            #print('\njijinDFOne=', jijinDFOne)
            #print("len=",len(jijinDFOne))
            if len(jijinDFOne) > 0:
                jijinDF = jijinDF.append(jijinDFOne)
            else:
                print('jijinDF is empty：', self.__jijinNo)
                break
                #continue
        if len(jijinDF)>0:
            #保险类的直接退出，不生成文件
            self.__writeFile(jijinDF)
        # sys.exit(0)
        # starttime = datetime.now()

        # endtime = datetime.now()
        # print('运行时间：', endtime - starttime)

        # 可以下载到数据的基金编号写入文件
        # jackylib.writelog(self.__jijinNo, 'downLog.txt')
        print(" ...... finished ! \n")

    def downMany(self, nolist, processName="noProcess"):
        lines = len(nolist)
        count = 0
        for i in nolist:
            self.downOne(i, processName)
            count = count + 1
            print(processName, ' 完成进度 = ', count, '/', lines)
            if count == lines:
                print(processName, '进程已结束！')

    def __checkNpData(self, jijinData, currentPage):

        lie = 7

        if ('单位净值' not in jijinData):
            # 保险类基金处理,记录基金编号
            return ''
        if ('暂无数据' in jijinData):
            # 没数据
            return ''

        if (currentPage != int(self.__totalPages)):
            jijinData.shape = self.__perPage + 1, lie
        else:
            # 取数据是最后一页时
            # 当数据满页
            if ((int(self.__records) % self.__perPage) == 0):
                jijinData.shape = self.__perPage + 1, lie
            else:
                # 数据不满页
                try:
                    jijinData.shape = int(self.__records) % self.__perPage + 1, lie
                except Exception as err:
                    print('writefile出错了：', self.__jijinNo, currentPage)
                    print('基金数据：', jijinData)
                    return ''
        # axis：删除子数组的轴
        # axis = 0：表示删除数组的行
        # axis = 1：表示删除数组的列
        # axis = None：表示把数组按一维数组平铺在进行索引删除

        # 删除表头标题字段行
        jijinData = np.delete(jijinData, 0, axis=0)
        jijinDF = pd.DataFrame(jijinData)
        # self.__writeFile(jijinDF)

        return jijinDF

    def __writeFile(self, jijinDF):
        filename = self.__jijinNo + ".txt"

        # print('=====',jijinDF)
        # jijinDF=pd.DataFrame(jijinDF)
        try:
            jijinDF = jijinDF.sort_values(by=0, axis=0, ascending=True)
            jijinDF.to_csv(os.path.join(jackylib.realpath(), self.__dataPath , filename), sep=',', header=False, index=False, mode='a')
        except Exception as err:
            print('write file Err :', self.__jijinNo, err)


def multProcess(datapath='data',processCount=10):
    # 开始下载基金每日数据
    starttime = datetime.now()
    print("Starting analysis ( multProcess = ",processCount,' ) :')

    jijinDl = jijin(datapath)
    # processCount = 定义进程数
    # 按把基金的总数量分成进程数的份数，每个进程负责下载一份基金清单
    shang = int(jijinDl.jijinCount / processCount)
    yushu = int(jijinDl.jijinCount % processCount)
    print('y,s=', yushu, shang)

    downloadProcesses = []

    # 开始创建进程
    for j in range(processCount):
        x = shang * j
        y = shang * j + shang

        downloadProcess = Process(target=jijinDl.downMany, args=(jijinDl.jijinNos[x:y], str(j),))
        downloadProcesses.append(downloadProcess)
        downloadProcess.start()

    if yushu != 0:
        lastdownloadProcess = Process(target=jijinDl.downMany,
                                      args=(jijinDl.jijinNos[processCount * shang:], str(processCount),))
        downloadProcesses.append(lastdownloadProcess)
        lastdownloadProcess.start()
    # 等待所有进程结束
    for analyseProcess in downloadProcesses:
        analyseProcess.join()

    endtime = datetime.now()

    print('运行时间：', endtime - starttime)
    print("End of analysis.")


