import  MySQLdb,os
from func.tools import *



db = MySQLdb.connect("localhost", "root", "1234", "haier_ac_od_box_hf", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor( cursorclass = MySQLdb.cursors.DictCursor)
# SQL 查询语句
sql = "SELECT * FROM inspections WHERE result <>0"

sourch_path = r'd:\work\imagelogo'
dest_path = r'd:\ng'
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   # print(results)
   for row in results:
      pic_name = row["name"]
      curr_pic=pic_name.split("-")
      date_str  = curr_pic[1]+"-"+curr_pic[2]+"-"+curr_pic[3]
      curr_file = os.path.join(sourch_path,date_str,pic_name)
      print(curr_file)
      copy_file(curr_file,dest_path)

except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()
