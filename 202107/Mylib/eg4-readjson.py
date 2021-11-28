from func.getjson import getJson

# 读取config.json里的key 'First-level-domain'
txt = getJson('First-level-domain')
print(txt)
txt = getJson('Line')
print(txt)
mylist= eval(txt)
print(mylist[0])
