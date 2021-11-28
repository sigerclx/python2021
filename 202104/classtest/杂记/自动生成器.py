n = [ i for i in range(1,100)]
print(n)


n = ( i for i in range(1,100))
print(n)
print(next(n))
print(next(n))
print(next(n))

# 自动生成器
def gen(max):
    n = 0
    while n<max:
        n +=1
        yield n

g = gen(100)
print(g)
print(next(g))
print(next(g))
