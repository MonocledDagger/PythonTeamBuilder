from .positive_checker import zero_checker #Checks for less than 0 
from .pickle_functions import save_pickle, load_pickle #Saves and loads pickles

def add_player():
    try:
        # Load existing player data
        players = load_pickle('player_data.pkl')
    except FileNotFoundError:
        # If the file doesn't exist yet, create an empty dictionary
        players = {}

    positions = ["C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P"]
    player_num= (f"Player {len(players) + 1}") #Used To Make Key Name for dictionary
    name = input("Name of New Player: ")
    player_position = input("Position of Player: ").upper()

    while player_position not in positions: #Checks if position in positions list
        print("Please Input Valid Position")
        print(positions)
        print("")
        player_position = input("Position of Player: ").upper()

    at_bats = zero_checker(int(input("Input Number of At Bats:"))) #Get number of times at bat
    hits = zero_checker(int(input("Input Number of Hits:"))) #Get number of hits

    while hits > at_bats: #Asks for hits again if number of hits is greater than atbats
        print("Player Hits cannot be greater than At Bats")
        hits = zero_checker(int(input("Input Number of Hits:")))

    new_player = {'name': name, 'position': player_position, 'atbats': at_bats, 'hits': hits} #Creates new player

    # Append new player to the dictionary
    players[player_num] = new_player

    try:
        # Save the updated player data dictionary
        save_pickle(players, 'player_data.pkl')
        print("Player Successfully Added!")
    except:
        print("Something Went Wrong")
