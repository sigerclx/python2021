import configparser
config = configparser.ConfigParser() # 类实例化

# 定义文件路径
path = r'danfang-list.ini'

# 第一种读取ini文件方式,通过read方法
config.read(path)
#alue = config['chashu']['url']
value = config.get('chashu','url')
print('第一种方法读取到的值：',value)

str= value.split('\n')

i=0
for s in str:
    i=i+1
    print(i,s)

print(len(str))

value = config.items('chashu')

print(value)