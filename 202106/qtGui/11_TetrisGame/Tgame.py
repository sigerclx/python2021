"""
PyQt5 tutorial

This is a Tetris game clone..

author: py40.com
last edited: 2017年3月
"""
import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication,QAction,qApp
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from func.tools import *


class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        # 创建一个菜单栏
        self.createMenu(self.menuBar())
        #self.resize(180, 380)
        self.resize(340, 600)
        self.center()
        self.setWindowTitle('俄罗斯方块 v1.0 敏而好学专属')
        self.show()

    def createMenu(self,menubar):
        exitAction = QAction('退出', self)
        #exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出游戏')
        exitAction.triggered.connect(self.quit)

        startAction = QAction('开始游戏', self)
        #startAction.setShortcut('Ctrl+S')
        startAction.setStatusTip('开始新游戏')
        startAction.triggered.connect(self.start)

        pauseAction = QAction('暂停', self)
        #pauseAction.setShortcut('Ctrl+P')
        pauseAction.setStatusTip('暂停游戏')
        pauseAction.triggered.connect(self.pause)
        # 添加菜单
        fileMenu = menubar.addMenu('方块大战')
        # 添加事件
        fileMenu.addAction(startAction)
        fileMenu.addAction(pauseAction)
        fileMenu.addAction(exitAction)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def start(self):
        self.tboard.writeMaxScore()
        self.tboard.initBoard()
        self.tboard.start()

    def quit(self):
        self.tboard.writeMaxScore()
        qApp.quit()

    def pause(self):
        self.tboard.pause()


class Board(QFrame):
    msg2Statusbar = pyqtSignal(str)

    BoardWidth = int(readConfig('BoardWidth'))   # 以块宽为单位
    BoardHeight = int(readConfig('BoardHeight'))  # 以块高为单位
    Speed = int(readConfig('Speed'))   # 游戏速度

    def __init__(self, parent):
        super().__init__(parent)


        self.initBoard()

    def initBoard(self):

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0

        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.curPiece = Shape()
        self.curPiece.setShape(Tetrominoe.NoShape)
        self.clearBoard()
        Tetrominoe.MaxSocre = int(readConfig('maxscore'))
        Tetrominoe.Life = int(readConfig('life'))
        Tetrominoe.LifeUp = int(readConfig('lifeup'))
        Tetrominoe.Removeline = int(readConfig('Removeline'))
        Tetrominoe.Removelineup = int(readConfig('Removelineup'))

        #self.setFocus(True)



    def shapeAt(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()
        self.setStatus()
        self.newPiece()
        self.timer.start(Board.Speed, self)



    def pause(self):

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.setStatus(" paused")

        else:
            self.timer.start(Board.Speed, self)
            self.setStatus()

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())

    def keyPressEvent(self, event):

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        elif key == Qt.Key_Down:
            #self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
            self.oneLineDown()

        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

        elif key == Qt.Key_Space:
            self.dropDown()

        elif key == Qt.Key_Plus:
            if Board.Speed >100:
                Board.Speed -= 100
                self.setStatus()
                self.timer.start(Board.Speed, self)
            elif Board.Speed >0:  # 速度不能小于0，太快了
                Board.Speed -= 5
                self.setStatus()
                self.timer.start(Board.Speed, self)



        elif key == Qt.Key_Minus:
            Board.Speed  += 100
            #print(Board.Speed)
            self.timer.start(Board.Speed, self)
            self.setStatus()

        elif key == Qt.Key_L:
            if Tetrominoe.Life>0:
                self.newPiece()
                Tetrominoe.Life -=1
                self.setStatus()


        # elif key == Qt.Key_C:   # 清除全屏，保留积分（相当于复活）
        #     self.isWaitingAfterLine = False
        #     self.board = []
        #     self.clearBoard()
        #     self.start()

        elif key == Qt.Key_X:   # 清除最底下一行，保留积分
            if Tetrominoe.Removeline > 0:
                Tetrominoe.Removeline -=1
                self.isWaitingAfterLine = False
                removeLine = [0 for i in range(0,self.BoardWidth)]
                self.board = self.board[self.BoardWidth:]+removeLine
                self.clearBoard()
                self.setStatus()


        else:
            super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)

    def clearBoard(self):

        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self):

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()

    def oneLineDown(self):

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):

        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):   # 按行检测这行是否铺满，可以消掉
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == self.BoardWidth:    # 如果铺满
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + 2**(numFullLines-1)*10
            if self.numLinesRemoved - Tetrominoe.LastRemoveLines >= Tetrominoe.LifeUp:
                Tetrominoe.Life  += 1
                Tetrominoe.LastRemoveLines = self.numLinesRemoved
            if numFullLines >= Tetrominoe.Removelineup:   # 同时消掉多行，奖励消行一次。
                Tetrominoe.Removeline  += numFullLines - Tetrominoe.Removelineup

            self.setStatus()

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()

    def newPiece(self):

        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY): # 游戏结束
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.writeMaxScore()
            self.setStatus(status=" Game over")


    def writeMaxScore(self):     # 记录游戏的最高记录
        if self.numLinesRemoved > Tetrominoe.MaxSocre:
            Tetrominoe.MaxSocre = self.numLinesRemoved
            writeConfig('MaxScore', Tetrominoe.MaxSocre)

    def tryMove(self, newPiece, newX, newY):

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    def drawSquare(self, painter, x, y, shape):

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

    def setStatus(self,status=''):
        self.msg2Statusbar.emit("得分:" + str(self.numLinesRemoved)+ "  L:"+str(Tetrominoe.Life)+ "  X:"+str(Tetrominoe.Removeline)+ "  速度:"+str(Board.Speed)+ ' 最高分:'+str(Tetrominoe.MaxSocre)+' '+status )


class Tetrominoe(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

    Life = 0       # 用户可以通过按快捷键变换下一个来的图块。
    LifeUp = 0      # 系统用以比较比上次L（按键，变换下一个）奖励（LifeUp=上次分值）以来提升了多少分
    LastRemoveLines = 0  # 系统用以比较比上次L（按键，重新发图块）奖励（LastRemoveLines=上次分值）以来提升了多少分
    MaxSocre = 0   # 最高纪录
    Removeline = 0  # 用户可以通过按快捷键消掉一行。
    Removelineup = 0 # 同时消掉行数>=Removelineup的时候，就奖励删除一行的次数


class Shape(object):
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):

        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):

        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def setRandomShape(self):
        self.setShape(random.randint(1, 7))

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def setX(self, index, x):
        self.coords[index][0] = x

    def setY(self, index, y):
        self.coords[index][1] = y

    def minX(self):

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def maxX(self):

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    def rotateLeft(self):

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotateRight(self):

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())