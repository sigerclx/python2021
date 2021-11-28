from enum import Enum
class Topurl(Enum):
    #day='https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=rzdf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.7309746407127156'
    week = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.594073948145458'
    month = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=1yzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.723692375495989'
    month3 = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-06-27&ed=2091-06-27&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.8260496759054652'
    month6 = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.7865579477777791'
    year = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=1nzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.7865579477777793'
    year2 = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=2nzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.7865579477777794'
    year3 = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=3nzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.7865579477777795'
    thisyear = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=jnzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.7865579477777791'
    allyear = 'https://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=lnzf&st=desc&sd=2020-06-27&ed=2021-06-28&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.7865579477777791'

#
# for i in Topurl:
#     print(i.value)