import pandas as pd
from  jjclass.zhangfu import zf
from sql.tomssql import Write_df
import sys
from sql.mssql import MSSQL
from sql.tomssql import Write_df


def main():
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)

    # 清洗并下载基金名录，存入文件data/base/nolist.txt


    mssql = MSSQL(host="192.168.0.51",user="sa",pwd="a1b2/a",db="Jijin")

    jjnolist= mssql.ExecQuery("select no from getmaxmindate")
    record = len(jjnolist)
    count= 0
    for no in jjnolist:
        count+=1
        print('\n当前基金：',no[0],count,'/',record)
        #sys.exit(0)
        jjdata = mssql.ExecQuery("select id,no,jingzhi,day5 from dayinfo where no='" +no[0]+"' and jingzhi<>0 order by date")
        #jjdata = mssql.ExecQuery("select id,no,jingzhi,day5 from dayinfo where no= '007928' order by date")
        #fieldName =['id','No','date','jingzhi','leiji','zhangfu','statusbuy','statussell','remark','day5']
        #print(jjdata)
        fieldName = ['id', 'No', 'jingzhi','day5']
        jijinDFall = pd.DataFrame(data=jjdata,columns=fieldName)
        zhangfu  = zf(jijinDFall)

        # currentdf 是当前净值未更新的数据行
        currentdf = zhangfu.filter()
        print('取出当前计算数据')
        # 数据要更新涨幅的行数大于5行，认为有数据可更新，否则不用更新
        if(len(currentdf)>5):
            # 计算涨幅字段
            alldf = zhangfu.alljingzhi(currentdf)
            print('净值计算完毕')
            zhangfudf = zhangfu.getzhangfu(alldf)
            #jj = pd.merge(currentdf, df)
            print('涨幅计算完毕')
            #print(zhangfudf)
            zfwritedb = Write_df()
            zfwritedb.write_jjzf(zhangfudf)
            print('数据库写入完毕')


if __name__ == '__main__':
    main()