import  MySQLdb,os
from func.tools import *
# 型号分类，根据型号，建立文件夹，把对应的NG图片拷贝进去

db = MySQLdb.connect("localhost", "root", "1234", "haier_ac_od_box_hf", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor( cursorclass = MySQLdb.cursors.DictCursor)
cursorModel = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)


def query_model(sn,sn1):
    # SQL 查询语句

    sql = "SELECT * FROM haier_ac_od_box_hf.acmodels where (serial= '%s' or serial= '%s')" %(sn,sn1)
    cursorModel.execute(sql)
    #print(sql)
    # 获取所有记录列表
    results = cursorModel.fetchone()

    if results:
        return results['name']
    else:
        return None

# SQL 查询语句
sql = "SELECT  * FROM inspections WHERE result <>0"
dest_path = r'd:\ng\ng'

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   # print(results)
   for row in results:
      pic_name = row["name"]

      ngfile = os.path.join(dest_path,pic_name)
      if not os.path.exists(ngfile):
          continue
      print(pic_name)
      serial_number = row["serial_number"].split(",")
      if len(serial_number)==2:
          #print(pic_name,serial_number)
          if len(serial_number[0])> len(serial_number[1]):
              curr_sn9 = serial_number[0][:9]
              curr_sn11 = serial_number[0][:11]
          else:
              curr_sn9 = serial_number[1][:9]
              curr_sn11 = serial_number[1][:11]

      else:
          # 不含两个码的数据忽略

          curr_sn9 = serial_number[0][:9]
          curr_sn11 = serial_number[0][:11]

      model = query_model(curr_sn9, curr_sn11)
      print('model:', model)
      if model:
          # 找到对应型号
          dest = os.path.join(dest_path, model)
          create_folder(dest)
          move_file(ngfile, dest)
      else:
          print(ngfile, curr_sn9, curr_sn11)


except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()
