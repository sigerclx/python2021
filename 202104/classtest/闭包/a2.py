'''
闭包的实现，用全局变量
这种方式，全局变量有可能被改变
不推荐这种方式，因为完全放弃了闭包的优点
'''
lucheng = 0
def walk():
    global  lucheng
    def go(x):
        global lucheng
        lucheng =  lucheng +x
        return lucheng
    return go

f1 = walk()
print(f1)
print(f1(3))
print(f1(3))
print(f1(4))
print(f1(30))
print(f1(300))