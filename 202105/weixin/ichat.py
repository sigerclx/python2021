# # hotReload(热加载),短时间内不需要再次扫码登陆
# itchat.auto_login(hotReload=True)
# # 将“Hello FileHelper”发送给微信的文件助手
# itchat.send(u"Hello FileHelper", "filehelper")

# -*- coding:utf-8 -*-
__author__ = "MuT6 Sch01aR"
import itchat
def get_friends():
  friends = itchat.get_friends(update=True) #获取微信好友列表，如果设置update=True将从服务器刷新列表
  for i in friends:
    print(i)
def main():
  itchat.auto_login(hotReload=True) #登录，会下载二维码给手机扫描登录，hotReload设置为True表示以后自动登录
  get_friends()
  itchat.run() #让itchat一直运行
if __name__ == "__main__":
  main()