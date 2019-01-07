from random import randint
import random

places = { 
        "University lecture": [
            "Lecturer",
            "Ambitious student",
            "Lazy student",
            "Student in wrong lecture",
            "Student that forgot a pen",
            "Tutor"
            ],
        "Scout campfire": [
            "Adult leader",
            "Overly ambitious scout",
            "Scout that just peed their pants",
            "Scout that loves fire a bit TOO much",
            "Older scout"
            ]
        }

no_of_players = 6

place = list(places.keys())[randint(0, len(places.keys())-1)]

print(place)

player_role_allocation = [role for role in places[place]]
player_role_allocation.append("Spy")
random.shuffle(player_role_allocation)
print(player_role_allocation)
