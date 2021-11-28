# 按今天日期,和距今天数backup_days,返回日期列表
import datetime
def Get_copy_dates(backup_days,today=1):
    date_list = []
    for i in range(1-today, backup_days):
        curr_date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y%m%d")
        date_list.append(curr_date)
    return date_list

import time
s = Get_copy_dates(20)
print(s)

