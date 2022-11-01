import json
import random

print("Welcome to the world of Pokemon!")

with open("pokedex.json", "r") as json_file:
    pokedex = json.load(json_file)

print(len(pokedex))
print(pokedex[0])
print("Picking 5 random Pokemon:")
for i in range(5):
    pokemon = random.choice(pokedex)
    print(pokemon.get("no"), "-", pokemon.get("name").title(), ":", ",".join(pokemon.get("abilities")).title().replace("-", " "))
