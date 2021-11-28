def init():
    global _global_dict
    _global_dict = {}

def setvalue(name, value):
    _global_dict[name] = value

def getvalue(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
