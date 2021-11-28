f = lambda x :x  # lambda x : True if x else False
g = lambda x : True if x else False  # 和上面功能相同
g1 = lambda x : False if x else True # 相反过滤
print(f(0))


list_x =  [1,0,0,1,0,0,1]
k = filter(f,list_x)
print(list(k))


k = filter(g,list_x)
print(list(k))


k = filter(g1,list_x)
print(list(k))

list_x = ['a','B','H','d','o','K'] # 过滤大小写
k = filter(lambda x : True if x == x.upper() else False,list_x)
print(list(k))