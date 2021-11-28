# coding:UTF-8
import os, sys
sys.path.append(r'/Volumes/Macintosh HD/Python/Source/2019/201912/Mforcast/lib')
import jackylib
from datetime import datetime
import numpy as np
import pandas as pd
from multiprocessing import Process, Manager
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import warnings

# 忽略警告
warnings.filterwarnings("ignore")


class jinzhi(object):
    def __init__(self, No, path='data'):
        self.No = str(No).zfill(6)
        self.period = [0, 1, 2, 3, 4, 5, -1, -7, -14]
        # self.period = [0, 5, 10, 20, 30, 50, -1]
        self.periodName = ['No', 'date', 'days0000', 'days0030', 'days0090', 'days0180', 'days0360', 'days0720',
                           'tomorrow', 'N1week', 'N2week']
        self.periodLength = len(self.period)
        self.pointDateList = []
        self.path = path
        self.historyDays = 365
        self.flag = True
        self.readJijinDF()

    def readJijinDF(self):
        # 按日期data获取基金no的对应的那一行
        filename = os.path.join(self.path, self.No + '.txt')
        # 这里注意没有表头header
        self.jijinDF = pd.read_csv(filename, header=None)
        self.jijinDF.columns = list('ABCDEFG')
        # 获取基金的起始日期

        self.startDate = self.jijinDF.head(1).iloc[0, 0]
        self.endDate = self.jijinDF.tail(1).iloc[0, 0]
        self.pointDate = jackylib.he(self.startDate, self.historyDays + 10)

        #print(self.startDate,self.endDate,self.pointDate)
        if jackylib.diffdate(self.pointDate, self.endDate):
            # 如果取样点大于基金的最晚日期，则返回失败
            self.flag = False

    def getDate(self, date):
        dateWhat = self.jijinDF.loc[self.jijinDF['A'] == date]
        return dateWhat

    def jingZhi(self, date):
        dateValue = pd.DataFrame([], index=None)
        count = 0
        # 去对应日期的基金净值，如果日期找不到，则日期减1，继续找，直到找到为止。但日期出范围则返回0
        while dateValue.empty:
            if jackylib.diffdate(self.startDate, date):
                return 0
            date = jackylib.cha(date, count)
            dateValue = self.getDate(date)
            if dateValue.empty == False:
                if dateValue['B'].empty:
                    dateValue = pd.DataFrame([], index=None)
                else:
                    jingZHI = dateValue['B'].values[0]
                    break
            count += 1  # 取不到数据，就向前顺延一天
        return jingZHI

    def periodJingzhi(self, date):
        '''
        根据pointDate构建按周期计算出的净值list
        # 不一定出具日期就一定有基金数据，没有数据的时候lines=''，所以要往前减一天顺延，直至有数据为止
        :return:净值list
        '''

        NoValues = []
        # print('%10s' % periodName, 'period = ', period, 'start ......')

        pDate = []
        # 根据周期长度，计算实际周期的具体日期
        for i in self.period:
            pDate.append(str(jackylib.cha(date, int(i))))
        # print(pDate)
        NoValues.append(self.No)
        NoValues.append(pDate[0])
        # 这求得的列都为空就继续往前顺延一天，求净值数据，直到不为空
        for i in pDate:
            # 取得对应日期的基金净值数据行DF格式(如果对应日期找不到，则减一天继续，直到找到对应基金净值，最后都没找到则返回0)
            a1 = self.jingZhi(i)
            NoValues.append(a1)

        return NoValues

    def createDatelist(self, step=7):
        pointDateList = []
        # 构建目标日期序列，每周一算
        count = 0
        currentDate = self.pointDate
        while jackylib.diffdate(self.endDate, currentDate):
            count = count + 1
            currentDate = jackylib.he(self.pointDate, step * count)
            pointDateList.append(currentDate)
        return pointDateList

    def resultDF(self, pointDatelist, return_dict, processName='noName'):
        '''
        获取单基金编号的多个日期的多周期基金净值数据
        '''

        starttime = datetime.now()
        lines = []
        for i in pointDatelist:
            line = self.periodJingzhi(i)
            lines.append(line)
        df = pd.DataFrame(lines, columns=self.periodName)
        # print(df)
        try:
            return_dict[pointDatelist[0]] = df
        except Exception as err:
            print('return_dict DF出错')
            print(err)
            print(df)
            sys.exit(0)

        endtime = datetime.now()
        print('进程:', processName, ' 数据预处理时间：', endtime - starttime, '\n')
        # return df

    def getManyNoPeriodJingzhi(self, Nolist):
        # 获取多个基金编号的周期（多个）的净值数据
        lines = []
        for i in Nolist:
            line = self.periodJingzhi()
            lines.append(line)
        return lines


