import os
from sqlalchemy import create_engine
from config import  basedir
import sqlalchemy
# flaskOne的根目录下的app目录里的__init__ 只执行一次，所以把全局变量全部放入其中
# share类就是获取全局的基础变量，可以在不同用户请求之间共享
class BaseValue(object):
    def __init__(self):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                  'sqlite:///' + os.path.join(basedir, 'app.db')
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)

        # 获取数据库名列表
        insp = sqlalchemy.inspect(self.engine)
        self.dbs = insp.get_schema_names()
        #print(insp.get_schema_names())
        # 获取表名列表
        self.tables = self.engine.table_names()
        self.reimbursement = self.getTablefields('reimbursement')
        #print(tables)
    def getTablefields(self,tablename):
        # 获取表字段列表
        md = sqlalchemy.MetaData()
        #print('md',md)
        table  = sqlalchemy.Table(tablename, md, autoload=True, autoload_with=self.engine)
        fields = table.c
        return fields
        #print(table.c)
        #for i in table.c:
        #    print(i,i.type)