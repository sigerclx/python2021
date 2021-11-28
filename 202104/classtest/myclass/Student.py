from myclass.Humen import Humen
class Student(Humen):
    def __init__(self,name,age,school):
        self.school = school
        super(Student,self).__init__(name,age)

    def get_school(self):
        print(self.school)