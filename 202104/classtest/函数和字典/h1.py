'''
字典和函数关联
通过key调用相应的函数
'''

def f1():
    print("f1")
def f2():
    print("f2")
func = {0:f1,1:f2}

func.get(0)()