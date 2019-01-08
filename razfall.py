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
            ],
        "Zoo": [
            "Zoo keeper",
            "Visitor",
            "School kid",
            "Parrot",
            "Animal activist",
            "Hunter"
            ],
        "Ski slope": [
            "Snowboarder",
            "Kid learning to ski",
            "Teenager with rich parents",
            "Ski instructor",
            "Hot chocolate vendor",
            "Pro freerider"
            ]
        }

no_of_players = 5

place = list(places.keys())[randint(0, len(places.keys())-1)]

print(place)

player_role_allocation = [role for role in places[place]][:no_of_players-1]
player_role_allocation.append("Spy")
random.shuffle(player_role_allocation)
print(player_role_allocation)
