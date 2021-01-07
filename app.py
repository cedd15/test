class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hi, my name is " + self.name)
        print("I am " + str(self.age))  # can't concatenate int to string hence the use of str()


p1 = Person("John", 36)

p1.intro()


class Student(Person):
    def __init__(self, name, age,city):
        super().__init__(name, age)
        self.city = city

    def comp(self):
        print("Hi, my name is " + self.name, "\nI am " + str(self.age), "\nI live in " + self.city)




x = Student("Mike", 20, "Manila")
x.comp()


# another test