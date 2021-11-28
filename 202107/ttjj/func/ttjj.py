import requests,datetime
import pandas as pd
class Ttjj(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Referer": "http://fund.eastmoney.com/"
        }
        # 显示所有列
        pd.set_option('display.max_columns', None)
        # 显示所有行
        pd.set_option('display.max_rows', None)
        # 设置value的显示长度为100，默认为50
        pd.set_option('display.max_columns', 500)
        pd.set_option('max_colwidth', 500)
        pd.set_option('display.width', 1500)
        #pd.set_option('display.line_width', None)

    def today(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def top(self,url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        htmltext = response.text
        s1 = htmltext.index('[')
        s2 = htmltext.index(']')
        data = htmltext[s1 + 2:s2 - 1].split('\",\"')
        return data

    def listtoframe(self,data,filter='all'):
        fieldName= ['编号','基金名称','jiancheng','date','单位净值', '累计净值', '今日', '本周', '月增幅', '近3月', '近6月', '近1年',
             '近2年', '近3年', '今年来', '成立来', '日期','f1','owndefine','fee1','fee2','f2','fee3','canbuy','f3']
        alljijins =[]
        for line in data:
            thisline = line.split(',')
            alljijins.append(thisline)
        df = pd.DataFrame(alljijins, columns=fieldName)
        #按日期过滤
        if filter!='all':
            date = filter
            df = df.loc[df["date"] == date]
        return df


