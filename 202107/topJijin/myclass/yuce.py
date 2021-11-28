import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime
import sys, os
import warnings

# 忽略警告
warnings.filterwarnings("ignore")


class yuce(object):
    def __init__(self, df, knn_range=10):
        self.df = df.fillna(0)  # 把NaN全部填0
        self.feature_names = ['zhang7', 'zhang30', 'zhang90', 'zhang180', 'Date', 'today', 'W7', 'W14', 'W21', 'N7',
                              'N14', 'N21']
        # self.feature_names = [ 'zhang180', 'zhang90', 'zhang30','zhang7']\
        self.empty = False
        # 把无法计算360天的数据过滤掉
        self.df = self.df[(self.df['zhang360'] != 0)]
        if self.df.empty:
            self.empty =True
            return
        self.x = self.df[self.feature_names]
        self.y = self.df.yuce.astype('int')
        # self.date = self.df.Date
        self.knn = knn_range
        self.No = str(self.df.No.head(1).iloc[0]).zfill(6)
        # print(self.No)
        # print(self.knn)
        # sys.exit(0)

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
            # tmpDict['dayscount'] = daysCount
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

        score_train = []
        score_test = []
        meanZhi = round(self.y_test.mean(), 3)
        lines = []
        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            print('KNeighbors=', k)

            self.x_train.icol(0)
            self.x_train.icol(1)
            self.x_train.icol(2)
            self.x_train.icol(4)

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
            result['总样本'] = self.x.shape[0]
            result['练习样本'] = self.x_train.shape[0]
            result['预测样本'] = self.y_test.shape[0]
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

    def knn_yuce_five(self):

        # knn = KNeighborsClassifier(n_neighbors=1)
        # 数据分离，找出训练集和测试集
        self.x_trainDate, self.x_testDate, self.y_train, self.y_test = train_test_split(self.x, self.y,
                                                                                        train_size=0.4)  # random_state=0,

        # n=1900 自己的按日期排序后的数据分离
        # self.x_trainDate = self.x[:n]
        # self.y_train = self.y[:n]
        # self.x_testDate = self.x[n:]
        # self.y_test = self.y[n:]
        # print(self.x_trainDate.shape[0])
        # sys.exit(0)
        # 取前4列
        self.x_train = self.x_trainDate.iloc[:, [0, 1, 2, 3]].copy(deep=True)

        self.x_test = self.x_testDate.iloc[:, [0, 1, 2, 3]].copy(deep=True)
        self.date = self.x_testDate.iloc[:, [4, 5, 6, 7, 8, 9, 10, 11]].copy(deep=True)
        # print(self.date.shape[0])

        # self.x_train_tmp = self.x_train.copy(deep=True)
        # print(self.x_train,self.x_trainDate)
        # sys.exit(0)
        if self.y_train[self.y_train > 0].empty or self.y_test[self.y_test > 0].empty:
            print('结果集全为0，无法学习！')
            return None

        # 模型训练

        score_train = []
        score_test = []
        meanZhi = round(self.y_test.mean(), 3)
        lines = []
        for k in range(2, self.knn + 1):
            # k = 3
            print('KNeighbors=', k)
            knn = KNeighborsClassifier(n_neighbors=k)

            # self.x_train.iloc[:, [0]] = self.x_trainDate.iloc[:, [1]] * j
            # self.x_train.iloc[:, [1]] = self.x_trainDate.iloc[:, [2]] * m
            # self.x_train.iloc[:, [2]] = self.x_trainDate.iloc[:, [3]] * n

            try:
                knn.fit(self.x_train, self.y_train)
                y_train_pred = knn.predict(self.x_train)
                y_test_pred = knn.predict(self.x_test)
            except Exception as err:
                print(self.x_train)
                print(self.y_train)
                print('KNN超出范围 or NaN')
                print(err)
                sys.exit(0)

            self.x_test = self.x_test.reset_index(drop=True)
            # print('x_test=', self.x_test)

            self.y_test = self.y_test.reset_index(drop=True)
            self.y_test.columns = ['test']
            y = pd.DataFrame(y_test_pred, columns=['pred'])
            # print('y_test_pred=')
            # print(y)

            # print(self.y_test)
            # print(y)
            # print(self.date)
            self.date = self.date.reset_index(drop=True)
            # print(self.date)
            # sys.exit(0)
            score_train.append(accuracy_score(self.y_train, y_train_pred))
            score_test.append(accuracy_score(self.y_test, y_test_pred))
            self.testDF = pd.merge(self.y_test, y, left_index=True, right_index=True, how='outer')
            self.testDF = pd.merge(self.testDF, self.date, left_index=True, right_index=True, how='outer')
            self.testDF = pd.merge(self.testDF, self.x_test, left_index=True, right_index=True, how='outer')
            # 预测明细数据
            self.testDF.to_csv(os.path.join('log', self.No + 'analysis_testDf.csv'), header=True, encoding='gb2312',
                               mode='w')
            # print(self.testDF)
            # 计算并展示混淆矩阵
            try:
                confusion = metrics.confusion_matrix(self.y_test, y_test_pred)
                # print('k=', k, '混淆矩阵=', confusion)
                print('训练样本准确率=', accuracy_score(self.y_train, y_train_pred))
                print('预测样本准确率=', accuracy_score(self.y_test, y_test_pred))

                # print(confusion)
                TN = confusion[0, 0]  # 预测为0，实际为0
                FP = confusion[0, 1]  # 预测为1，实际为0
                FN = confusion[1, 0]  # 预测为0，实际为1
                TP = confusion[1, 1]  # 预测为1，实际为1
            except Exception as err:
                print('机器学习错误,confusion混淆矩阵出错：')
                print(err)
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

            try:
                result['No'] = self.df['No'].head(1).iloc[0]
            except Exception as err:
                print('err11=', err)
            # sys.exit(0)
            result['总样本'] = self.x.shape[0]
            result['练习样本'] = self.x_train.shape[0]
            result['预测样本'] = self.y_test.shape[0]
            result['所有平均'] = self.testDF['today'].mean()
            result['0平均'] = self.testDF['today'][(self.testDF['pred'] == 0)].mean()
            result['1平均'] = self.testDF['today'][(self.testDF['pred'] == 1)].mean()
            result['2平均'] = self.testDF['today'][(self.testDF['pred'] == 2)].mean()
            result['1-2平均'] = self.testDF['today'][(self.testDF['pred'] == 2) | (self.testDF['pred'] == 1)].mean()

            # result['参数'] = str(j) + '--' + str(m) + '--' + str(n)
            result['n_neighbors'] = k
            result['准确率'] = accuracy_score(self.y_test, y_test_pred)
            result['混淆矩阵'] = confusion
            result['回收率'] = recall
            result['特异度'] = specificity
            result['精确率'] = precision
            result['测试数据平均值'] = meanZhi
            lines.append(result)
        return lines
        # print(score_test)
        # print(score_train)

    def knn_Save(self):

        # 把基金编号，日期取样数量，日期步长
        starttime = datetime.now()
        lines = []

        tmpList = self.knn_yuce_five()
        # print('--------------')
        # sys.exit(0)
        if tmpList == None:
            return
        for i in tmpList:
            if i == None:
                return
            # i['step'] = step
            lines.append(i)

        df = pd.DataFrame(lines)
        # 预测结果集存盘

        df.to_csv(os.path.join('log', 'analysis.csv'), header=True, encoding='gb2312', mode='a')
        # 样本数据存盘
        self.df.to_csv(os.path.join('log', self.No + 'analysisDf.csv'), header=True, encoding='gb2312', mode='a')
        # 预测明细数据
        # self.testDF.to_csv(os.path.join('log', 'analysis_testDf.csv'), header=True, encoding='gb2312', mode='w')
        endtime = datetime.now()
        print(' 预测数据运行时间：', endtime - starttime, '\n')
        return df
