import time
import playsound
import pprint
import sys
import win32com.client
from func.globalValue import *
import func.configRead

class student:
        spendMinute=0
        spendSecond=0
        startTime=''
        endTime=''
        alarmTime=0
        question=0
        wronglist=[]

kid = student()
speak = win32com.client.Dispatch('SAPI.SPVOICE')

def quitgame(words):
    global kid
    global speak
    kid.endTime= func.tools.get_hour()
    kid.wronglist =list(set(kid.wronglist))  #去除重复单词
    wrongTime=len(kid.wronglist)
    rightTime=kid.question-wrongTime
    print(kid.question)
    print('得分 = '+str(round((rightTime)/(kid.question) *100)))
    print('\n总共出题：'+str(kid.question))
    print('答对题目：'+str(rightTime))
    print('答错题目：'+str(wrongTime))
    print('提示次数：'+str(kid.alarmTime))
    kid.spendMinute=round(func.tools.time_cmp(kid.endTime,kid.startTime) /60,0)
    kid.spendSecond=func.tools.time_cmp(kid.endTime,kid.startTime) % 60

    print('用时：'+str(kid.spendMinute)+'分'+str(kid.spendSecond)+'秒')
    
    speak.Speak('你总共得分：'+str(round(rightTime/(kid.question) *100))+'分')
    
    if len(kid.wronglist)>0:
        print('\n以下是答错的单词')
        speak.Speak('你答错了下面的单词：')
        pprint.pprint(kid.wronglist)
        rewrite(kid.wronglist,words)
        
    else:
        if (kid.question-1)>0:
            print('恭喜你全部正确！\n')
            speak.Speak('恭喜你全部正确！')
        
    func.tools.recordLog('得分 = '+str(round((rightTime-1)/(kid.question-1) *100,0)))
    func.tools.recordLog('总共出题：'+str(kid.question-1))
    func.tools.recordLog('答对题目：'+str(rightTime-1))
    func.tools.recordLog('答错题目：'+str(wrongTime))
    func.tools.recordLog('提示次数：'+str(kid.alarmTime))
    func.tools.recordLog('用时：'+str(kid.spendMinute)+'分'+str(kid.spendSecond)+'秒')
    func.tools.recordLog('以下是答错的单词')
    func.tools.recordLog(str(kid.wronglist))
    print('\n练习完毕，请输入回车退出')
    while len(input())<1:
        sys.exit(0)

def rewrite(wronglist,words):
    print("亲爱的，你一共做错了"+str(len(wronglist))+'个单词')
    
    practice= Get_value('practice')
    print('以下开始每一个做错的单词练习输入'+str(practice)+'遍\n')

    for i in wronglist:
        print(i)
        #speak.Speak(i.lower())
        for j in words:
            if i==j['word']:
                print('单词含义：')
                print(j['mean'])
                #playsound.playsound(j['mp3'], True)
                break
        m=0
        while m<practice:
            print('\n请输入正确的单词：',end='')
            playsound.playsound(j['mp3'], True)
            keyinput=input()
            if keyinput.strip().lower()!=i.lower():
               print("输入错误！\n")
            else:
               print("输入正确！\n")
               m=m+1
        print('\n')
            
        

def listenWrite(words,questionnum=10):
    global kid
    global speak
    kid.startTime= func.tools.get_hour()
    
    if questionnum>len(words):
        func.tools.recordLog("出题数目大于单词总量")
        print("出题数目大于单词总量,将使用最大单词量")
        questionnum=len(words)
    words=words[:questionnum]
    print('英语小测验  共' + str(questionnum) + '题')
    print('答题时请注意：')
    print(r'1、 按 回车 键可以重新听单词发音')
    print(r'2、 按 s回车 键可以看到单词的拼写')
    print('')
    print('')

    inputPress=''
    func.tools.recordLog('')
    func.tools.recordLog('全新答题开始：')
    for i in words:
        kid.question=kid.question+1
        while inputPress!='Q':
            
            print("\n第"+str(kid.question)+"题，请根据发音输入答案：",end='')
            speak.Speak("第"+str(kid.question)+"题")
            #time.sleep(1)
            try:
                playsound.playsound(i['mp3'], True)
            except Exception as err:
                print(i['mp3'])
                func.tools.recordLog(str(err))
                func.tools.recordLog("打开MP3出错")
                print("打开MP3出错")
                sys.exit(0)
            inputPress=input()
            inputPress=inputPress.strip().upper()
            if inputPress==i['word'].upper():
                print('回答正确!')
                if Get_value('dispmean').lower()=='yes':
                    print("该单词的含义：" + i['mean'])
                break
            elif inputPress=='':
                time.sleep(1)
                continue
            elif inputPress=='S':
                kid.alarmTime=kid.alarmTime+1
                print("正确的单词："+i['word'])
                kid.wronglist.append(i['word'])
                time.sleep(1)
                continue
            elif inputPress=='Q':
                kid.wronglist.append(i['word'])
                quitgame(words)
            else:
                func.tools.recordLog("第"+str(kid.question)+"题 "+i['word']+' 回答错误：'+inputPress)
                print(inputPress.lower()+'是错误的 ! 请再听一次 ',end="")
                print('按 回车=重新听单词发音 , 按 s回车= 查看单词的拼写 , q回车 = 退出')
                
                kid.wronglist.append(i['word'])
                
                print("该单词的含义："+i['mean'])
    quitgame(words)
