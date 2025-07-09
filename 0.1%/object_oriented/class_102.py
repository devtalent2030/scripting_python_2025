


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"hello, my name is {self.name} and I am a {self.species}.")
        

# instance of the class





dog = Pet("buddy", "Dog")


print(dog)
print(dog.name)
print(dog.species)

dog.introduce()
