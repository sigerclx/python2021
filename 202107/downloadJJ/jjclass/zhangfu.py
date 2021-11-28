import pandas as pd
import numpy as np

class zf(object):

    def __init__(self,df):
        self.df =df
        self.records =len(df)
        # datefields 比 datelist 多出一个字段id
        self.datefields = ['id','today','day5','day10','day15','day20','day25','day30','day45','day60',
                           'day90','day120','day150','day180','day360','day720','day1440',
                           'n1','n2','n3','n4','n5','n6','n7','n8','n9','n10','n15','n20','n30','n60','n90']
        self.datelist = [0,5,10,15,20,25,30,45,60,90,120,150,180,360,720,1440,
                         -1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-15,-20,-30,-60,-90]

    def getjingzhi(self,index,id):
        # 按df索引获得self.datelist天数的对应净值
        names = locals()
        line = []
        line.append(id)
        for i in self.datelist:
           indexno = index - i
           if indexno >= 0  and indexno <self.records:
               jingzhi =self.df[self.df.index == (index-i)].values
               line.append(jingzhi[0][2])
           else:
               line.append(None)
        return line

    def getzhangfu(self,jingzhidf):
        fields = ['id','today','day5','day10','day15','day20','day25','day30','day45','day60','day90','day120',
                   'day150','day180','day360','day720','day1440',
                  'z5','z10','z15','z20','z25','z30','z45','z60','z90','z120',
                   'z150','z180','z360','z720','z1440',
                  'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n15', 'n20', 'n30', 'n60', 'n90']

        df = pd.DataFrame(jingzhidf, columns=fields)
        if df.empty == False:
            df['z5'] = (df['today'] - df['day5']) / df['day5']
            df['z10'] = (df['today'] - df['day10']) / df['day10']
            df['z15'] = (df['today'] - df['day15']) / df['day15']
            df['z20'] = (df['today'] - df['day20']) / df['day20']
            df['z25'] = (df['today'] - df['day25']) / df['day25']
            df['z30'] = (df['today'] - df['day30']) / df['day30']
            df['z45'] = (df['today'] - df['day45']) / df['day45']
            df['z60'] = (df['today'] - df['day60']) / df['day60']
            df['z90'] = (df['today'] - df['day90']) / df['day90']
            df['z120'] = (df['today'] - df['day120']) / df['day120']
            df['z150'] = (df['today'] - df['day150']) / df['day150']
            df['z180'] = (df['today'] - df['day180']) / df['day180']
            df['z360'] = (df['today'] - df['day360']) / df['day360']
            df['z720'] = (df['today'] - df['day720']) / df['day720']
            df['z1440'] = (df['today'] - df['day1440']) / df['day1440']
            df['n1'] = ( df['n1']-df['today']) / df['today']
            df['n2'] = (df['n2']-df['today']) / df['today']
            df['n3'] = ( df['n3']-df['today']) / df['today']
            df['n4'] = (df['n4']-df['today']) / df['today']
            df['n5'] = ( df['n5']-df['today']) / df['today']
            df['n6'] = ( df['n6']-df['today']) / df['today']
            df['n7'] = ( df['n7']-df['today']) / df['today']
            df['n8'] = ( df['n8']-df['today']) / df['today']
            df['n9'] = ( df['n9']-df['today']) / df['today']
            df['n10'] = (df['n10']-df['today']) / df['today']
            df['n15'] = ( df['n15']-df['today']) / df['today']
            df['n20'] = (df['n20']-df['today']) / df['today']
            df['n30'] = ( df['n30']-df['today']) / df['today']
            df['n60'] = (df['n60']-df['today']) / df['today']
            df['n90'] = ( df['n90']-df['today']) / df['today']

        # inf 写入数据库时会报错
        df = df.replace(np.inf, -1)
        #print('------------------------------------')
        #print(df)
        #print('------------------------------------')
        return df.round(4)  # 保留4位小数



    def alljingzhi(self,currentdf):
        #计算某基金的所有净值
        lines = []
        for index, row in currentdf.iterrows():
            lines.append(self.getjingzhi(index,row['id']))

        jijinzhangfu = pd.DataFrame(lines, columns=self.datefields)
        return jijinzhangfu

    def filter(self):
        # 过滤day5没有值的行，相当于过滤没有计算涨幅的行
        df1 = self.df[self.df.day5.isna() ]
        print('过滤要更新的数据行数：',len(df1))
        return df1

