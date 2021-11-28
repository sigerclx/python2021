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
    result= requests.request('get', url, headers=searchheader)
    resulttxt =  json.loads(result.text)
    return resulttxt

def produce1(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'w', encoding='utf-8')
    #print(data)
    cnName =data['data']['cnName']
    enName =data['data']['enName']
    botanicalName =data['data']['botanicalName']
    keywordList =data['data']['keywordList']
    f1.write(cnName+' 英文名：'+enName+" 拉丁名："+botanicalName)
    f1.write("\n功能: ")
    for i in range(len(keywordList)):
        f1.write(keywordList[i]['keywordTypeName']+" ")
    f1.write("\n")

def produce2(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
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
    f1.write('\n中文别名:'+oilChineseOtherName)
    f1.write('\n英文别名:'+oilEnglishOtherName)
    f1.write('\n植物属科:'+plantFamilyName+' '+plantFamilyName)
    f1.write('\n主要产地:'+origin)
    f1.write('\n萃取部位:'+' '+isNone(plantPartCnName)+' '+isNone(plantPartEnName))
    f1.write('\n萃取方式'+extractionMethodName+' '+extractionMethodEnName)
    f1.close()



def produce3(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
    #print(data)
    bodySystemList =data['data']['bodySystemList']
    f1.write("\n\n适用系统：\n"+str(bodySystemList)+"\n")
    healingAttributePhysiologyList = data['data']['healingAttributePhysiologyList']
    f1.write("\n疗愈属性：\n")
    f1.write("\n生理方面：\n")
    for i in range(len(healingAttributePhysiologyList)):
        f1.write(healingAttributePhysiologyList[i]['chineseName']+" "+str(healingAttributePhysiologyList[i]['recommendLevel'])+" "+"星\n") #healingAttributePhysiologyList[i]['englishName'],

    f1.write("\n心理方面：\n")
    healingAttributeMentalityList = data['data']['healingAttributeMentalityList']
    for i in range(len(healingAttributeMentalityList)):
        f1.write(healingAttributeMentalityList[i]['chineseName']+" "+str(healingAttributeMentalityList[i]['recommendLevel'])+" "+"星\ns") #,healingAttributeMentalityList[i]['englishName']

    f1.write("\n用途：\n")
    healthConditionList = data['data']['healthConditionList']
    for i in range(len(healthConditionList)):
        f1.write("\n"+healthConditionList[i]['typeBaseKindCnName']+":\n")
        healthConditionList1 = data['data']['healthConditionList'][i]['healthConditionList']
        for j in range(len(healthConditionList1)):
            f1.write(healthConditionList1[j]['conditionCnName']+" "+str(healthConditionList1[j]['recommendLevel'])+" 星\n")
    f1.close()

def produce4(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
    #print(data)
    f1.write('\n安全:')
    f1.write('\n可用于香薰:'+str(data['data']['aromatically']))
    f1.write('\n可用于涂抹:'+str(data['data']['topically']))
    f1.write('\n可用于口服:'+str(data['data']['internally']))
    f1.write('\n安全提示:')
    for i in range(len(data['data']['safetyWarningList'])):
        f1.write("\n"+str(i+1)+"、"+ data['data']['safetyWarningList'][i]['chineseName']+" ")
        f1.write('\n严重级别:'+ str(data['data']['safetyWarningList'][i]['severityLevel']))
        f1.write('\n描述:'+ data['data']['safetyWarningList'][i]['description'])

    f1.write('\n刺激性:'+data['data']['dilutionLevel']['subName'])
    f1.write('\n光敏性:'+data['data']['avoidSunlightLevel']['subName'])

    f1.write("\nFDA认证： ")
    for i in range(len(data['data']['fdaList'])):
        f1.write(isNone(data['data']['fdaList'][i]['subName'])+ isNone(data['data']['fdaList'][i]['description'])+"\n")
    f1.write("国际认证：")
    try:
        f1.write(isNone(data['data']['cfda']['subName'])+ isNone(data['data']['cfda']['description']))
    except Exception:
        f1.write("无\n")
    f1.close()



def produce5(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
    #print(data)
    f1.write("\n\n简易用法：\n")
    for i in range(len(data['data'])):
        f1.write('\n用法'+str(i+1)+": "+data['data'][i]['recipeTitle']+' : '+data['data'][i]['recipeDescription'])
    f1.close()


def produce6(s,danfangName,searchheader=searchheader):
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
    data = returnJson(s,searchheader)
    #print(data)
    f1.write('\n\n精油属性:')
    f1.write('\n气味特征:'+data['data']['aromaticDescription'])
    f1.write('\n香氛族群:'+data['data']['aromaticGroup']['subName'])
    f1.write('\n香气音调:'+data['data']['aromaticToneName'])
    f1.write('\n气味强度:'+str(data['data']['aromaticStrengthLevel']))
    f1.write('\n粘稠度:'+str(data['data']['consistencyLevel']))
    f1.write('\n易保存度:'+str(data['data']['easySaveLevel']['subId'])+' , '+data['data']['easySaveLevel']['subName']+' , '+data['data']['easySaveLevel']['description'])
    f1.write('\n颜色:'+data['data']['colorDescription'])
    f1.close()

def produce7(s,danfangName,searchheader=searchheader):
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
    # print(data)
    data = returnJson(s,searchheader)

    f1.write("\n\n含有该精油的复方：\n")
    for i in range(len(data['data'])):
        f1.write('\n复方'+str(i+1)+" : "+ data['data'][i]['oilChineseName']+'('+data['data'][i]['oilEnglishName']+')')
        f1.write('\n功能:')
        for j in range(len(data['data'][i]['keywordList'])):
            f1.write(data['data'][i]['keywordList'][j]['keywordTypeName']+"、")
    f1.write("\n")
    f1.close()


def produce8(s, danfangName,searchheader=searchheader):
    data = returnJson(s, searchheader)
    f1 = open(r'danfanglist/' + danfangName + '.txt', 'a',encoding='utf-8')
    #print(data)
    f1.write("\n\n了解更多：\n")
    f1.write("\n1、关于植物：\n")
    f1.write(data['data']['plantForm'])
    f1.write("\n2、历史故事：\n")
    f1.write(data['data']['history'])
    f1.write("\n3、精油特点：\n")
    f1.write(data['data']['description'])
    f1.close()
