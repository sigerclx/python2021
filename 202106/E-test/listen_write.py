import time
import playsound
import pprint
import sys
import win32com.client
import tools
import configRead

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
    kid.endTime= tools.get_hour()
    kid.wronglist =list(set(kid.wronglist))  #去除重复单词
    wrongTime=len(kid.wronglist)
    rightTime=kid.question-wrongTime
    print('得分 = '+str(round((rightTime-1)/(kid.question-1) *100,0)))
    print('\n总共出题：'+str(kid.question-1))
    print('答对题目：'+str(rightTime-1))
    print('答错题目：'+str(wrongTime))
    print('提示次数：'+str(kid.alarmTime))
    kid.spendMinute=round(tools.time_cmp(kid.endTime,kid.startTime) /60,0)
    kid.spendSecond=tools.time_cmp(kid.endTime,kid.startTime) % 60

    print('用时：'+str(kid.spendMinute)+'分'+str(kid.spendSecond)+'秒')
    
    speak.Speak('你总共得分：'+str(round((rightTime-1)/(kid.question-1) *100,0))+'分')
    
    if len(kid.wronglist)>0:
        print('\n以下是答错的单词')
        speak.Speak('你答错了下面的单词：')
        pprint.pprint(kid.wronglist)
        time.sleep(5)
        print('\n')
        rewrite(kid.wronglist,words)
        
    else:
        if (kid.question-1)>0:
            print('恭喜你全部正确！\n')
            speak.Speak('恭喜你全部正确！')
        
    tools.recordLog('得分 = '+str(round((rightTime-1)/(kid.question-1) *100,0)))
    tools.recordLog('总共出题：'+str(kid.question-1))
    tools.recordLog('答对题目：'+str(rightTime-1))
    tools.recordLog('答错题目：'+str(wrongTime))
    tools.recordLog('提示次数：'+str(kid.alarmTime))
    tools.recordLog('用时：'+str(kid.spendMinute)+'分'+str(kid.spendSecond)+'秒')
    tools.recordLog('以下是答错的单词')
    tools.recordLog(str(kid.wronglist))
    print('\n练习完毕，请输入回车退出')
    while len(input())<1:
        sys.exit(0)

def rewrite(wronglist,words):
    print("亲爱的，你一共做错了"+str(len(wronglist))+'个单词\n')
    
    practice= int(configRead.readConfig('listenwrite','practice'))
    print('以下开始每一个做错的单词练习输入'+str(practice)+'遍\n\n')

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
    kid.startTime= tools.get_hour()
    
    if questionnum>len(words):
        tools.recordLog("出题数目大于单词总量")
        print("出题数目大于单词总量,将使用最大单词量")

    
    inputPress=''
    tools.recordLog('')
    tools.recordLog('全新答题开始：')
    for i in words:
        kid.question=kid.question+1
        if kid.question>questionnum:
            quitgame(words)
        while inputPress!='Q':
            
            print("\n第"+str(kid.question)+"题，请根据发音输入答案：",end='')
            speak.Speak("第"+str(kid.question)+"题")
            #time.sleep(1)
            try:
                playsound.playsound(i['mp3'], True)
            except Exception as err:
                print(i['mp3'])
                tools.recordLog(str(err))
                tools.recordLog("打开MP3出错")
                print("打开MP3出错")
                sys.exit(0)
            inputPress=input()
            inputPress=inputPress.strip().upper()
            if inputPress==i['word'].upper():
                print('回答正确!')
                break
            elif inputPress=='A' or inputPress=='':
                time.sleep(1)
                continue
            elif inputPress=='S':
                kid.alarmTime=kid.alarmTime+1
                print("正确的单词："+i['word'])
                kid.wronglist.append(i['word'])
                time.sleep(1)
                continue
            elif inputPress=='Q':
                quitgame(words)
            else:
                tools.recordLog("第"+str(kid.question)+"题 "+i['word']+' 回答错误：'+inputPress)
                print(inputPress.lower()+'是错误的 ! 请再听一次')
                
                kid.wronglist.append(i['word'])
                
                print("该单词的含义："+i['mean'])
    quitgame(words)
