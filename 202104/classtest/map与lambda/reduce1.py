from functools import reduce
list_x = [1,2,3,4,5]

# reduce 连续运算，x的取值为 x+y后 赋值到x
k  = reduce(lambda x,y: x+y,list_x)
print(k)
print(type(k))

