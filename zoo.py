class Animal:
    def __init__(self, species, age, name):
        # write the method
        self.species = species
        self.age = age
        self.name = name

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

# Compelte the class
class Bird(Animal):
    def __init__(self, species, age, name, can_fly):
        # complete the method
        super().__init__(species, age, name)
        if can_fly:
            self.can_fly = 'Yes'
        else:
            self.can_fly = 'No'

    def __str__(self):
        # complete the method
        return super().__str__() + f", Can Fly: {self.can_fly}"

class Zoo:
    def __init__(self):
        # complete the method
        self.animals = []

    def add_animal(self, animal):
        # complete the method
        self.animals.append(animal)

    def list_animals(self):
        # complete the method
        for animal in self.animals:
            print(animal, end="\n\n")
    
    def __str__(self, animal):
        details = f"Name: {animal.name}, Species: {animal.species}, Age: {animal.age}"
        if isinstance(animal, Bird):
            details += f", Can Fly:{animal.can_fly}"
        return details


animal1 = Animal("Northern giraffe", 3, "Sharma")
animal2 = Animal("Masai giraffe", 0.5, "Oboli Popo")
bird1 = Bird("Emperor penguin", 1, "Layla", False)
animal3 = Animal("Royal Mysore giraffe", 5.2, "Kumaraswamy")
bird2 = Bird("Golden eagle", 7, "Sheeba", True)
bird3 = Bird("Golden eagle", 7, "Bheesham", True)


chamarajendrawodeyarzoo = Zoo()

chamarajendrawodeyarzoo.add_animal(animal1)
chamarajendrawodeyarzoo.add_animal(bird1)
chamarajendrawodeyarzoo.add_animal(animal2)
chamarajendrawodeyarzoo.add_animal(bird3)
chamarajendrawodeyarzoo.add_animal(bird2)
chamarajendrawodeyarzoo.add_animal(animal3)

chamarajendrawodeyarzoo.list_animals()