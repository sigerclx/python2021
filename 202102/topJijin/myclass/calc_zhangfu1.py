import os, sys

sys.path.append(r'/Volumes/Macintosh HD/Python/Source/2019/201912/Mforcast/lib')
import jackylib
from datetime import datetime
import pandas as pd
from multiprocessing import Process, Manager


class oneJijin(object):
    def __init__(self, No, path='data'):
        self.No = str(No).zfill(6)
        self.path = path
        self.df2 = self.readJijin()

    def readJijin(self):
        # 按日期data获取基金no的对应的那一行
        filename = os.path.join(self.path, self.No + '.txt')
        # 这里注意没有表头header
        # print(filename)
        # sys.exit(0)
        self.jijinDF = pd.read_csv(filename, header=None)
        self.jijinDF.columns = ['date', 'net', 'addup', 'dailygain', 'status', 'redeem', 'bonus']
        # 获取基金的起始日期,结束日期
        self.startDate = self.jijinDF.head(1).iloc[0, 0]
        self.endDate = self.jijinDF.tail(1).iloc[0, 0]
        self.pointDateList = self.jijinDF['date'][1:]
        # 指定date为索引列
        # self.jijinDF.set_index('date',inplace = True)
        # return self.jijinDF[['No']]

    def getDate(self, date):
        dateWhat = self.jijinDF.loc[self.jijinDF['date'] == date]
        return dateWhat

    def jingZhi(self, pdate):
        dateValue = pd.DataFrame([], index=None)
        count = 0
        # 去对应日期的基金净值，如果日期找不到，则日期减1，继续找，直到找到为止。但日期出范围则返回0
        while dateValue.empty:
            if jackylib.diffdate(self.startDate, pdate):
                return
            date = jackylib.cha(pdate, count)
            # print('date=',date)
            dateValue = self.getDate(date)
            # print('dateValue',dateValue)
            if dateValue.empty == False:
                if dateValue['net'].empty:
                    dateValue = pd.DataFrame([], index=None)
                else:
                    jingZHI = dateValue['net'].values[0]
                    break
            count += 1  # 取不到数据，就向前顺延一天
        return jingZHI

    def periodJingzhi(self, date, period):
        '''
        根据pointDate构建按周期计算出的净值list
        # 不一定出具日期就一定有基金数据，没有数据的时候lines=''，所以要往前减一天顺延，直至有数据为止
        # 在周期外始终包含基金的起始日期的净值
        :return:净值list
        '''

        NoValues = []
        # print('%10s' % periodName, 'period = ', period, 'start ......')

        pDate = []
        # 根据周期长度，计算实际周期的具体日期
        for i in period:
            pDate.append(str(jackylib.cha(date, int(i))))
        # print(pDate)
        NoValues.append(self.No)
        NoValues.append(pDate[0])
        NoValues.append(self.jingZhi(self.startDate))  # 加上起始日净值
        # 这求得的列都为空就继续往前顺延一天，求净值数据，直到不为空
        for i in pDate:
            # 取得对应日期的基金净值数据行DF格式(如果对应日期找不到，则减一天继续，直到找到对应基金净值，最后都没找到则返回0)
            a1 = self.jingZhi(i)
            NoValues.append(a1)
        return NoValues

    def FDTD_pJingzhi(self, pointDateList, period):
        lines = []
        for pDate in pointDateList.values:
            #print(self.No, pDate)
            lines.append(self.periodJingzhi(pDate, period))
        return lines


class zhangfuCreate(object):
    def __init__(self, No,path='zhangfu',jijinPath='data'):
        self.period = [0, 7, 30, 90, 180, 360, 720, 1080, 1800,-7,-14,-21,-30,-90,-180,-360]
        self.periodNames = ['No', 'Date', 'startDate', 'today', '7', '30', '90', '180', '360', '720', '1080', '1800','N7','N14','N21','N30','N90','N180','N360']
        self.No = str(No).zfill(6)
        self.path = path
        self.jijinPath = jijinPath
        self.jijin = oneJijin(No,jijinPath)
        self.tillDate()
        self.periodFu()

    def tillDate(self):
        filename = self.No + '.csv'

        if os.path.exists(os.path.join(self.path, filename)):
            zhangfuFile = open(os.path.join(self.path, filename), 'r', encoding='utf-8')
            df = pd.read_csv(zhangfuFile, header=0)
            if (df.empty):
                self.tillNow = False
            else:
                date = df.tail(1).iloc[0, 1]
                self.tillNow = date
        else:
            self.tillNow = False

    def periodFu(self):
        # 获取对应涨幅文件，查询最后计算日期，补充计算涨幅数据
        if self.tillNow == False:
            # 如果基金涨幅数据为空，则需要从头计算涨幅数据
            pointDateList = self.jijin.pointDateList
        else:
            # 如果基金涨幅数据最后计算日期< 基金日数据最后日期，则构建计算涨幅的日期list
            pointDateList = self.jijin.pointDateList[self.jijin.pointDateList > self.tillNow]
        # print(pointDateList)
        # sys.exit(0)
        jingzhiList = self.jijin.FDTD_pJingzhi(pointDateList, self.period)
        df = pd.DataFrame(jingzhiList, columns=self.periodNames)
        if df.empty == False:
            df['zhang7'] = (df['today'] - df['7']) / df['7']
            df['zhang30'] = (df['today'] - df['30']) / df['30']
            df['zhang90'] = (df['today'] - df['90']) / df['90']
            df['zhang180'] = (df['today'] - df['180']) / df['180']
            df['zhang360'] = (df['today'] - df['360']) / df['360']
            df['zhang720'] = (df['today'] - df['720']) / df['720']
            df['zhang1080'] = (df['today'] - df['1080']) / df['1080']
            df['zhang1800'] = (df['today'] - df['1800']) / df['1800']
            df['tillNow'] = (df['today'] - df['startDate']) / df['startDate']
            df['W7'] = (df['N7'] - df['today']) / df['today']
            df['W14'] = (df['N14'] - df['today']) / df['today']
            df['W21'] = (df['N21'] - df['today']) / df['today']
            df['W30'] = (df['N30'] - df['today']) / df['today']
            df['W90'] = (df['N90'] - df['today']) / df['today']
            df['W180'] = (df['N180'] - df['today']) / df['today']
            df['W360'] = (df['N360'] - df['today']) / df['today']
        self.zhangfuDf = df.round(4) #保留4位小数

    def writeCsv(self):
        filename = self.No + '.csv'
        if os.path.exists(os.path.join(self.path, filename)):

            if self.zhangfuDf.empty:
                print('基金', self.No, '无需补充数据...')
                return
            else:
                print('基金', self.No, '补充部分数据...')
                self.zhangfuDf.to_csv(os.path.join(self.path, filename), sep=',', header=None, index=False, mode='a')
        else:
            print('基金',self.No,'补充全部数据...')
            self.zhangfuDf.to_csv(os.path.join(self.path, filename), sep=',', header=True, index=False, mode='w')

