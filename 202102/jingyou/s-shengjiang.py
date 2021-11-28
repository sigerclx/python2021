#获取单方精油信息
import requests,json

searchheader ={
  "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",
  "content-type" : "application/json; charset=utf-8", #application/json;charset=UTF8  ，"text/html; charset=utf-8"
   "referer":"https://servicewechat.com/wx27c8c2dad98ab660/107/page-frame.html",
  "Accept": "*/*",
  "Accept-Language": "zh-CN",
 "Accept-Encoding": "gzip, deflate, br",
 "Token":"7208b02ed93a9ca8e55cdcf496f799c2"
}

def returnJson(url,searchheader):
    result= requests.request('get', url, headers=searchheader)
    resulttxt =  json.loads(result.text)
    return resulttxt

def produce1(s,searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    cnName =data['data']['cnName']
    enName =data['data']['enName']
    botanicalName =data['data']['botanicalName']
    keywordList =data['data']['keywordList']
    print(cnName,'英文名：'+enName,"拉丁名："+botanicalName)
    for i in range(len(keywordList)):
        print(keywordList[i]['keywordTypeName'])

def produce2(s,searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    oilChineseOtherName =data['data']['oilChineseOtherName']
    oilEnglishOtherName =data['data']['oilEnglishOtherName']
    plantFamilyName =data['data']['plantFamilyName']
    plantGenusName =data['data']['plantGenusName']
    origin =data['data']['origin']
    partClassCnName =data['data']['partClassCnName']
    plantPartCnName =data['data']['plantPartCnName']
    plantPartEnName =data['data']['plantPartEnName']
    extractionMethodName =data['data']['extractionMethodName']
    extractionMethodEnName =data['data']['extractionMethodEnName']
    print('中文别名:'+oilChineseOtherName)
    print('英文别名:'+oilEnglishOtherName)
    print('植物属科:'+plantFamilyName+' '+plantFamilyName)
    print('主要产地:'+origin)
    print('萃取部位:'+partClassCnName+' '+plantPartCnName+' '+plantPartEnName)
    print('萃取方式'+extractionMethodName+' '+extractionMethodEnName)




def produce3(s,searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    bodySystemList =data['data']['bodySystemList']
    print("适用系统：\n",bodySystemList)
    healingAttributePhysiologyList = data['data']['healingAttributePhysiologyList']

    for i in range(len(healingAttributePhysiologyList)):
        print(healingAttributePhysiologyList[i]['chineseName'],healingAttributePhysiologyList[i]['recommendLevel'],"星") #healingAttributePhysiologyList[i]['englishName'],

    print("心理方面：\n")
    healingAttributeMentalityList = data['data']['healingAttributeMentalityList']
    for i in range(len(healingAttributeMentalityList)):
        print(healingAttributeMentalityList[i]['chineseName'],healingAttributeMentalityList[i]['recommendLevel'],"星") #,healingAttributeMentalityList[i]['englishName']

    print("用途：\n")
    healthConditionList = data['data']['healthConditionList']
    for i in range(len(healthConditionList)):
        print("\n",healthConditionList[i]['typeBaseKindCnName'],":\n")
        healthConditionList1 = data['data']['healthConditionList'][i]['healthConditionList']
        for j in range(len(healthConditionList1)):
            print(healthConditionList1[j]['conditionCnName'],healthConditionList1[j]['recommendLevel'],"星")


def produce4(s,searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    print('可用于香薰:',data['data']['aromatically'])
    print('可用于涂抹:',data['data']['topically'])
    print('可用于口服:',data['data']['internally'])
    print('安全提示:')
    for i in range(len(data['data']['safetyWarningList'])):
        print('提示:',i+1, data['data']['safetyWarningList'][i]['chineseName'],end=" ")
        print('严重级别:', data['data']['safetyWarningList'][i]['severityLevel'])
        print('描述:', data['data']['safetyWarningList'][i]['description'])

    print('刺激性:',data['data']['dilutionLevel']['subName'])
    print('光敏性:',data['data']['avoidSunlightLevel']['subName'])

    print("FDA认证：")
    for i in range(len(data['data']['fdaList'])):
        print(data['data']['fdaList'][i]['subName'], data['data']['fdaList'][i]['description'])
    print("国际认证：")
    print(data['data']['cfda']['subName'], data['data']['cfda']['description'])



def produce5(s,searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    print("简易用法：")
    for i in range(len(data['data'])):
        print('用法',i+1, data['data'][i]['recipeTitle'],':',data['data'][i]['recipeDescription'])



def produce6(s,searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    print('气味特征:',data['data']['aromaticDescription'])
    print('香氛族群:',data['data']['aromaticGroup']['subName'])
    print('香气音调:',data['data']['aromaticToneName'])
    print('气味强度:',data['data']['aromaticStrengthLevel'])
    print('粘稠度:',data['data']['consistencyLevel'])
    print('易保存度:',data['data']['easySaveLevel']['subId'],',',data['data']['easySaveLevel']['subName'],data['data']['easySaveLevel']['description'])
    print('颜色:',data['data']['colorDescription'])

def produce7(s,searchheader):
    data = returnJson(s,searchheader)
    #print(data)

    print("含有该精油的复方：")
    for i in range(len(data['data'])):
        print('\n复方',i+1,":", data['data'][i]['oilChineseName'],'(',data['data'][i]['oilEnglishName'],')')
        print('功能:',end="")
        for j in range(len(data['data'][i]['keywordList'])):
            print(data['data'][i]['keywordList'][j]['keywordTypeName'],end="、")


def produce8(s, searchheader):
    data = returnJson(s, searchheader)
    #print(data)
    print("了解更多：")
    print("1、关于植物：")
    print(data['data']['plantForm'])
    print("2、历史故事：")
    print(data['data']['history'])
    print("3、精油特点：")
    print(data['data']['description'])


filters = ["searchBaseInfById","searchBotanyById","searchSingleOilBaseInfSpiritualHealingById","searchSingleOilBaseInfSafetyById","searchUseMethod","searchSingleOilBaseInfAttrById","searchBlendOil","searchSingleOilBaseInfMoreById"]
urlS = []

s1="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfSpiritualHealingById?oilId=S0031&familyMemberId=15774&nonce_str=pwrYx8ZTnhd5wKyKwMTtSypifJbiPs3k&sign=14deb02c92a66550999d87d9cd5b6a94"
s2="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBaseInfById?oilId=S0031&familyMemberId=15774&nonce_str=sZZfadBsWwESMnkz3kAX8yRBmMAZXHST&sign=ee5593777ff9d663ce2afd34d5a31a00"
s3="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBotanyById?oilId=S0031&familyMemberId=15774&nonce_str=Srah5ec88YiMhGa6mzpjz2ZbycAbayf2&sign=3a881c53ed43c9fc293866e39255c70b"
s4="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfSafetyById?oilId=S0031&familyMemberId=15774&nonce_str=4WHAHfcw2JASkWpXF3ZMjeAFw32WAdXQ&sign=e157b8752bc0b9769f765ed016cb7904"
s5="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchUseMethod?oilId=S0031&familyMemberId=15774&nonce_str=rHh5mWcSnfhB4SebMCDMakE4Dw7iZMjQ&sign=183150dc1506ded5a0eca1f78acb01cb"
s6="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfAttrById?oilId=S0031&familyMemberId=15774&nonce_str=DBKW8znPNBHJfctdixphxY7ZwsK8FCa7&sign=61358f2a53d77061277bb0e9bd5d08e2"
s7="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfMoreById?oilId=S0031&familyMemberId=15774&nonce_str=bwRtRDXM4chRncy2hAESWtWRtd7SCbnp&sign=b02343d53a790493438cc61049bb27f2"
s8="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBlendOil?oilId=S0031&familyMemberId=15774&nonce_str=DbTGJp2GrB7D3KN3GFdfRynRajMY2MDP&sign=7d7ffd6b8102342432f4bedf60f3271b"

urlS.append(s1)
urlS.append(s2)
urlS.append(s3)
urlS.append(s4)
urlS.append(s5)
urlS.append(s6)
urlS.append(s7)
urlS.append(s8)

for keyword in filters:
    #print("keyword",keyword)
    for s in urlS:
        #print("s=",s)
        if keyword in s and keyword==filters[0]: produce1(s,searchheader)
        if keyword in s and keyword==filters[1]: produce2(s,searchheader)
        if keyword in s and keyword==filters[2]: produce3(s,searchheader)
        if keyword in s and keyword==filters[3]: produce4(s,searchheader)
        if keyword in s and keyword==filters[4]: produce5(s,searchheader)
        if keyword in s and keyword==filters[5]: produce6(s,searchheader)
        if keyword in s and keyword==filters[6]: produce7(s,searchheader)
        if keyword in s and keyword == filters[7]: produce8(s, searchheader)
    print("\n-------------------------------\n")











