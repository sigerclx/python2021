import os,datetime
import tools.stringfunc


# 按今天日期,和距今天数backup_days,返回日期列表
def __get_copy_dates(backup_days,today=1):
    if backup_days<1:
        backup_days=1  #至少保护当天的
    date_list = []
    for i in range(1-today, backup_days):
        curr_date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        date_list.append(curr_date)
    return date_list


#目录是否是日期方式：2002-10-31
def likedate(folder):
    # 分离目录名字，不带路径
    foldername = folder.split('\\')[-1]

    # 年月日 含-  2020-02-28 或 2021-1-1
    if tools.stringfunc.is_valid_date(foldername):
        return 1
    else:
        return 0

def protectdays(folder,backupinfo):
# 如果是保护目录，则返回
    protectdays = __get_copy_dates(backupinfo.protectDays)


    for protectday in protectdays:
        if protectday in folder:
            print('----- 目录保护：', folder, ' ------')
            return 1
    return 0


# 文件存在逻辑
def fileexist(file):
    if os.path.exists(file):
        return 1
    else:
        return 0