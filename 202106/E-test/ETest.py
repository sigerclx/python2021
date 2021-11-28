#! python3
# P148 古诗根据gushi.py随机出题
# 要求：出题从古诗名称中随机选，不能重复，4个答案不能重复，必须含正确答案

import os
import pprint
import gushi
import random
import copy

#print(gushi.gushi)
#print(gushi.gushi['乡村四月'])
#print(gushi.gushi['乡村四月'][1])
#myNumber = random.randint(1,100)


questionCount = 10  #出题数量
questionStr=list(gushi.gushi.keys())  #取得古诗名字
answerStr=list(gushi.gushi.values())  #取得古诗作者和第一句

zuozhe=[]  #作者

for name in answerStr:   #取得作者名字的列表
    zuozhe.append(name[1])

zuozhe =list(set(zuozhe))  #作者列表去重

zuozheTMP = copy.copy(zuozhe)

random.shuffle(questionStr)  #随机排列questionStr 列表


errorQuestions=[]
errorNum=0

for i in range(questionCount):
    zuozheTMP= copy.copy(zuozhe)
    zuozheTMP.remove(gushi.gushi[questionStr[i]][1])   # 先去掉当前古诗的作者
    
    choice = []  # 存储4个选择答案
    for j in range(3):  #除了正确答案外，还有三个备选答案
        daan=zuozheTMP[random.randint(0,len(zuozheTMP)-1)]
        choice.append(daan)
        zuozheTMP.remove(daan)
    choice.append(gushi.gushi[questionStr[i]][1])
    
    random.shuffle(choice)  #随机排列答案，把四个作者随机排列 列表
    print('第',str((i+1)).rjust(2,'0'),'题：古诗《',questionStr[i],'》的第一句：',gushi.gushi[questionStr[i]][0],' 诗的作者是：')
    print('   A. ',choice[0],' B. ',choice[1],' C. ',choice[2],' D.',choice[3],'\n')
    currentAnswerNum=choice.index(gushi.gushi[questionStr[i]][1])
    if currentAnswerNum==0:
        currentAnswerStr = 'A'
    if currentAnswerNum==1:
        currentAnswerStr = 'B'
    if currentAnswerNum==2:
        currentAnswerStr = 'C'
    if currentAnswerNum==3:
        currentAnswerStr = 'D'
        
    inputPress=input("请输入答案：")
    
    if inputPress.upper()==currentAnswerStr.upper():
        print('回答正确!\n')
    else:
        errorNum += 1
        print('回答错误')
        print('正确答案 作者是：',gushi.gushi[questionStr[i]][1],'\n\n')
        errorQuestions.append('《'+questionStr[i]+'》 的作者是：'+gushi.gushi[questionStr[i]][1])
    del(choice)

print('您一共回答了',questionCount,'道题，其中',errorNum,'道题错误! 得分：',round((1-errorNum/questionCount)*100,2),'\n')
if errorNum>0:
    print('以下是您答错题的正确答案：')
    for str1 in errorQuestions:
        print(str1)

input()
