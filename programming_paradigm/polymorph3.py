class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} says woof!"

    def make_sound(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} says meow!"
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says meow!"

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} says chirp!"

def let_them_speak(animals):
    for animal in animals:
        print(animal.make_sound())

dog = Dog("Bosko")
cat = Cat("Whiskers")
bird = Bird("Tweety")

animal_list = [dog, cat, bird]

let_them_speak(animal_list)