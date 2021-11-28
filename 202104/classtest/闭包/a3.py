'''
闭包的实现
不使用全局变量，
'''

origin=0
def factory(pos):
    def go(step):
        nonlocal pos
        pos= pos + step
        return pos
    return go

f1=factory(origin)
print(f1(2))
print(f1(3))
print(f1(4))