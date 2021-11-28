import time
def decorator(func):
    def wapper():
        print(time.time())
        func()
    return wapper

def f0():
    '''
    没有装饰器的文档
    :return:
    '''
    print('f0')
    print(f0.__name__)
    print(f0.__doc__)
f0()

@decorator
def f1():
    '''
    加装饰器后，函数的名字就改变了，同时 原函数的 doc文档也无法访问
    :return:
    '''
    print('f1')
    print('f1的函数名字:',f1.__name__)
    print('f1函数的文档doc：',f1.__doc__)
f1()

@decorator
def f2():
    print('f2')
    print(f2.__name__)

f2()

print("--------------还原原有函数名称和doc----------------------")

from functools import wraps
def decorator1(func):
    @wraps(func)
    def wapper():
        print(time.time())
        func()
    return wapper

@decorator1
def f1():
    '''
    加装饰器后，函数的名字就改变了，同时 原函数的 doc文档也无法访问
    :return:
    '''
    print('f1')
    print('f1的函数名字:',f1.__name__)
    print('f1函数的文档doc：',f1.__doc__)
f1()