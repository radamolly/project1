class Person:
    school = "Montfort"
    def __init__(self, name, age, school=None):
        self.name = name
        self.age = age
        if(school != None):
            self.school = school

    def greet(self):
        print("Hello, My name is", self.name)

    def show_age(self):
        print("My age is", self.age)

    def show_school(self):
        print("I study at", self.school)

person = Person("John", 36)
person.greet()
person.show_age()
person.show_school()

person2 = Person("Mali", 15,"Ban kok")
person2.greet()
person2.show_age()
person2.show_school()