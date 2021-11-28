# 列表推导式
# 集合推导式

a = [1,2,3,4,5,6,7,8]
b = [i**2 for i in a]

print(b)

# 按条件筛选a，可读性弱些
b = [i**2 for i in a if i>4]

print(b)

# 集合、字典、元组也可以被推导
a = (1,2,3,4,5,6,7,8)
b = {1,2,3,4,5,6,7,8}
c = {"a":1,"b":8,"c":6}

for k in c:
    print(c[k])

a1 = [i**2 for i in a if i>4]
b1 = {i**2 for i in b if i>4}
c1 = {c[i]**2 for i in c if c[i]>4}

print(a1,b1)
print(c1)