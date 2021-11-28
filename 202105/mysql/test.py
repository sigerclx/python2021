import  MySQLdb,os
from func.tools import *

db = MySQLdb.connect("localhost", "root", "1234", "haier_ac_od_box_hf", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor( cursorclass = MySQLdb.cursors.DictCursor)
cursorModel = db.cursor( cursorclass = MySQLdb.cursors.DictCursor)







# SQL 查询语句
sql ="SELECT * FROM haier_ac_od_box_hf.acmodels where  serial='AA3Q2901P';"

sourch_path = r'd:\work\imagelogo'
dest_path = r'd:\ng'
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchone()
   # print(results)
   if results:
        print(results)




except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()
