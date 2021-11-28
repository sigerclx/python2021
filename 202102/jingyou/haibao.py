#73种海报配方
import requests,json

def returnJson(url,searchheader):
    result= requests.request('get', url, headers=searchheader)
    resulttxt =  json.loads(result.text)
    return resulttxt

s1="https://wx.drmom.cn/jywy-wx/posterManage/all?posterReviewType=11&nonce_str=j4DkK3i4iYz8PYRQsifddwSjypcPBJ7m&sign=789c7d5ab62b8eb3c22d4a2774997af8"


searchheader ={
  "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",
  "content-type" : "text/html; charset=utf-8", #application/json;charset=UTF8  ，"text/html; charset=utf-8"
  "Token":"8ca48c6e1f6fcf33c40dc48e08f5776c",
  #8ca48c6e1f6fcf33c40dc48e08f5776c
   "referer":"https://servicewechat.com/wx27c8c2dad98ab660/107/page-frame.html",
  "Accept": "*/*",
  "Accept-Language": "zh-CN",
 "Accept-Encoding": "gzip, deflate, br"
}

data = returnJson(s1,searchheader)
print(data)
chang = len(data['data'])
print(len(data))

value = data['data']
for i in range(chang):
    print(value[i]['textBody'])





