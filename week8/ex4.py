class Animal:
    def __init__(self, name):
        self.__name = name
    
    def breathe(self):
        pass

    def get_name(self):
        return self.__name

class Fish(Animal):
    def breathe(self):
        return "fin"
    
class Cat(Animal):
    def breathe(self):
        return "Nose"
    
fish = Fish("George")
print(fish.get_name(), "Fish use", fish.breathe(), "to breathe")
print(fish.breathe())

cat = Cat("Som")
print(cat.get_name(), "Cat use", cat.breathe(), "to breathe")
print(cat.breathe())

    
