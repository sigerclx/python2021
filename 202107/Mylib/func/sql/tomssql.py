import pandas as pd
import sqlalchemy,sys
from sqlalchemy import create_engine
from pandas.core.frame import DataFrame

class Write_df(object):
    def __init__(self):
        self.engine = create_engine('mssql+pymssql://sa:a1b2/a@192.168.0.51/Jijin')

    def write_jjinfo(self,jijinNO,jijinDF):
        '''
        根据文件路径，取得该文件名称，基金数据起始日期，结束日期
        :param filename:
        :return:
        '''
        record = len(jijinDF)
        print(jijinNO,record)
        #sys.exit(0)
        # 设定基金列名，对应数据表的字段名
        jijinDF.columns=['date', 'jingzhi', 'leijijingzhi', 'zhangfu', 'statusBuy','statusSell','remark']

        col_name = jijinDF.columns.tolist()  # 将jijinDF的列名全部提取出来存放在列表里
        col_name.insert(0, 'no')  # 在列索引为0的位置插入一列,列名为:no，刚插入时不会有值，整列都是NaN
        jijinDF = jijinDF.reindex(columns=col_name)  # DataFrame.reindex() 对原行/列索引重新构建索引值
        jijinDF['no'] = jijinNO  #整列都等于基金编号
        jijinDF['zhangfu'] =jijinDF['zhangfu'].str.replace('%','')
        # 在此处可以将处理好的数据一次写入数据库
        jijinDF.to_sql('dayinfo' ,self.engine, index=False,if_exists='append',dtype={'no':sqlalchemy.types.NVARCHAR(),'date': sqlalchemy.types.NVARCHAR(),'jingzhi':sqlalchemy.types.FLOAT(),'leijijingzhi':sqlalchemy.types.FLOAT(),'zhangfu':sqlalchemy.types.FLOAT() ,'statusBuy':sqlalchemy.types.NVARCHAR(), 'statusSell':sqlalchemy.types.NVARCHAR(), 'remark':sqlalchemy.types.NVARCHAR() })

    def write_jjlist(self,jijinNOlist):
        '''
        根据文件路径，取得该文件名称，基金数据起始日期，结束日期
        :param filename:
        :return:
        '''
        df = DataFrame(jijinNOlist)
        record = len(df)
        print('基金总数：',record)
        #print(df)

        #sys.exit(0)
        # 设定基金列名，对应数据表的字段名
        df.columns=['no', 'pinyin', 'name', 'type', 'quanpin']
        # 在此处可以将处理好的数据一次写入数据库
        df.to_sql('nolist' ,self.engine, index=False,if_exists='replace',dtype={'no':sqlalchemy.types.NVARCHAR(),'pinyin': sqlalchemy.types.NVARCHAR(),'name':sqlalchemy.types.NVARCHAR(),'type':sqlalchemy.types.NVARCHAR(),'quanpin':sqlalchemy.types.NVARCHAR() })

    def write_jjzf(self,jijinzf):
        '''
        根据文件路径，取得该文件名称，基金数据起始日期，结束日期
        :param filename:
        :return:
        '''
        df = DataFrame(jijinzf)
        record = len(df)
        print('更新基金涨幅日期行数：',record)

        # 设定基金列名，对应数据表的字段名
        df.columns = ['id', 'today','day5','day10','day15','day20','day25','day30','day45','day60','day90','day120','day150','day180','day360','day720','day1440',
                      'z5','z10', 'z15', 'z20', 'z25', 'z30', 'z45', 'z60', 'z90', 'z120',
                      'z150', 'z180', 'z360', 'z720', 'z1440',
                      'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n15', 'n20', 'n30', 'n60', 'n90']

        # 在此处可以将处理好的数据一次写入数据库
        df.to_sql('jjzf' ,self.engine, index=False,if_exists='replace',dtype={'id':sqlalchemy.types.BIGINT(),
                                                                              'today': sqlalchemy.types.FLOAT(),
                                                                              'day5': sqlalchemy.types.FLOAT(),
                                                                              'day10': sqlalchemy.types.FLOAT(),
                                                                              'day15': sqlalchemy.types.FLOAT(),
                                                                              'day20': sqlalchemy.types.FLOAT(),
                                                                              'day25': sqlalchemy.types.FLOAT(),
                                                                              'day30': sqlalchemy.types.FLOAT(),
                                                                              'day45': sqlalchemy.types.FLOAT(),
                                                                              'day60': sqlalchemy.types.FLOAT(),
                                                                              'day90': sqlalchemy.types.FLOAT(),
                                                                              'day120': sqlalchemy.types.FLOAT(),
                                                                              'day150': sqlalchemy.types.FLOAT(),
                                                                              'day180': sqlalchemy.types.FLOAT(),
                                                                              'day360': sqlalchemy.types.FLOAT(),
                                                                              'day720': sqlalchemy.types.FLOAT(),
                                                                              'day1440': sqlalchemy.types.FLOAT(),
                                                                              'z5': sqlalchemy.types.FLOAT(),
                                                                              'z10': sqlalchemy.types.FLOAT(),
                                                                              'z15': sqlalchemy.types.FLOAT(),
                                                                              'z20': sqlalchemy.types.FLOAT(),
                                                                              'z25': sqlalchemy.types.FLOAT(),
                                                                              'z30': sqlalchemy.types.FLOAT(),
                                                                              'z45': sqlalchemy.types.FLOAT(),
                                                                              'z60': sqlalchemy.types.FLOAT(),
                                                                              'z90': sqlalchemy.types.FLOAT(),
                                                                              'z120': sqlalchemy.types.FLOAT(),
                                                                              'z150': sqlalchemy.types.FLOAT(),
                                                                              'z180': sqlalchemy.types.FLOAT(),
                                                                              'z360': sqlalchemy.types.FLOAT(),
                                                                              'z720': sqlalchemy.types.FLOAT(),
                                                                              'z1440': sqlalchemy.types.FLOAT(),
                                                                              'n1': sqlalchemy.types.FLOAT(),
                                                                              'n2': sqlalchemy.types.FLOAT(),
                                                                              'n3': sqlalchemy.types.FLOAT(),
                                                                              'n4': sqlalchemy.types.FLOAT(),
                                                                              'n5': sqlalchemy.types.FLOAT(),
                                                                              'n6': sqlalchemy.types.FLOAT(),
                                                                              'n7': sqlalchemy.types.FLOAT(),
                                                                              'n8': sqlalchemy.types.FLOAT(),
                                                                              'n9': sqlalchemy.types.FLOAT(),
                                                                              'n10': sqlalchemy.types.FLOAT(),
                                                                              'n15': sqlalchemy.types.FLOAT(),
                                                                              'n20': sqlalchemy.types.FLOAT(),
                                                                              'n30': sqlalchemy.types.FLOAT(),
                                                                              'n60': sqlalchemy.types.FLOAT(),
                                                                              'n90': sqlalchemy.types.FLOAT()
                                                                              })
        # 设定主键
        with self.engine.connect() as con:
            #设置非空和主键
            con.execute("ALTER TABLE jjzf alter column id BIGINT not null")
            con.execute("ALTER TABLE jjzf ADD PRIMARY KEY(id)")
            #更新数据
            con.execute("UPDATE dayinfo SET [day5] = jjzf.day5,[day10] = jjzf.day10," \
                        "[day15] = jjzf.day15,[day20] = jjzf.day20," \
                        "[day25] = jjzf.day25,[day30] = jjzf.day30," \
                        "[day45] = jjzf.day45,[day60] = jjzf.day60," \
                        "[day90] = jjzf.day90,[day120] = jjzf.day120," \
                        "[day150] = jjzf.day150,[day180] = jjzf.day180," \
                        "[day360] = jjzf.day360,[day720] = jjzf.day720," \
                        "[day1440] = jjzf.day1440," \
                        "[z5] = jjzf.z5 ,[z10] = jjzf.z10,[z15] = jjzf.z15," \
                        "[z20] = jjzf.z20 ,[z25] = jjzf.z25,[z30] = jjzf.z30," \
                        "[z45] = jjzf.z45 ,[z60] = jjzf.z60,[z90] = jjzf.z90," \
                        "[z120] = jjzf.z120 ,[z150] = jjzf.z150,[z180] = jjzf.z180," \
                        "[z360] = jjzf.z360 ,[z720] = jjzf.z720,[z1440] = jjzf.z1440, " \
                        "[n1] = jjzf.n1 ,[n2] = jjzf.n2,[n3] = jjzf.n3," \
                        "[n4] = jjzf.n4,[n5] = jjzf.n5," \
                        "[n6] = jjzf.n6 ,[n7] = jjzf.n7,[n8] = jjzf.n8," \
                        "[n9] = jjzf.n9 ,[n10] = jjzf.n10," \
                        "[n15] = jjzf.n15 ,[n20] = jjzf.n20," \
                        "[n30] = jjzf.n30 ,[n60] = jjzf.n60,[n90] = jjzf.n90 " \
                        " from jjzf,dayinfo WHERE  dayinfo.id = jjzf.id")

        #sql = "UPDATE dayinfo SET [day5] = jjzf.day5 from jjzf,dayinfo WHERE  dayinfo.id = jjzf.id "


