class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        print(f"My name is {self.name} and I study {self.course}.")

s1 = Student("Ranjini" , "Python Automation")
s1.introduce()