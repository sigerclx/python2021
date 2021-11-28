# 微信好友性别及位置信息
# 这里要注意：不管你是为了Python就业还是兴趣爱好，记住：项目开发经验永远是核心，如果你没有2020最新python入门到高级实战视频教程，可以去小编的Python交流.裙 ：七衣衣九七七巴而五（数字的谐音）转换下可以找到了，里面很多新python教程项目，还可以跟老司机交流讨教！

#导入模块
from wxpy import Bot

# '''
# 微信机器人登录有3种模式，
# (1)极简模式:robot = Bot()
# (2)终端模式:robot = Bot(console_qr=True)
# (3)缓存模式(可保持登录状态):robot = Bot(cache_path=True)
# '''
#初始化机器人，选择缓存模式（扫码）登录
#robot = Bot(cache_path=True)
robot = Bot()
#获取好友信息
robot.chats()
#robot.mps()#获取微信公众号信息

#获取好友的统计信息
Friends = robot.friends()
print(Friends.stats_text())