def MutiProcess(No, step, processCount=1):
    '''
    :param No: 单个基金编号
    :param step:  每个日期数据的间隔天数
    :param processCount 进程数
    :return:
    '''
    starttime = datetime.now()
    manager = Manager()
    return_dict = manager.dict()
    myjingzhi = jinzhi(No)
    #print('jjclass init.' , 'step=',step)
    #print('myjingzhi.flag',myjingzhi.flag)
    if myjingzhi.flag == False:
        return pd.DataFrame([])
    pointDatelist = myjingzhi.createDatelist(step)
    #print('pointDatelist',pointDatelist)
    #sys.exit(0)
    dateCount = len(pointDatelist)

    shang = int(dateCount / processCount)
    yushu = int(dateCount % processCount)
    print('dateCount=', dateCount, 'shang = ', shang, 'yushu = ', yushu)

    downloadProcesses = []

    # 开始创建进程
    for j in range(processCount):
        x = shang * j
        y = shang * j + shang

        downloadProcess = Process(target=myjingzhi.resultDF, args=(pointDatelist[x:y], return_dict, str(j + 1),))
        downloadProcesses.append(downloadProcess)
        downloadProcess.start()

    if yushu != 0:
        lastdownloadProcess = Process(target=myjingzhi.resultDF,
                                      args=(pointDatelist[processCount * shang:], return_dict, str(processCount + 1),))
        downloadProcesses.append(lastdownloadProcess)
        lastdownloadProcess.start()
    # 等待所有进程结束
    for analyseProcess in downloadProcesses:
        analyseProcess.join()

    # 取出多进程返回值的第一个
    result = list(return_dict.values())[0]
    # 拼合返回值结果集
    for i in return_dict.values()[1:]:
        result = pd.concat([result, i], axis=0)
    df = result.sort_values(by='date', ascending=True)  # 按date列排序
    df = df.reset_index(drop=True)  # 重新索引

    endtime = datetime.now()
    print('多线程数据预处理总运行时间：', endtime - starttime, '\n')
    return df


