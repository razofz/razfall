from random import randint
import random
import json

with open('places.txt', 'r') as places_file:
    places = json.loads(places_file.read())

# print(places)

no_of_players = 5

place = list(places.keys())[randint(0, len(places.keys())-1)]

print(place)

player_role_allocation = [role for role in places[place]][:no_of_players-1]
player_role_allocation.append("Spy")
random.shuffle(player_role_allocation)
print(player_role_allocation)
