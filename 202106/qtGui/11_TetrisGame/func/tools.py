import configparser


def readConfig(key,group='Tetris'):
    cp = configparser.ConfigParser()
    value =""
    try:
        cp.read('config.ini',encoding='utf-8')
        value = eval(cp.get(group,key))
    except Exception as err:
        print("read config err!"+ str(err))
    return  value

def writeConfig(key,value ,group='Tetris'):
    cp = configparser.ConfigParser()
    cp.read('config.ini',encoding='utf-8')
    #cp.add_section(group)
    cp.set(group, key, str(value))
    cp.write(open('config.ini', "r+",encoding='utf-8'))