class yuce(object):
    def __init__(self, df):
        self.df = df
        self.feature_names = ['days0000', 'days0030', 'days0090', 'days0180', 'days0360']
        self.yuchuli()
        self.x = df[self.feature_names]
        self.y = df.yuce
        self.knn_range = 25

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

    def huigui_yuce(self):
        # 数据分离
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y,
                                                                                train_size=0.4)  # random_state=0,

        # print(self.x_train.shape,self.y_train.shape)

        # 模型训练,机器学习
        self.logreg = LogisticRegression()

        if self.y_train[self.y_train > 0].empty or self.y_test[self.y_test > 0].empty:
            print('结果集全为0，无法学习！')
            return None

        try:
            self.logreg.fit(self.x_train, self.y_train)
        except Exception as err:
            # 目前的唯一错误就是训练和结果数据全部为0，所以无法训练
            print('机器学习错误：')
            print(err)
            print('self.x_train,  self.y_train', self.x_train, self.y_train)
            print('self.x_train,  self.y_train', self.x_train.shape, self.y_train.shape)
            print('self.x_test, self.y_test', self.x_test.shape, self.y_test.shape)
            sys.exit(0)

        # 测试数据 结果预测
        y_pred = self.logreg.predict(self.x_test)
        meanZhi = round(self.y_test.mean(), 3)

        # 计算并展示混淆矩阵
        try:
            confusion = metrics.confusion_matrix(self.y_test, y_pred)
            # print(confusion)
            TN = confusion[0, 0]  # 预测为0，实际为0
            FP = confusion[0, 1]  # 预测为1，实际为0
            FN = confusion[1, 0]  # 预测为0，实际为1
            TP = confusion[1, 1]  # 预测为1，实际为1
        except Exception as err:
            print('机器学习错误,confusion混淆矩阵出错：')
            print(err)
            print(confusion)
            print('self.x_train,  self.y_train', self.x_train, self.y_train)
            print('self.x_train,  self.y_train', self.x_train.shape, self.y_train.shape)
            print('self.x_test, self.y_test', self.x_test, self.y_test)
            print('self.x_test, self.y_test', self.x_test.shape, self.y_test.shape)
            sys.exit(0)

        # print(TN, FP, FN, TP)
        accuracy = round((TP + TN) / (TP + TN + FN + TP), 3)  # 准确率
        # print('准确率', accuracy)
        recall = round(TP / (TP + FN), 3)  # 正样本中预测正确率
        # print('回收率(正样本的预测正确率 预测上升 TP / (TP + FN))', recall)
        specificity = round(TN / (TN + FP), 3)  # 正样本中预测正确率
        # print('特异度(负样本的预测正确率 预测下降 TN / (TN + FP) )', specificity)
        precision = round(TP / (TP + FP), 3)
        # print('精确率(预测为1的正确率 TP / (TP + FP))', precision)

        result = {}
        result['No'] = self.df['No'].head(1)[0]

        result['准确率'] = accuracy
        result['混淆矩阵'] = confusion
        result['回收率'] = recall
        result['特异度'] = specificity
        result['精确率'] = precision
        result['测试数据平均值'] = meanZhi

        # print(result)
        return result

    def huigui_Save(self, step, times=10):
        # 把基金编号，日期取样数量，日期步长
        starttime = datetime.now()
        lines = []
        for i in range(times):
            tmpDict = self.huigui_yuce()
            if tmpDict == None:
                return
            #tmpDict['dayscount'] = daysCount
            tmpDict['step'] = step
            lines.append(tmpDict)

        df = pd.DataFrame(lines)
        df.to_csv(os.path.join('log', 'analysis.csv'), header=None, encoding='gb2312', mode='a')
        endtime = datetime.now()
        print(' 预测数据运行时间：', endtime - starttime, '\n')
        return df

    def knn_yuce(self):

        # knn = KNeighborsClassifier(n_neighbors=1)
        # 数据分离，找出训练集和测试集
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y,
                                                                                train_size=0.4)  # random_state=0,
        if self.y_train[self.y_train > 0].empty or self.y_test[self.y_test > 0].empty:
            print('结果集全为0，无法学习！')
            return None

        # 模型训练
        k_range = list(range(1, self.knn_range))
        # knn.fit(self.x_train,  self.y_train)
        score_train = []
        score_test = []
        meanZhi = round(self.y_test.mean(), 3)
        lines = []
        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(self.x_train, self.y_train)
            try:
                y_train_pred = knn.predict(self.x_train)
                y_test_pred = knn.predict(self.x_test)
            except Exception as err:
                print('KNN超出范围')
                print(err)
                break

            score_train.append(accuracy_score(self.y_train, y_train_pred))
            score_test.append(accuracy_score(self.y_test, y_test_pred))
            # 计算并展示混淆矩阵
            try:
                confusion = metrics.confusion_matrix(self.y_test, y_test_pred)
                print('k=', k, '混淆矩阵=', confusion)
                print('准确率=', accuracy_score(self.y_test, y_test_pred))
                # print(confusion)
                TN = confusion[0, 0]  # 预测为0，实际为0
                FP = confusion[0, 1]  # 预测为1，实际为0
                FN = confusion[1, 0]  # 预测为0，实际为1
                TP = confusion[1, 1]  # 预测为1，实际为1
            except Exception as err:
                print('机器学习错误,confusion混淆矩阵出错：')
                print(err)
                print(confusion)
                print('self.x_train,  self.y_train', self.x_train, self.y_train)
                print('self.x_train,  self.y_train', self.x_train.shape, self.y_train.shape)
                print('self.x_test, self.y_test', self.x_test, self.y_test)
                print('self.x_test, self.y_test', self.x_test.shape, self.y_test.shape)
                sys.exit(0)

            # print(TN, FP, FN, TP)
            accuracy = round((TP + TN) / (TP + TN + FN + TP), 3)  # 准确率
            # print('准确率', accuracy)
            recall = round(TP / (TP + FN), 3)  # 正样本中预测正确率
            # print('回收率(正样本的预测正确率 预测上升 TP / (TP + FN))', recall)
            specificity = round(TN / (TN + FP), 3)  # 正样本中预测正确率
            # print('特异度(负样本的预测正确率 预测下降 TN / (TN + FP) )', specificity)
            precision = round(TP / (TP + FP), 3)
            # print('精确率(预测为1的正确率 TP / (TP + FP))', precision)

            result = {}
            result['No'] = self.df['No'].head(1)[0]
            result['n_neighbors'] = k
            result['准确率'] = accuracy
            result['混淆矩阵'] = confusion
            result['回收率'] = recall
            result['特异度'] = specificity
            result['精确率'] = precision
            result['测试数据平均值'] = meanZhi
            lines.append(result)
        return lines
        # print(score_test)
        # print(score_train)

    def knn_Save(self, step, times=1):
        # 把基金编号，日期取样数量，日期步长
        starttime = datetime.now()
        lines = []

        tmpList = self.knn_yuce()
        if tmpList == None:
            return
        for i in tmpList:
            if i == None:
                return
            i['step'] = step
            lines.append(i)

        df = pd.DataFrame(lines)
        df.to_csv(os.path.join('log', 'analysis.csv'), header=None, encoding='gb2312', mode='a')
        endtime = datetime.now()
        print(' 预测数据运行时间：', endtime - starttime, '\n')
        return df


