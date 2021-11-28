from func.ttjj import Ttjj
from func.topurl import Topurl
from func.tools import get_yesterday,is_week_lastday
import pandas as pd
import os,sys


#fieldName = ['no', 'name',  'date', '单位净值', '累计净值', '今日', '本周', '月增幅', '近3月', '近6月', '近1年',
#             '近2年', '近3年', '今年来', '成立来', '日期']
fieldName = ['编号','基金名称',  'date', '今日', '本周', '月增幅','近3月', '近6月', '近1年']
date = str(get_yesterday())
date = '2021-07-14'
# 周末不运行，退出
# if is_week_lastday():
#     sys.exit(0)

j = Ttjj()
toplist=[]
print(get_yesterday())


for i in Topurl:
    data = j.top(i.value)
    df = j.listtoframe(data,filter=date)
    csvfilename = date +str(i.name) + '.csv'
    df.to_csv(os.path.join('data',csvfilename))
    toplist.append(df[fieldName])


res = pd.DataFrame()

res = pd.merge(toplist[0],toplist[1],on=fieldName)
print('\n周月同榜：')
print(res)
res.to_csv(os.path.join('data',date+'-周月同榜.csv'))


res = pd.merge(res,toplist[2],on=fieldName)
print('\n周月季同榜')
print(res)
res.to_csv(os.path.join('data',date+'-周月季同榜.csv'))

res = pd.merge(res,toplist[3],on=fieldName)
print('\n周月季半年同榜')
print(res)
res.to_csv(os.path.join('data',date+'-周月季半年同榜.csv'))

res = pd.merge(res,toplist[4],on=fieldName)
print('\n周月季半年年同榜')
print(res)
res.to_csv(os.path.join('data',date+'-周月季半年年同榜.csv'))