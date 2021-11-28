import time
from func.tools import recordLog,writeerrbook
import win32com.client

class Student:
    spendMinute = 0
    spendSecond = 0
    startTime = ''
    endTime = ''
    alarmTime = 0
    question = 0
    wronglist = []

class Exam(object):
    def __init__(self):
        self.student = Student()
        self.questionnum = 0
        self.questions = []
        self.answers = []
        self.answerpinyin =[]
        self.title = ''
        self.speak = win32com.client.Dispatch('SAPI.SPVOICE')

    def setparam(self,title,questionnum,questions,answers):
        self.questionnum = questionnum
        self.questions = answers
        self.answers = answers
        self.title = title


    def printtitle(self):
        print('\n'+self.title ,end=" ")

    def replaceall(self,txt):
        fuhao =['\"',",","，","。"," ","　"]
        for i in fuhao:
            txt = txt.replace(i,'')
        return txt

    def startTest(self):
        self.printtitle()
        if self.questionnum> len(self.questions):
            self.questionnum = len(self.questions)
        print('-- 共有',self.questionnum,'道题')
        for i in  range(self.questionnum):

            print('\n第',i+1,'题：')
            self.speak.Speak("第" + str(i+1) + "题")
            print('题目：'+self.questions[i])
            self.student.question +=1
            key = input('\n请输入答案：')
            key  = self.replaceall(key)
            answer  = self.replaceall(self.answers[i])
            if key.lower()==answer:
                print('回答正确 √',' 拼音：',self.answerpinyin[i],'\n')
                self.speak.Speak('回答正确')
            else:

                print('回答错误！ × \n')
                self.speak.Speak('回答错误')
                print('正确答案：',self.answers[i],' 拼音：',self.answerpinyin[i],'\n')
                self.student.wronglist.append(self.answers[i])
        self.showscore()

    def showscore(self):
        score = int((1-len(self.student.wronglist) / self.student.question) * 100)
        print('\n得分：',score)
        self.speak.Speak('最后得分' + str(score) + '分')
        if score<100:
            print('你答错了下面的题目：')
            print(self.student.wronglist)
            recordLog(str(self.student.wronglist))
            for i in (self.student.wronglist):
                writeerrbook(i)
            self.speak.Speak('你答错了下面的题目')
