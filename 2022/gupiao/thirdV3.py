import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 类： 指标，天数，线型
class Basedata:
    pass

class Getdata:
    def __init__(self,basedata):
        self.basedata =  basedata
        self.__get_df_from_excel()

    def __get_df_from_excel(self):
        self._df = pd.read_excel(self.basedata.source)

    def __Z_ScoreNormalization(self,x, mu, sigma):
        # 数据归一化
        x = (x - mu) / sigma;
        return x;

    def to_rows_np(self,start,field):
        #在时间轴上纵向获取数据,比如取close收盘数据从某天取到某天
        #将某列从pandas的dataframe转换为numpy 的np list
        # datanp = np.array(df.loc[:, field]) 取列名field的全部数据
        datanp = np.array(self._df.loc[start:start+self.basedata.days-1, field].values)
        datanp = datanp[::-1]  # 倒序
        print(field, datanp)
        datanp = self.__Z_ScoreNormalization(datanp, datanp.mean(), datanp.std())
        return datanp

    def to_line_np(self,startline):
        # 在时间轴上横向获取数据（取某一天内的不同关键指标，例如某一天内的开盘、收盘价格）
        oneline =[]
        for key in self.basedata.key:
            datanp = np.array(self._df.loc[startline, key[0]])
            print(key[0],datanp)
            oneline.append(datanp)
        oneline =np.array(oneline)
        # 当oneline里少于3个关键指标的时候，不能正确归一化
        datanp = self.__Z_ScoreNormalization(oneline, oneline.mean(), oneline.std())
        return datanp

    def erfen_qujian(self,p_change):
        if p_change > 0:
            return 'Z'
        return 'F'

    def get_savename(self,start):
        # 获知明天的将要预测的数据
        p_change = self._df.loc[start - 1, 'p_change']
        date = self._df.loc[start - 1, 'date']
        path = self.erfen_qujian(p_change)
        filename = path + '_' + str(date) + '.jpg'
        # 生成文件名日期加分类的文件名
        path = os.path.join(self.basedata.path,path)
        return path,filename



    def get_one_piece(self):

        pass

    def get_more_data(self):
        pass

class Drawpic:
    def __init__(self,mybase):
        self.__mybase = mybase
        self.__getdata = Getdata(mybase)

    def create_folder(self,dest_path):
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

    def draw_volume(self,start):
        for key in self.__mybase.drawkey:
            onepiece = self.__getdata.to_rows_np(start,key[0])
            draw_x = [x for x in range(0, len(onepiece))]
            if key[1]=='plot':
                plt.plot(draw_x, onepiece, color=key[2], linewidth=4)
            else:
                plt.bar(draw_x, onepiece, width=0.4, tick_label=draw_x, fc=key[2])
            print(onepiece)
        plt.axis('off')
        path,filename = self.__getdata.get_savename(start)
        print(path)
        print(filename)
        self.create_folder(path)
        # plt.savefig(os.path.join('601919',path,filename),dpi=600)
        plt.savefig(os.path.join(path, filename),dpi=10)
        plt.show()
        plt.close()

    def draw_manypiece(self):
        for no in range(self.__mybase.start,self.__mybase.end):
            print('\nNo=',no)
            self.draw_volume(no)



mybase = Basedata()
mybase.key = [['open','b'],['close','g'],['high','r'],['low','c'],['volume','y']]
mybase.drawkey = [['close','plot','y'],['volume','bar','r']]
mybase.days = 5
mybase.start = 1
mybase.end = 3392
mybase.source = "601919-2.xlsx"
mybase.path = '601919'

mytarget = Basedata()
mytarget.forecastdays = 1
mytarget.forecastkey= 'close'


mydraw = Drawpic(mybase)
mydraw.draw_manypiece()



