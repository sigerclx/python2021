import func.tools
import datetime
import win32com.client
speak = win32com.client.Dispatch('SAPI.SPVOICE')

class Question():
    def __init__(self):
        self.keyin=''

    def disp(self):
        self.t1 = datetime.datetime.now()
        speak.Speak('按回车开始')
        self.keyin = input("按回车开始")
        self.keyin =input(self.title)

        self.t2 = datetime.datetime.now()
        self.panduan()

    def panduan(self):
        if self.keyin.lower() == self.answer:
            print('回答正确')
            speak.Speak('回答正确')
        else:
            print('回答错误')
            speak.Speak('回答错误')
        print("总共耗时：", func.tools.get_seconds(self.t1, self.t2))
        speak.Speak("总共耗时："+ str(func.tools.get_seconds(self.t1, self.t2))+'秒')

    def gettime(self):
        pass