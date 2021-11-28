#-*- coding: utf-8 -*-
import configparser
import tools
# 读取config.ini 获取字典返回值 eval 把字符串转为字典
def readConfig(group,key):
    cp = configparser.SafeConfigParser()
    value =""
    try:
        cp.read('config.ini',encoding='utf-8')
        value = eval(cp.get(group,key))
    except Exception as err:
        tools.recordLog("read config err!"+ str(err))
        print("read config err!"+ str(err))
    return  value


