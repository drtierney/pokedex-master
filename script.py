import json
import random

class Pokemon:
    def __init__(self, no, name, types, height, weight, abilities, stats):
        self.no = no
        self.name = name
        self.types = types
        self.height = height
        self.weight = weight
        self.abilities = abilities
        self.stats = dict(zip(stats[0], stats[1]))
        self.details = str(self).split("\n")

    def __repr__(self):
        description = "{name} is #{no} in the Pokedex!\n".format(name=self.name.title(), no=self.no)
        description += "{count} types: {types}.\n".format(count=len(self.types), types=" & ".join(self.types).capitalize()) if len(self.types) > 1 \
                        else "1 type: {types}\n".format(types=self.types[0].title())
        description += "Height is {height} & Weight is {weight}.\n".format(weight=self.weight, height=self.height)
        description += "Abilities such as {abilities}.\n".format(abilities=((", ".join(self.abilities[:-1]).title() + " & " + (self.abilities[-1]).title()).replace("-", " ")))
        description += "Base stats are - {stats}".format(stats=(', '.join(f'{key}:{value}' for key, value in self.stats.items()).upper()).replace("-", " "))
        return description

    def get_all_details(self):
        print("We think we know all the details about this Pokemon, but just can't remember the name...")
        print("\n".join(self.details[1:]))

    def get_random_details(self):
        print("We can only remember some details about this wild_pokemon...")
        print("\n".join(random.sample(self.details[1:],random.randint(2,3))))


with open("pokedex.json", "r") as json_file:
    pokedex = json.load(json_file)

print("Welcome to the world of Pokemon!")
choice = random.choice(pokedex)

wild_pokemon = Pokemon(choice.get("no"), choice.get("name"), choice.get("types"), 
                  choice.get("height"), choice.get("weight"), choice.get("abilities"), 
                  [choice.get("stats_names"), choice.get("stats_values")])
print()
print(wild_pokemon)
print()
wild_pokemon.get_all_details()
print()
wild_pokemon.get_random_details()