def do_huigui(times):
    jjfile = open(os.path.join('base', 'jijinListInfo.txt'), 'r', encoding='utf-8')
    DF = pd.read_csv(jjfile, header=0)
    jijinNos = DF['No'][DF['startDate'] < '2014-01-01']


    for k in jijinNos[:4]:
        for i in range(3):
            print('基金', '%6s' % k, '第', i + 1, '次 ', end='')
            # 数据预处理，多进程。第一个参数是基金编号，第二个是起始日期，第三个是取样日期数量，第四个是取样日期间隔，最后一个参数是进程数
            step = (i+1) * 20
            print('MutiStart:',k,step)
            df = MutiProcess(k, step, 10)
            # 去除数据NaN,全部置0
            df.fillna(0, inplace=True)
            myce = yuce(df)
            yc = myce.huigui_Save(step, times)


def do_knn(step):
    jjfile = open(os.path.join('base', 'mylist.txt'), 'r', encoding='utf-8')
    DF = pd.read_csv(jjfile, header=0)
    jijinNos = DF['No']  # [DF['startDate'] < '2014-01-01']

    for k in jijinNos:
        print('基金', '%6s' % k, end='')
        # 数据预处理，多进程。第一个参数是基金编号，第二个是起始日期，第三个是取样日期数量，第四个是取样日期间隔，最后一个参数是进程数

        df = MutiProcess(k, step, 10)
        # print('df',type(df),df)
        if df.empty:
            print('该基金数据太少，无法分析')
            continue
        # sys.exit(0)
        # 去除数据NaN,全部置0
        df.fillna(0, inplace=True)
        myce = yuce(df)
        yc = myce.knn_Save(step, 1)  # k, daysCount, step, 5


def main():
    starttime = datetime.now()
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # do_huigui()  # 线性回归运算

    #do_knn(1)
    do_huigui(2)
    endtime = datetime.now()
    print(' 程序运行时间：', endtime - starttime, '\n')
    print('分析完毕！')


if __name__ == '__main__':
    main()
