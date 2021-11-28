from sql.mssql import MSSQL

mssql = MSSQL(host="192.168.0.51",user="sa",pwd="a1b2/a",db="Jijin")
reslist = mssql.ExecQuery("select * from getmaxmindate")
for i in reslist:
   print (i)