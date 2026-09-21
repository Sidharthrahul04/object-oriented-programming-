class Animal: #class
    n=0  #class variable
    def __init__(self,name): #constructore
        self.name=name #instance variable
        self.is_alive=True
        Animal.n=Animal.n+1

    def sleep(self):
        print(f"{self.name} is sleeping")

    def sound(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def sound(self):
        print(f"sound of {self.name} is meow")

dog = Animal("aboubakkar")
print(dog.name)
dog.sound()
print(dog.is_alive)
cat=Cat("tommy")
cat.sound()
print(Animal.n)
    
