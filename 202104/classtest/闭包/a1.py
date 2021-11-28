# 这种方式，全局变量有可能被改变,不安全

def curve_pre():
    a = 25
    def curve(x):
        # a=10 加入这句，该函数就不是闭包了
        return a * x * x
    return curve


def c1():
    pass

f = curve_pre()
print(f)
print(f(2))
print(f.__closure__)

f1 = c1()
#print(f1.__closure__)