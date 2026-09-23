class Animal:    
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

#Parents
class Predator(Animal): 
    def hunt(self):
        print("this animal hunts")

class Prey(Animal):
    def flee(self):
            print(f"{self.name} animal flees")

#children
class Rabbit(Prey):  
    def __init__(self, name,color,age):
        super().__init__(name)
        self.colour=color
        self.age=age

    def flee(self):
        print(f"{self.name} flees")
        super().flee()

class Hawk(Predator):
    def __init__(self, name,breed,is_alive):
        super().__init__(name)
        self.breed=breed
        self.is_alive=is_alive

class Fish (Prey,Predator):   #multiple inheritance
     pass

rabbit=Rabbit("sugu","white",3)
print(rabbit.name)
rabbit.flee()

