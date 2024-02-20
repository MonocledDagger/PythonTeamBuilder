from .print_players import print_players #Prints Players and Numbers
from .pickle_functions import save_pickle #Saves Pickle

def move_players(players):
    print("")
    print_players(players)

    move_from = input("Please Enter The INDEX of the Player You Want to Move: ")
    new_move_from="Player "+ move_from #Makes Key for dictionary
    move_to = input("Please Enter the INDEX of the Player you want to Switch With: ")
    new_move_to="Player " + move_to #Makes Key for dictionary

    try:
        # Swap the entire dictionary entries
        players[new_move_from], players[new_move_to] = players[new_move_to], players[new_move_from]

        save_pickle(players, 'player_data.pkl')
        print("Entry Moved successfully.")
    except KeyError:
        print("Invalid player Number. Please try again.")
    except Exception as e:
        print(f"Error Occurred: {e}. Please Try again")

        
        
        
        