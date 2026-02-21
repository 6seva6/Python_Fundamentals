class Zoo:
    total_animal = 0
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.names = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.total_animal += 1

    def get_info(self, species):
        if species == "mammal":
            species = "Mammals"
            self.names = self.mammals
        elif species == "fish":
            species = "Fishes"
            self.names = self.fishes
        elif species == "bird":
            species = "Birds"
            self.names = self.birds
        return f"{species.capitalize()} in {self.zoo_name}: {', ' .join(self.names)} \nTotal animals: {Zoo.total_animal}"


name = input()
animal_count = int(input())
my_zoo = Zoo(name)

for i in range(animal_count):
    input_species = input().split()
    species, name = input_species
    my_zoo.add_animal(species, name)

info = input()

print(my_zoo.get_info(info))