# -*- coding: utf-8 -*-
# @File  : mysql_backup.py
# @Author: AaronJny
# @Date  : 2021/11/29
# @Desc  : 使用Python脚本，批量备份MySQL数据库结构和数据
from mylib.mysqlbackup import Backup
if __name__ == '__main__':
    mydb = Backup()
    mydb.backup()


