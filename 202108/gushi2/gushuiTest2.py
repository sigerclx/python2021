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
    replacestr = [' ','[',']','\'']
    for str in replacestr:
        shibody =shibody.replace(str,'')
    shibody = shibody.split(',')
    return (shibody[:-1])

gushi = gs.ramdom_poem(20)
num =0
errorNum =0
for i in gushi:
    num = num + 1
    zuozhelist = gs.getfourzuozhe(i[1])
    #print(i[0],i[1],i[2],gs.getfourzuozhe(i[1]),dasuan(i[3]))
    print('第', num, '题：古诗《', i[0], '》\n')
    speak.Speak('第'+ str(num)+ '题'+i[0])
    print('古诗：',i[3])
    print('诗的作者是：')
    print('   A. ', zuozhelist[0], ' B. ', zuozhelist[1], ' C. ', zuozhelist[2], ' D.', zuozhelist[3], '\n')
    #正确答案
    answer=[]
    answer.append(i[1])
    answer.append(i[2])
    currentAnswerNum = zuozhelist.index(answer)
    if currentAnswerNum == 0:
        currentAnswerStr = 'A'
    if currentAnswerNum == 1:
        currentAnswerStr = 'B'
    if currentAnswerNum == 2:
        currentAnswerStr = 'C'
    if currentAnswerNum == 3:
        currentAnswerStr = 'D'

    #print(currentAnswerStr)

    inputPress = input("请输入答案：")
    if inputPress.upper()==currentAnswerStr.upper():
        print('回答正确!\n\n')
        speak.Speak('回答正确')
    else:
        errorNum += 1
        print('回答错误')
        speak.Speak('回答错误')
        print('正确答案 作者是：',answer,'\n\n')


print('一共',num,'道题，答对',num-errorNum,'总共得分:',(num-errorNum)/num*100)
