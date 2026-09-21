#grand parent
class Animal:    
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

#parents
class Predator(Animal): 
    def hunt(self):
        print("this animal hunts")

class Prey(Animal):
    def flee(self):
            print("this animal flees")

#children
class Rabbit(Prey):  
     pass

class Hawk(Predator):
     pass

class Fish (Prey,Predator):   #multiple inheritance
     pass

rabbit=Rabbit("muhammad")
rabbit.flee()
rabbit.eat()
rabbit.sleep()
hawk=Hawk("sulaiman")
hawk.hunt()
fish=Fish("raghav")
fish.hunt()
fish.flee()

    
