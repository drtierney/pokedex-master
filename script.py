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
        self.comparison = ["_" for _ in range(len(name))]


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
        print("We can only remember some details about this Pokemon...")
        print("\n".join(random.sample(self.details[1:],random.randint(2,3))))

    
    def update_comparison(self, guess):
        for i in range(min(len(self.name), len(guess))):
            if guess[i] == self.name[i] and self.comparison[i] == "_":
                self.comparison[i] = guess[i]


with open("pokedex.json", "r") as json_file:
    pokedex = json.load(json_file)

print("""
   _____      _            _             __  __           _            
 |  __ \    | |          | |           |  \/  |         | |           
 | |__) |__ | | _____  __| | _____  __ | \  / | __ _ ___| |_ ___ _ __ 
 |  ___/ _ \| |/ / _ \/ _` |/ _ \ \/ / | |\/| |/ _` / __| __/ _ \ '__|
 | |  | (_) |   <  __/ (_| |  __/>  <  | |  | | (_| \__ \ ||  __/ |   
 |_|   \___/|_|\_\___|\__,_|\___/_/\_\ |_|  |_|\__,_|___/\__\___|_|   
 """)
print("Our Pokemon experts in Pallet Town are looking for help in identifying a wild Pokemon, and we were hoping you could help as a Pokedex Master!")
print("We are only looking at Pokemon from the Kanto region (Which is also known as the Red/Blue region and also Gen 1)")
print("I hope you can figure this out before our 5 experts do!")
print()

choice = random.choice(pokedex)
wild_pokemon = Pokemon(choice.get("no"), choice.get("name"), choice.get("types"), 
                  choice.get("height"), choice.get("weight"), choice.get("abilities"), 
                  [choice.get("stats_names"), choice.get("stats_values")])
wild_pokemon.get_all_details() if random.random() >= 0.75 else wild_pokemon.get_random_details()
print()
guesses = 4 # allows 5 guesses
while True:
    print("Do you know this Pokemon's name? {0}".format(" ".join(wild_pokemon.comparison)))
    guess = input()
    wild_pokemon.update_comparison(guess.lower())
    print()
    if guesses == 0:
        print()
        print("Hmm........ the experts figured it out!")
        print(f"This is {wild_pokemon.name.title()}, which is #{wild_pokemon.no} in the Pokedex!")
        print("Keep training and you could become a Pokedex Master!")
        break
    if guess.lower() == wild_pokemon.name:
        print()
        print("Yeah thats the right one!")
        print(wild_pokemon.details[0])
        print("You really are a Pokedex Master!")
        break
    elif guesses > 0:
        print("That doesn't seem quite right, have another guess...")
    guesses -= 1