#清洁推荐用油
import requests,json

def returnJson(url,searchheader):
    result= requests.request('get', url, headers=searchheader)
    resulttxt =  json.loads(result.text)
    return resulttxt

s1='https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBaseInfById?oilId=S0044&nonce_str=mFCGttBpri8sirHtHhGkEm7HmNiKbREC&sign=8dd56b6ef8107d353bee7aae4e2b85b8'
s2="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBotanyById?oilId=S0044&nonce_str=K6e6cNWDYbAsjGW8HM5nkscHcpxksFy2&sign=f7c5ed6a1e60eed642216b0e346f5d60"
s3="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfSpiritualHealingById?oilId=S0044&nonce_str=ETYjhWSBKdH57YYFPCiZsfQh6rPApQpD&sign=2ea1cee9afade7bc02a435147b45d736"
s4="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfSafetyById?oilId=S0044&nonce_str=HfjyjPBMe3S27rwSXmWPzNMiA3CW4fxW&sign=68d966476a48aae91ef17ed021d41344"
s5="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchUseMethod?oilId=S0044&nonce_str=Htw7zXfDjQNaPEMxjkPt4yGTXWCNzSWR&sign=4b856f0931f38f7892b8d824eef7dd6b"
s6="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfAttrById?oilId=S0044&nonce_str=8dDjEwP47TBKBfJZAweR4p52pSF4BJaf&sign=f1d43cabb2bc2e709058e15495031506"
s7="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfMoreById?oilId=S0044&nonce_str=QB7AdY4GXbzr7JmjdBQfkMGxKmTJRtS8&sign=7e03de51d84cb5cf1d1aa61feba8469e"
s8="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBlendOil?oilId=S0044&nonce_str=mmXmnDKkd3NympjNZJccxJxmrGXAP7fE&sign=44947046050097e59d1b8c2f1a64ca44"
s9="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfResearchById?oilId=S0044&nonce_str=CXWKeYn8zHinxA664dhGE57SDH2QKnSE&sign=ab26d6ca4c90f92b951e7e994460c7f1"




searchheader ={
  "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",
  "content-type" : "application/json; charset=utf-8", #application/json;charset=UTF8  ，"text/html; charset=utf-8"
  "Token":"8ca48c6e1f6fcf33c40dc48e08f5776c",
  #8ca48c6e1f6fcf33c40dc48e08f5776c
   "referer":"https://servicewechat.com/wx27c8c2dad98ab660/107/page-frame.html",
  "Accept": "*/*",
  "Accept-Language": "zh-CN",
 "Accept-Encoding": "gzip, deflate, br"
}


print(returnJson(s1,searchheader))
print(returnJson(s2,searchheader))
print(returnJson(s3,searchheader))
print(returnJson(s4,searchheader))
print(returnJson(s5,searchheader))
print(returnJson(s6,searchheader))
print(returnJson(s7,searchheader))
print(returnJson(s8,searchheader))
print(returnJson(s9,searchheader))




