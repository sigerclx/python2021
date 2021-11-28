from dataclasses import dataclass
class Student():
    def __init__(self,name,age,school_name):
        self.name = name
        self.age = age
        self.school_name = school_name

    def test(self):
        print(self.name)

student1 = Student('Jacky',34,'hangzhoulu')
student1.test()

'''
用装饰器替代构造函数
'''
@dataclass
class Student1():
    name:str
    age:int
    school_name:str

    def test(self):
        print(self.name)

student1 = Student('Jacky',34,'hangzhoulu')
student1.test()