from lxml import etree
import json,random,requests,ast
class jijin:
    no = '',
    name ='',
    jiancheng = '',
    date ='',
    dwjz ='',
    ljjj ='',
    rzzl ='',
    week = '',
    month3 ='',
    month6 ='',
    year ='',
    year2 ='',
    year3 ='',
    thisyear ='',
    establish ='',
    fee=''

headers = {
            "User-Agent":"Mozilla/5.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Referer": "http://fund.eastmoney.com/"
        }


url = 'http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;s6yzf;pn50;ddesc;qsd20200627;qed20210627;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb'
url='http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-06-27&ed=2021-06-27&qdii=&tabSubtype=,,,,,&pi=1&pn=100&dx=1&v=0.2893811077855697'
url='http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=rzdf&st=desc&sd=2020-06-27&ed=2021-06-27&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.46007574245710603'
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
htmltext = response.text
s1 = htmltext.index('[')
s2 = htmltext.index(']')
data =htmltext[s1+2:s2-1].split('\",\"')


for i in data:
    print(i)

