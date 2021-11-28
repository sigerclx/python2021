import pandas as pd
import random
import win32com.client
from func.init import *

from func.gushi import Gushi
speak = win32com.client.Dispatch('SAPI.SPVOICE')


# 用户选择
choice = selectbook()
gs = Gushi(choice)



def dasuan(shibody):
    shibody = shibody.replace('。', ',')
    shibody = shibody.replace('，', ',')
    shibody = shibody.replace('？', ',')

    replacestr = [' ','[',']','\'']
    for str in replacestr:
        shibody =shibody.replace(str,'')
    shibody = shibody.split(',')
    return (shibody[:-1])

def getstr(shibody):
    replacestr = ['！','\'','!','？','，','。',' ','[',']','\'']
    for str in replacestr:
        shibody =shibody.replace(str,'')
    return shibody

gushi = gs.ramdom_poem(20)
num =0
errorNum =0
for i in gushi:
    num = num + 1
    zuozhelist = gs.getfourzuozhe(i[1])
    shibody = dasuan(i[3])
    random.shuffle(shibody)
    #print(i[0],i[1],i[2],gs.getfourzuozhe(i[1]),dasuan(i[3]))
    print('第', num, '题：古诗《', i[0], '》',i[1],i[2],'\n')
    speak.Speak('第'+ str(num)+ '题'+i[0])
    #print('古诗：',i[3])
    # 显示打乱的诗句
    juzi=0
    for suan in shibody:
        juzi += 1
        print(juzi,suan)
    #print(currentAnswerStr)

    inputPress = input("请输入答案：")

    # 按句子顺序拼合全诗
    alllength = len(inputPress)
    answer =''
    for k in range(alllength):
        answer += shibody[int(inputPress[k])-1]

    if getstr(i[3]) == answer:
        print('回答正确!\n\n')
        speak.Speak('回答正确')
    else:
        errorNum += 1
        print('回答错误')
        speak.Speak('回答错误')
        print('正确答案 古诗正确顺序：',i[3],'\n\n')


print('一共',num,'道题，答对',num-errorNum,'总共得分:',(num-errorNum)/num*100)
speak.Speak('总共得分:'+str((num-errorNum)/num*100))
