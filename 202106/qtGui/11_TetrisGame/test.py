import configparser


def writeConfig(key,value ,group='Tetris'):
    cp = configparser.ConfigParser()
    cp.read('config.ini',encoding='utf-8')
    #cp.add_section(group)
    cp.set(group, key, str(value))
    cp.write(open('config.ini', "r+",encoding='utf-8'))


writeConfig('maxscore',2)