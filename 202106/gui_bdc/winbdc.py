import sys
from PyQt5.QtWidgets import (QWidget, QLabel,QLineEdit,QMainWindow,
    QTextEdit,QComboBox,QPushButton, QHBoxLayout,QVBoxLayout,QApplication)
from func.init import *
from func.globalValue import *
from func.listen_write import *

class BdcWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        bookdict = getEbooknames()
        self.combo = QComboBox(self)
        for v in bookdict.values():
            self.combo.addItem(v)
        self.combo.move(80, 10)
        self.combo.activated[str].connect(self.onActivated)
        self.selectlbl = QLabel('选择书目:', self)
        self.selectlbl.move(10,15)
        self.tiplbl = QLabel('题号:', self)
        self.tiplbl.move(10, 50)
        self.titleEdit = QLineEdit("", self)
        self.titleEdit.move(80,45)
        self.tipEdit = QTextEdit("", self)
        self.tipEdit.move(80, 80)
        self.startButton = QPushButton("开始", self)
        self.startButton.move(350,10)
        self.startButton.clicked.connect(self.onStart)
        self.submitButton = QPushButton("重听", self)
        self.submitButton.move(350, 45)
        self.submitButton = QPushButton("提示", self)
        self.submitButton.move(430, 45)
        self.submitButton = QPushButton("提交", self)
        self.submitButton.move(510, 45)
        #self.statusBar().showMessage('Ready')

        self.setGeometry(300, 100, 600, 400)
        self.setWindowTitle('英语背单词')
        self.show()

    def onActivated(self, text):
        Set_value('book',text)
        print(Get_value('book'))
        # 获取书单词，短语，句子list
        self.book_words, self.book_phrases, self.book_sentences = getbookcontent(Get_value('book'))
        #print(self.book_words)
        self.words = getTestQuestions(self.book_words)
        print(self.words)

    def onStart(self):
        listenWrite(self,self.words, Get_value('questionnum'))
        Set_value('conn', None)

    def dispMean(self, text):
        self.tipEdit.setText(text)

    def dispStatus(self, text):
        pass
        #self.statusBar().showMessage(text)

if __name__ == '__main__':
    # 预读参数
    getConfig()
    # 初始化数据库
    db_init()
    app = QApplication(sys.argv)
    ex = BdcWindow()
    #ex.dispStatus('dddd1')


    sys.exit(app.exec_())