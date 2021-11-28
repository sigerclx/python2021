# 针对None不能写入文件的对策

def isNone(x):
    if x is None:
        return ''
    else:
        return x

f1 = open(r'../danfanglist/111.txt', 'w', encoding='utf-8')
cnName=None
f1.write(isNone(cnName)+' 英文名：')
f1.close()