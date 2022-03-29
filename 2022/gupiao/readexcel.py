import pandas as pd
import numpy as np
import sys
from sklearn import preprocessing

import matplotlib.pyplot as plt
def Z_ScoreNormalization(x,mu,sigma):
    # 数据归一化
    x = (x - mu) / sigma;
    return x;

def np_do(df,field,line):

    # datanp = np.array(df.loc[:, field]) 取列名field的全部数据
    datanp = np.array(df.loc[:line, field].values)
    datanp = datanp[::-1]  # 倒序
    datanp = Z_ScoreNormalization(datanp, datanp.mean(), datanp.std())
    return  datanp

df=pd.read_excel("601919-2.xlsx")
print(df.loc[:4,'close'].values)
rows = 15
close = np_do(df,'close',rows)
#print(close)
#sys.exit(0)
turnover = np_do(df,'turnover',rows)
volume = np_do(df,'volume',rows)

#close = np.mat(close) 转为矩阵
#print(close.shape)
lines = df.shape[0]
lines = rows +1
x = np.linspace(1,lines,lines)
# 颜色代码{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
plt.plot(x,close,label='close',color='c')
plt.plot(x,turnover,label='turnover',color='y')
plt.plot(x,volume,label='volume',color='r')
plt.legend()
plt.savefig('1.jpg')
plt.show()
