#class method
class School:
    name="XYZ School"
    n=0
    gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        School.n+=1
        School.gpa+=gpa

    @classmethod
    def total(cls):
        return School.n
    
    @classmethod
    def avg(cls):
        return School.gpa/School.n

    @classmethod
    def change(cls,school):
        School.name=school

obj1=School("boubakkar",7.8)
obj2=School("abdul",6.8)
print(School.avg())
print(School.total())
School.change("ABC School")
print(School.name)



    
