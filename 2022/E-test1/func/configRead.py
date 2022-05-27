#-*- coding: utf-8 -*-
import configparser
import func.tools
# 读取config.ini 获取字典返回值 eval 把字符串转为字典
def readConfig(group,key):
    cp = configparser.SafeConfigParser()
    value =""
    try:
        cp.read('configNG.ini',encoding='utf-8')
        value = eval(cp.get(group,key))
    except Exception as err:
        print("read config err!"+ str(err))
    return  value


