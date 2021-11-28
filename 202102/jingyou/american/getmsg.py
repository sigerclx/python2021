import requests,json

searchheader ={
  "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",
  "content-type" : "application/json; charset=utf-8", #application/json;charset=UTF8  ，"text/html; charset=utf-8"
   "referer":"https://servicewechat.com/wx27c8c2dad98ab660/107/page-frame.html",
  "Accept": "*/*",
  "Accept-Language": "zh-CN",
 "Accept-Encoding": "gzip, deflate, br"
}


def isNone(x):
    if x is None:
        return ''
    else:
        return x


def returnJson(url,searchheader):
    resulttxt= requests.request('get', url, headers=searchheader)
    #resulttxt =  json.loads(resulttxt.text)
    return resulttxt.text

url="https://www.doterra.com/US/zh/education/pe/wild-orange-oil"

print(returnJson(url,searchheader))