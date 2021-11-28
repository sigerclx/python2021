#获取单方精油信息
import requests,json

searchheader ={
  "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",
  "content-type" : "application/json; charset=utf-8", #application/json;charset=UTF8  ，"text/html; charset=utf-8"
   "referer":"https://servicewechat.com/wx27c8c2dad98ab660/107/page-frame.html",
  "Accept": "*/*",
  "Accept-Language": "zh-CN",
 "Accept-Encoding": "gzip, deflate, br",
 "Token":"8d14b1c318cd168c91dba3066c7a6109"
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
    print("适用系统：",bodySystemList)
    healingAttributePhysiologyList = data['data']['healingAttributePhysiologyList']

    for i in range(len(healingAttributePhysiologyList)):
        print(healingAttributePhysiologyList[i]['chineseName'],healingAttributePhysiologyList[i]['recommendLevel'],"星") #healingAttributePhysiologyList[i]['englishName'],

    print("心理方面：")
    healingAttributeMentalityList = data['data']['healingAttributeMentalityList']
    for i in range(len(healingAttributeMentalityList)):
        print(healingAttributeMentalityList[i]['chineseName'],healingAttributeMentalityList[i]['recommendLevel'],"星") #,healingAttributeMentalityList[i]['englishName']

    print("用途：")
    healthConditionList = data['data']['healthConditionList']
    for i in range(len(healthConditionList)):
        print(healthConditionList[i]['typeBaseKindCnName'],":")
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

s1="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBaseInfById?oilId=S0009&familyMemberId=15774&nonce_str=jdE2r4hzfjJHkDwaiB3jPe27diA3AsTf&sign=1f1bd658b27167cd033bc63785a37bd6"
s2="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBotanyById?oilId=S0009&familyMemberId=15774&nonce_str=PknsPsHTkkiD6F2Hh23bb3Sb45dD8WZA&sign=d5a13ae859567e3ba6d4e2c26be160b9"
s3="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfSpiritualHealingById?oilId=S0009&familyMemberId=15774&nonce_str=NZEYCCke8zbHmWji7aah8DMDzhhepmwR&sign=941938a299b5500468042c6143a519ba"
s4="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfSafetyById?oilId=S0009&familyMemberId=15774&nonce_str=73SCBmY2K2RjmSbGsAb3J2Xr7cZRBfYT&sign=929f9fa64a7714a267e3fde4c2d99648"
s5="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchUseMethod?oilId=S0009&familyMemberId=15774&nonce_str=SrrPeHhwccQyyfxyE6BdPpBGXXAbGD5D&sign=9a764ad27e8ce7268fd63accc2e4d745"
s6="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfAttrById?oilId=S0009&familyMemberId=15774&nonce_str=QMCP45nXc4treEP5AW54riC34tTyW7PA&sign=7dbd6a7758217f09877007fa62fb296d"
s7="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchBlendOil?oilId=S0009&familyMemberId=15774&nonce_str=wwhcfHE7xwMTW7FpnsecXJs6BYAQWyp5&sign=a3013e6a730f3a9b4459d4aa3a6d7bab"
s8="https://wx.drmom.cn/jywy-wx/singleOilBaseInf/searchSingleOilBaseInfMoreById?oilId=S0009&familyMemberId=15774&nonce_str=mWEmTReb6JZb35diSFBS3EQswxGE8KH2&sign=fef263b93442a66924849324f2c43ac7"
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











