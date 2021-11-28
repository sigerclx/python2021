import random
import easygui as g
import sys  # 系统模块

#窗口演示

# 循环
for i in range(1, 6):
    a = random.randint(0, 99)
    ab = g.enterbox(msg='第' + str(i) + '轮 第1次 ：请猜出一个（1~100的数）', title="猜数游戏")
    for n in range(2, 10):
        ab = int(ab)

        if n >= 7:
            g.buttonbox(msg='都猜了这么多次都没猜到，太遗憾了,游戏结束', title="猜数游戏", choices=('退出游戏', '继续游戏'))
            if fanhui == '继续游戏':
                break
            else:
                sys.exit(0)

        if ab == a:
            fanhui = g.buttonbox(msg='恭喜你，猜对了！', title="猜数游戏", choices=('退出游戏', '继续游戏'))
            if fanhui == '继续游戏':
                break
            else:
                sys.exit(0)

        lun = '第' + str(i) + '轮 第' + str(n) + '次 : '

        if ab > a:
            ab = g.enterbox(msg=lun + '你的数大了', title="猜数游戏")
            ab = int(ab)

        if ab < a:
            ab = g.enterbox(msg=lun + '你的数小了', title="猜数游戏")

