# used to give an object its initial values

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hi, {self.name}, and I'm {self.age} years old.")

p1 = Person("Sreeranjinj", 26)
p1.say_hello()
