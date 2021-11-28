import  pymysql,os
from func.tools import *

db = pymysql.connect(host="192.168.0.61", user="root", passwd="", db="haier_refrige_1_v2", charset='utf8',cursorclass =pymysql.cursors.DictCursor )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM zinfo_imgpath where date >='2021-03-10'"

sourch_path = r'G:\picturedata\2021'
dest_path = r'e:\zhongyi'
#dest_path = r'X:\work\z1\门齐照片2021(1-5月)'
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   # print(results)
   i =0
   for row in results:
      i += 1
      print(i)
      date = row["date"]
      y,m,d = date.split('-')
      model = row["model"]
      path  = row["path"]
      filename = row["filename"]
      currentsourcePath = os.path.join(sourch_path,m,d,path,filename)
      currentdestPath = os.path.join(dest_path,model)
      #print(currentsourcePath,currentdestPath)
      copy_file(currentsourcePath,currentdestPath,filename)

except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()