class zhangfuDf(object):
    def __init__(self,No,path='zhangfu'):
        self.path = path
        self.No = No
        self.df = self.getDf()
        self.yuchuli()
        self.feature_names = ['zhang7', 'zhang30', 'zhang90', 'zhang180', 'zhang360', 'zhang720', 'zhang1080',
                              'zhang1800', 'tillNow']
        self.x = self.df[self.feature_names]
        self.y = self.df.yuce

    def getDf(self):
        # 读取涨幅数据
        filename = self.No + '.csv'
        df = pd.DataFrame([])
        if os.path.exists(os.path.join(self.path, filename)):
            zhangfuFile = open(os.path.join(self.path, filename), 'r', encoding='utf-8')
            df = pd.read_csv(zhangfuFile, header=0)
        return df

    def yuchuli(self):
        df = self.df
        df['cha'] = df['tomorrow'] - df['days0000']
        df['N1cha'] = (df['N1week'] - df['days0000']) / df['days0000']
        df['N2cha'] = (df['N2week'] - df['N1week']) / df['N1week']
        df['yuce'] = df['tomorrow']
        # 将后期净值结果集二分成1或0，即上升或下降
        df['yuce'][(df['N1cha'] >= 0.01) & (df['N2cha'] >= 0.01)] = 1
        df['yuce'][(df['N1cha'] <= 0.01) | (df['N2cha'] < 0.01)] = 0
        # print(df)
        return df

class readjijinInfo():
    def __init__(self,path='base'):
        # 这里注意有header
        self.df = pd.read_csv(os.path.join(path, 'jijinListInfo.txt'), header=0)
        #self.df = pd.read_csv(os.path.join(path, 'tmp.txt'), header=0)
        self.rows = self.df.shape[0]
        self.NosList = list(self.df['No'].values)


def manyNoszhangfu(Nos,jijinPath='data',zhangfuPath='zhangfu',processName='noName'):
    lines = len(Nos)
    count = 0
    for i in Nos:
        starttime = datetime.now()
        count = count +1
        No = str(i).zfill(6)
        print('进程：', '%3s' % processName, ' 基金：', No, 'Starting ...',' 完成进度 = ', count, '/', lines)
        B = zhangfuCreate(No,zhangfuPath,jijinPath)
        B.writeCsv()
        endtime = datetime.now()
        print('进程：', '%3s' % processName, ' 基金：', No, '耗时', endtime - starttime)

def mutiProcess(processCount,basePath='base',jijinPath='data',zhangfuPath='zhangfu'):
    starttime = datetime.now()
    info = readjijinInfo(basePath)
    Nos = info.NosList

    lengthNos =len(Nos)
    shang = int(lengthNos / processCount)
    yushu = int(lengthNos % processCount)
    print('dateCount=', lengthNos , 'shang = ', shang, 'yushu = ', yushu)
    #print(Nos)
    #sys.exit(0)
    downloadProcesses = []

    # 开始创建进程
    for j in range(processCount):
        x = shang * j
        y = shang * j + shang
        #print('x,y,j',x,y,j)
        downloadProcess = Process(target=manyNoszhangfu, args=(Nos[x:y], jijinPath,zhangfuPath,str(j + 1),))
        downloadProcesses.append(downloadProcess)
        downloadProcess.start()

    if yushu != 0:
        lastdownloadProcess = Process(target=manyNoszhangfu,
                                      args=(Nos[processCount * shang:],jijinPath,zhangfuPath,str(processCount + 1),))
        downloadProcesses.append(lastdownloadProcess)
        lastdownloadProcess.start()
    # 等待所有进程结束
    for analyseProcess in downloadProcesses:
        analyseProcess.join()

    endtime = datetime.now()
    print(' 涨幅运行时间：', endtime - starttime, '\n')
    print('涨幅计算完毕！')



