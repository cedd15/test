class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hi, my name is " + self.name)
        print("I am " + str(self.age)) # can't concatenate int to string hence the use of str()

p1 = Person("John", 36)

p1.intro()

