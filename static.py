#static method

class Math:
    def __init__(self,digit):
        self.digit=digit

    def square(self):  #instance method
        return self.digit**2

    @staticmethod      #it doesnt belong to any specific object, it belongs to the class and is accesible using class.method().
    def add(a,b):
        return a+b


obj1=Math(3)
print(obj1.square())
print(Math.add(1,2))




