class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, Age: {self.age}")

    def __del__(self):
        print(f"Bye {self.name}!")

person = Person("Johnte Wanyama", 35)

del person
