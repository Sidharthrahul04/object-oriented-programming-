class Student:
    def __init__(self,name,year):    #Object initialization   #__init__() magic method/dunder method 
        self.name=name
        self.year=year

    def __str__(self):  #human readable representation       #magic method/dunder method
        return f"{self.name} and year:{self.year}"

    def __repr__(self):  #developer representation      #representation method
        return f"({self.name} and year:{self.year})"

    def __eq__(self, other):
        return self.name==other.name


s1=Student("sulthan",2025)
s2=Student("labib",2025)
s3=Student("fakru",2022)
print(s1.year)
print(s2.year)
print(s1) #__str__()
print(s2)
print(repr(s1))
print(repr(s2))

l=[s1,s2,s3]
print(l)    #__repr__()

print(s1.year==s2.year)
