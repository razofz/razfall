from random import randint
import random
import json
from flask import Flask, render_template, session
app = Flask(__name__)
import pudb

# we've got the best security in the world, tremendous
# will _absolutely_ remove this later.... TODO
app.secret_key = 'password123'

@app.route("/")
def start_page():
    # do an input field here, for no_of_players
    no_of_players = 5

    with open('places.json', 'r') as places_file:
        places = json.loads(places_file.read())

    place = list(places.keys())[randint(0, len(places.keys())-1)]

    player_role_allocation = [role for role in places[place]][:no_of_players-1]
    player_role_allocation.append("Spy")
    random.shuffle(player_role_allocation)

    session["no_of_players"] = no_of_players
    session["player_role_allocation"] = player_role_allocation
    session["place"] = place
    session["places"] = places
    session["player_number"] = -1

    return render_template('index.html') #, no_of_players)

@app.route("/give_roles")
def give_roles():
#     pudb.set_trace()

    player_number = session.get("player_number")
    are_roles_allocated = False

    if player_number == session.get("no_of_players")-2:
        are_roles_allocated = True

    player_number += 1
    session["player_number"] = player_number
            
    return render_template('give_roles.html', 
            are_roles_allocated=are_roles_allocated,
            role=session.get("player_role_allocation")[player_number],
            place=session.get("place")
            )

@app.route("/possible_places")
def possible_places():
    return render_template('possible_places.html', 
            places=list(session.get("places").keys()))

