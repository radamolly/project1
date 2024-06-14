class Animal:
    name = "no name"
    def __init__(self,name = None):
        self.name = name
    def can(self, ability):
        print("Animal can", ability)

class Dog(Animal):
    def speak(self):
        print("Woof!")

animal = Animal()
animal.can("breathe")

dog = Dog()
dog.speak()
dog.can("breathe")
print("")