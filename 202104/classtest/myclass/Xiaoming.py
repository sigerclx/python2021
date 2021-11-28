from myclass.Student import Student
class Xiaoming(Student):
    def __init__(self,parent):
        self.parent = parent

    def get_parent(self):
        print(self.parent)