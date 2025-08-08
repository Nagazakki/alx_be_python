class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} is flying."

class Mammal:
    def __init__(self, name):
        self.name = name

    def run(self):
        return f"{self.name} is running."

class Bat(Bird, Mammal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        return f"{self.name} is flying like a bird."

    def run(self):
        return f"{self.name} is running like a mammal."

bat = Bat("Batista")
print(bat.fly())
print(bat.run())