from sqlalchemy import create_engine
import tushare as ts



# 这里注意， tushare版本需大于1.2.10
# 设置token
ts.set_token('480ee193ae416ff6b096f533abfc982455e1fa5e7eb841d56b13a454')
# 初始化pro接口
pro = ts.pro_api()

#data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#print(data)

#df = pro.daily(ts_code='601919.SH', start_date='20220210', end_date='20220215')
#print(df)

df = ts.get_hist_data('601919',start='2019-08-01',end='2019-08-18',ktype='D')
#df.to_excel('601919.xlsx')

#df = ts.get_tick_data('601919')
print(df)
engine = create_engine('mysql://root:1234@192.168.0.62/jackytest?charset=utf8')
#存入数据库
df.to_sql('tick_data',engine,if_exists='append')