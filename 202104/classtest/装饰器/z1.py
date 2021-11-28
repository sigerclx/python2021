import time
def decorator(func):
    def wrapper(*args,**kw):  # 适应各种参数模式
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print(func_name)

@decorator
def f2(func_name1,func_name2):
    print(func_name1,func_name2)

@decorator
def f3(func_name1,func_name2,**kw):
    print(func_name1,func_name2)
    print(kw)

f1("beijing")
f2("nanjing",'shanghai')
f3("nanjing",'shanghai',k=1,f=2,r="36c")