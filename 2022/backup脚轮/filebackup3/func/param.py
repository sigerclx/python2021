
def Param_init():  # 初始化
    global _global_dict
    _global_dict = {}

def Set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def Get_value(key, defValue=None):
    #""" 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        return ""





