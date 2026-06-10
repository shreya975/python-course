class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")