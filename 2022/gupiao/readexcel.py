import pandas as pd
import numpy as np
import sys,os
from sklearn import preprocessing

# 折线图
import matplotlib.pyplot as plt

def Create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

def Z_ScoreNormalization(x,mu,sigma):
    # 数据归一化
    x = (x - mu) / sigma;
    return x;

def np_do(df,field,startnumber,endnumber):

    # datanp = np.array(df.loc[:, field]) 取列名field的全部数据
    datanp = np.array(df.loc[startnumber:endnumber, field].values)
    datanp = datanp[::-1]  # 倒序
    print(field,datanp)
    datanp = Z_ScoreNormalization(datanp, datanp.mean(), datanp.std())
    return  datanp

def qujian(p_change):
    if p_change > 7.5:
        return 'F75'
    if p_change > 5:
        return 'Z5'
    if p_change > 2.5:
        return 'Z25'
    if p_change > 0:
        return 'Z0'
    if p_change > -2.5:
        return 'F25'
    if p_change > -5:
        return 'F5'
    if p_change > -7.5:
        return 'F75'

    return 'F10'

def get_img(startnumber,guanzhu,rows):
    endnumber = rows + startnumber
    draw_x = [x for x in range(1,rows+2)]
    print(draw_x)
    for zhibiao in guanzhu:
        draw_y = np_do(df,zhibiao[0],startnumber,endnumber)
        plt.plot(draw_x,draw_y,color=zhibiao[1],linewidth=10)
        plt.legend()
    p_change = df.loc[startnumber-1, 'p_change']
    date = df.loc[startnumber - 1, 'date']
    print('p_change = ',p_change)
    path = qujian(p_change)
    filename = path +'_' +str(date) +'.jpg'
    Create_folder(os.path.join('601919', path))
    #plt.savefig(os.path.join('601919',path,filename),dpi=600)
    plt.savefig(os.path.join('601919', path, filename))
    plt.show()

def all_img(guanzhu,rows,records):
    pics =  records - rows
    for i in range(1,pics):
        print('No：',i)
        get_img(i,guanzhu, rows)

df=pd.read_excel("601919-2.xlsx")
guanzhu= [['open','b'],['close','g'],['high','r'],['low','c'],['turnover','m'],['volume','m']]
start = 0
records= df.shape[0]
records =50
# 绘图的区间天数
rows = 4
all_img(guanzhu,rows,records)
# print(df.loc[:4,'close'].values)
#print(close)
#sys.exit(0)

#close = np.mat(close) 转为矩阵
#print(close.shape)
#lines = df.shape[0]

# 颜色代码{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
