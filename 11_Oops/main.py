class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")


