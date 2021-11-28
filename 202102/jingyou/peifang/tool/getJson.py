import requests,json

searchheader ={
  "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",
  "content-type" : "application/json; charset=utf-8", #application/json;charset=UTF8  ，"text/html; charset=utf-8"
   "referer":"https://servicewechat.com/wx27c8c2dad98ab660/107/page-frame.html",
  "Accept": "*/*",
  "Accept-Language": "zh-CN",
 "Accept-Encoding": "gzip, deflate, br"
}
import os

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print(root) #当前目录路径
        #print(dirs) #当前路径下所有子目录
        return files #当前路径下所有非目录子文件


import tool.readurl
peifangList=[]

def start(Name):
    urlS =tool.readurl.getpeifangUrl(Name)
    filters = ["searchBaseInf",  "recipeGroup","recipeConditioningStage",
               "related"]
    for keyword in filters:
        #print("keyword",keyword)
        for s in urlS:
            #print("s=",s)
            if keyword in s and keyword==filters[0]: tool.getJson.produce1(s,Name)
            if keyword in s and keyword==filters[1]: tool.getJson.produce3(s,Name)
            if keyword in s and keyword == filters[2]: tool.getJson.produce2(s, Name)
            if keyword in s and keyword==filters[3]: tool.getJson.produce4(s,Name)



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
    f1 = open(r'peifanglist/' + danfangName + '.txt', 'w', encoding='utf-8')
    print(data)
    #keywordList = data['data']['objectOthersList']
    cnName = data['data']['cnName']
    enName = data['data']['enName']
    otherName = data['data']['otherName']
    f1.write(cnName + ' 英文名：' + enName+ ' 别名：'  +otherName+"\n")
    f1.write('适用：' + data['data']['objectAgeGroup']+"\n")
    f1.write("\n")

def produce2(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    f1 = open(r'peifanglist/' + danfangName + '.txt', 'a', encoding='utf-8')

    data = data['data']

    for i in range(len(data)):
        f1.write(data[i]['stageName'] + "\n")
        f1.write("症状描述：\n")
        f1.write(data[i]['description'] + "\n\n")
        f1.write(peifangList[i])
    f1.close()

def produce3(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    #f1 = open(r'peifanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
    print(data)
    data =data['data']
    writeList =""
    for i in range(len(data)):
        writeList = writeList +data[i]['detailName']+":"+data[i]['effectInGroup']+"\n"
        writeList = writeList +"用法:"+data[i]["usageName"] + "  方式："+data[i]['usageClassValue'] + "\n"

        if data[i]['singleTechnique'] is None:
            try:
                blendTechnique = data[i]['multiTechnique']['blendTechnique']['techniqueDescription']
                writeList = writeList + "\n调配方法：\n"
                writeList = writeList + blendTechnique + "\n"
            except Exception:
                writeList = writeList + "\n"


            eachDoseValue = data[i]['multiTechnique']['eachDoseValue']
            writeList = writeList +"\n每次用量："+str(eachDoseValue) + "\n"

            try:
                mainTechnique = data[i]['multiTechnique']['mainTechnique']['techniqueDescription']
                writeList = writeList +"\n使用手法：\n"
                writeList = writeList +mainTechnique+"\n"
            except Exception:
                writeList = writeList + "\n"



            try:
                tipsTechnique = isNone(data[i]['multiTechnique']['tipsTechnique']['techniqueDescription'])
                writeList = writeList + "\n小提示：\n"
                writeList = writeList +tipsTechnique+"\n"
            except Exception:
                writeList = writeList + "\n"
        else:
            try:
                mainTechnique = data[i]['singleTechnique']['mainTechnique']['techniqueDescription']
                writeList = writeList +"\n使用手法：\n"
                writeList = writeList +mainTechnique+"\n"
            except Exception:
                writeList = writeList + "\n"

            try:
                tipsTechnique = isNone(data[i]['singleTechnique']['tipsTechnique']['techniqueDescription'])
                writeList = writeList + "\n小提示：\n"
                writeList = writeList +tipsTechnique+"\n"
            except Exception:
                writeList = writeList + "\n"


        writeList = writeList +"\n使用频次：\n"
        frequencyValue = data[i]['frequencyValue']
        writeList = writeList +str(frequencyValue) + "\n"
        writeList = writeList +"\n配方：(单次用量)\n"
        writeList = writeList +"稀释比例："+isNone(data[i]['dilutionRateValue']) + "\n"
        recipeDoseDetailList = data[i]['recipeDoseDetailList']
        for j in range(len(recipeDoseDetailList)):
            writeList = writeList+recipeDoseDetailList[j]['mixtureName'] + " " + str(recipeDoseDetailList[j]['doseValue']) + recipeDoseDetailList[j]['doseUnitValue']

            if len(recipeDoseDetailList[j]['recipeDoseDetailReplaceList'])>0:
                writeList= writeList+"  替代精油列表：["
                for k in range(len(recipeDoseDetailList[j]['recipeDoseDetailReplaceList'])):
                    writeList = writeList + recipeDoseDetailList[j]['recipeDoseDetailReplaceList'][k]['mixtureName']+" "
                writeList = writeList + "]"
            writeList = writeList +"\n"
        writeList = "分装瓶:"+writeList + isNone(data[i]['defaultBottleTypeValue'])+"\n"
        writeList = writeList +"------------\n\n"

        """
        f1.write(data[i]['detailName']+":"+data[i]['effectInGroup']+"\n")
        f1.write("用法:"+data[i]["usageName"] + "  方式："+data[i]['usageClassValue'] + "\n")

        f1.write("\n使用手法：\n")
        singleTechnique = data[i]['singleTechnique']['mainTechnique']['techniqueDescription']
        f1.write(singleTechnique+"\n")
        f1.write("\n使用频次：\n")
        frequencyValue = data[i]['frequencyValue']
        f1.write(str(frequencyValue) + "\n")
        f1.write("\n配方：(单次用量)\n")
        f1.write("稀释比例："+data[i]['dilutionRateValue'] + "\n")
        recipeDoseDetailList=data[i]['recipeDoseDetailList']
        for j in range(len(recipeDoseDetailList)):
            f1.write(recipeDoseDetailList[j]['mixtureName'] +" "+ str(recipeDoseDetailList[j]['doseValue'])+recipeDoseDetailList[j]['doseUnitValue']+"\n")
        f1.write("\n\n")
        """


    peifangList.append(writeList)
    #f1.close()

def produce4(s,danfangName,searchheader=searchheader):
    data = returnJson(s,searchheader)
    #print(data)
    f1 = open(r'peifanglist/' + danfangName + '.txt', 'a', encoding='utf-8')
    #print(data)
    f1.write('\n延伸配方:')

    for i in range(len(data['data'])):
        f1.write("\n"+str(i+1)+"、"+ data['data'][i]['conditionCnName']+"\n")
    f1.close()

