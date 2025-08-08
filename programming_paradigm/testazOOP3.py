class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says Woof! Woof!")

print("=== Creating Animal ===")
animal = Animal("Generic Animal")
animal.eat()
animal.sleep()

print("\n=== Creating Dog ===")
dog = Dog("Buddy", "Golden Retriever")
dog.eat()
dog.sleep()
dog.bark()

