import os
from flask import g #(单个请求中的全局变量)
#https://www.cnblogs.com/-wenli/p/13949636.html
from sqlalchemy import create_engine
import sqlalchemy
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
print('environ',basedir,os.environ.get('DATABASE_URL'))
# 获取数据库名列表
insp = sqlalchemy.inspect(engine)
print(insp.get_schema_names())
# 获取表名列表
tables = engine.table_names()
print(tables)
# 获取表字段列表
md = sqlalchemy.MetaData()
print('md',md)
table  = sqlalchemy.Table('User', md, autoload=True, autoload_with=engine)
print(table.c)
for i in table.c:
    print(i,i.type)