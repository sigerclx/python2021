'''
None 空
'''
a =''
b =False
c =[]

print(a==None)
print(b==None)
print(c==None)

print(type(None)) # 空时对象

a =[]  

if not a :  # 判断空的操作
    print('T')
else:
    print('F')

if  a is None :  # 非判断空的操作，不适合判断空
    print('T')
else:
    print('F')

