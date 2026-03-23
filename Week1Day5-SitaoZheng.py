# Question 11
class Mixin:
    def __init__(self):
        print(self.__class__.__name__)
    def is_animal(self):
        return isinstance(self, Animal)
    
class Animal(Mixin):
    pass
    
class Cat(Animal):
    pass

class Car(Mixin):
    pass

def mixin_main():
    a = Animal() # print Animal
    c = Cat() # print Cat
    car = Car() # print Car

    print(c.is_animal()) # True
    print(car.is_animal()) # False

