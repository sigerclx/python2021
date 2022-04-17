import pandas as pd
import numpy as np
import sys,os,gc
from sklearn import preprocessing

import matplotlib.pyplot as plt
# 直方图

def Create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

def Z_ScoreNormalization(x,mu,sigma):
    # 数据归一化
    x = (x - mu) / sigma;
    return x;

def np_do(field,startnumber,endnumber):
    global df
    # datanp = np.array(df.loc[:, field]) 取列名field的全部数据
    datanp = np.array(df.loc[startnumber:endnumber, field].values)
    datanp = datanp[::-1]  # 倒序
    #print(field,datanp)
    datanp = Z_ScoreNormalization(datanp, datanp.mean(), datanp.std())
    #print('datanp=',datanp)
    return  datanp

def np_oneday(df,guanzhu,startnumber):

    # datanp = np.array(df.loc[:, field]) 取列名field的全部数据
    one_day_values= []
    for field in guanzhu:
        one = df.loc[startnumber, field[0]]
        one_day_values.append(one)
    print(one_day_values)
    one_day_values = np.array(one_day_values)
    one_day_values = Z_ScoreNormalization(one_day_values, one_day_values.mean(), one_day_values.std())
    return  one_day_values

def qujian(p_change):
    if p_change > 7.5:
        return 'Z75'
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

def erfen_qujian(p_change):
    if p_change > 0:
        return 'Z'
    return 'F'

def get_img(startnumber,guanzhu,rows):
    endnumber = rows + startnumber
    draw_x = [x for x in range(1,rows+2)]
    print(draw_x)
    for zhibiao in guanzhu:
        draw_y = np_do(df,zhibiao[0],startnumber,endnumber)
        plt.plot(draw_x,draw_y,color=zhibiao[1],linewidth=10)
    p_change = df.loc[startnumber-1, 'p_change']
    date = df.loc[startnumber - 1, 'date']
    print('p_change = ',p_change)
    path = qujian(p_change)
    filename = path +'_' +str(date) +'.jpg'
    Create_folder(os.path.join('601919', path))
    #plt.savefig(os.path.join('601919',path,filename),dpi=600)
    plt.savefig(os.path.join('601919', path, filename))
    plt.show()
    plt.close()
    gc.collect()

def get_zhifang_img(startnumber,guanzhu,rows):
    #global df
    endnumber = rows + startnumber
    #print('startnumber,endnumber',startnumber,endnumber)
    draw_x = [x for x in range(0, rows + 1)]
    #print('draw_x=', draw_x)
    x = list(range(len(draw_x)))
    for zhibiao in guanzhu:
        draw_y = np_do(zhibiao[0], startnumber, endnumber)
        plt.bar(x, draw_y, width=0.15, tick_label=draw_x, fc=zhibiao[1])
        for i in range(len(x)):
           x[i] += 0.15
    # 关闭坐标轴
    plt.axis('off')
    # 获知明天的将要预测的数据
    p_change = df.loc[startnumber-1, 'p_change']
    date = df.loc[startnumber - 1, 'date']
    close = df.loc[startnumber - 1, 'close']
    print('p_change = ',p_change,date,close)
    path = qujian(p_change)
    path = erfen_qujian(p_change)
    # 生成文件名日期加分类的文件名
    filename = path +'_' +str(date) +'.jpg'
    Create_folder(os.path.join('601919', path))
    #plt.savefig(os.path.join('601919',path,filename),dpi=600)
    plt.savefig(os.path.join('601919', path, filename))
    plt.show()
    plt.close()
    gc.collect()

def all_img(guanzhu,rows,records):
    pics =  records - rows
    for i in range(1,pics):
        print('No：',i)
        get_img(i,guanzhu, rows)

def all_imgzhifang(guanzhu,rows,records):
    pics =  records - rows
    for i in range(1,pics):
        print('No：',i)
        get_zhifang_img(i,guanzhu, rows)

df=pd.read_excel("601919-2.xlsx")
guanzhu= [['open','b'],['close','g'],['high','r'],['low','c'],['volume','y']]
guanzhu= [['open','b'],['close','g'],['volume','y']]
#guanzhu= [['open','b'],['close','g'],['high','r'],['low','c'],['turnover','m']]

start = 0
records= df.shape[0]
print('records',records)
#records =23
# 绘图的区间天数
rows =5
#all_img(guanzhu,rows,records)
#get_zhifang_img(1,guanzhu,rows)
all_imgzhifang(guanzhu,rows,records)
# print(df.loc[:4,'close'].values)
#print(close)
#sys.exit(0)

#close = np.mat(close) 转为矩阵
#print(close.shape)
#lines = df.shape[0]

# 颜色代码{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
