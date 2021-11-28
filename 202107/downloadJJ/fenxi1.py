'''
计算某一基金，累计上涨和累计下跌的量,month
'''
import pandas as pd
from sql.mssql import MSSQL


def main():
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    mssql = MSSQL(host="192.168.0.51",user="sa",pwd="a1b2/a",db="Jijin")
    no='004995'
    jjdf= mssql.ExecQuery("select id,no,date,jingzhi,zhangfu from dayinfo where no='" +no+"' order by date")
    record = len(jjdf)
    print('records=',record)
    count= 0

    fieldName =  ['id','no','date', 'jingzhi',  'zhangfu']
    jijin = pd.DataFrame(data=jjdf, columns=fieldName)
    # 设定基金列名，对应数据表的字段名

    #col_name = jijin.columns.tolist()  # 将jijinDF的列名全部提取出来存放在列表里
    #print(col_name)
    #fieldName.insert(5, 'type')  # 在列索引为4的位置插入一列,列名为:type，刚插入时不会有值，整列都是NaN
    #jijinDF = jijin.reindex(columns=fieldName)  # DataFrame.reindex() 对原行/列索引重新构建索引值
    #print(jijin)
    lines = []
    lastflag = 10
    for i,data in jijin.iterrows():
        line=[]
        zhangfu = data['zhangfu']
        if zhangfu>0 :
            flag = 1
        else:
            flag = 0
        if lastflag!=flag :
            if lastflag!=10 :
                line.append(data['no'])
                line.append(round(sum,2))
                line.append(count)
                line.append(lastdate)
                lines.append(line)
            sum = 0
            count= 0
            lastflag = flag
            lastdate = data['date']

        sum =  sum + zhangfu
        count = count + 1

    #print(lines)

    fieldName = ['no', 'fu','count', 'date']
    jijinsum = pd.DataFrame(data=lines, columns=fieldName)
    print(jijinsum['fu'].max(),jijinsum['fu'].min(),jijinsum['count'].max())
    print(jijinsum)


if __name__ == '__main__':
    main()