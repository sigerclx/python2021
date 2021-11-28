class Test():
    pass

test = Test()
print(id(test))
print(type(test))
if test:
    print('S')

#print(len(test))

# 两个特殊的方法 ，让函数返回0，或false ，系统认为该实例化的函数还是为空
# 有内置的 __len__，该函数才能求长度
class Test1():
    def __len__(self):
        return 0
    def __bool__(self):
        return False

test = Test1()
if test:
    print('S')
else:
    print('F')

print(len(test))