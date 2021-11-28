#124种单方精油
import requests,json

def returnJson(url,searchheader):
    result= requests.request('get', url, headers=searchheader)
    #resulttxt =  json.loads(result.text)
    return result

s1="https://wx.drmom.cn/jywy-wx/keyword/searchAll?keyword=%E7%94%9F%E5%A7%9C&familyMemberId=15774&nonce_str=TKxKzTXyyzcSdTWDsSitBtWCz8dhMtwG&sign=552088c36d8447a00524dbac262e79ff"
searchheader ={
  "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",
  "content-type" : "text/html; charset=utf-8", #application/json;charset=UTF8  ，"text/html; charset=utf-8"
  "Token":"e21d42e6fa1407e2d19542c63ab3287e",
  #8ca48c6e1f6fcf33c40dc48e08f5776c
   "referer":"https://servicewechat.com/wx27c8c2dad98ab660/107/page-frame.html",
  "Accept": "*/*",
  "Accept-Language": "zh-CN",
 "Accept-Encoding": "gzip, deflate, br"
}

data = returnJson(s1,searchheader)
print(data.text)







